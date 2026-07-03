"""
predictor.py — loads trained LightGBM and builds exact 42-feature vector
"""
import os
from datetime import date,datetime, timedelta
import numpy as np
import pandas as pd
import joblib

SPEED_MAP = {"bike": 40, "bicycle": 15, "car": 35}

FEATURE_COLS = [
    "drop_lat","drop_lon","order_size","order_value","promised_eta",
    "hour","day","month","weekday","is_weekend","lat","lon","avg_rating",
    "prep_capacity","lat_rider","lon_rider","completed_orders",
    "shift_hours","current_load","peak_hour",
    "rider_restaurant_distance","restaurant_customer_distance",
    "total_distance","vehicle_speed","estimated_travel_time",
    "restaurant_load","restaurant_load_ratio","restaurant_efficiency",
    "load_ratio","order_complexity",
    "cuisine_Beverages","cuisine_Biryani","cuisine_Chinese",
    "cuisine_Continental","cuisine_Fast_Food","cuisine_Healthy_Bowls",
    "cuisine_Italian","cuisine_North_Indian","cuisine_South_Indian",
    "vehicle_type_bike","vehicle_type_car",
    "rider_experience_Expert","rider_experience_Intermediate",
]

def haversine_km(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1,lon1,lat2,lon2 = map(np.radians,[lat1,lon1,lat2,lon2])
    a = np.sin((lat2-lat1)/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin((lon2-lon1)/2)**2
    return R * 2 * np.arcsin(np.sqrt(np.clip(a,0,1)))

def normalise_vehicle(v):
    v = str(v).lower().strip()
    if v in ("bike","two_wheeler","scooter","e-scooter"): return "bike"
    if v in ("bicycle","cycle"): return "bicycle"
    if v in ("car","4-wheeler"): return "car"
    return "bike"

def rider_experience(n):
    if n <= 500: return "Beginner"
    if n <= 2000: return "Intermediate"
    return "Expert"

def peak_hour_flag(h):
    return int(11 <= h <= 14 or 18 <= h <= 22)

class ETAPredictor:
    def __init__(self, model_path):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model not found: {model_path}")
        self.model = joblib.load(model_path)

    def _build_features(self, req):
        now = datetime.now()
        hour  = int(req.get("hour")  or now.hour)
        day   = int(req.get("day")   or now.day)
        month = int(req.get("month") or now.month)

        rest_lat  = float(req["lat"])
        rest_lon  = float(req["lon"])
        rider_lat = float(req.get("lat_rider") or rest_lat)
        rider_lon = float(req.get("lon_rider") or rest_lon)
        drop_lat  = float(req["drop_lat"])
        drop_lon  = float(req["drop_lon"])

        d_rider_rest = haversine_km(rider_lat, rider_lon, rest_lat, rest_lon)
        d_rest_cust  = haversine_km(rest_lat, rest_lon, drop_lat, drop_lon)
        total_dist   = d_rider_rest + d_rest_cust

        vehicle      = normalise_vehicle(req.get("vehicle_type","bike"))
        speed        = SPEED_MAP.get(vehicle, 40)
        travel_time  = (d_rest_cust / speed) * 60

        completed    = float(req.get("completed_orders"))
        shift_hours  = float(req.get("shift_hours"))
        current_load = float(req.get("current_load"))
        exp          = rider_experience(completed)

        prep_capacity = int(req.get("prep_capacity"))
        avg_rating    = float(req.get("avg_rating"))
        cuisine       = str(req.get("cuisine"))
        order_size    = int(req.get("order_size"))
        order_value   = float(req.get("order_value"))

        promised_eta = req.get("promised_eta")
        if promised_eta is None:
            promised_eta = travel_time + 10
        promised_eta = float(promised_eta)

        weekday = datetime(
        datetime.now().year,
        month,
        day
        ).weekday()

        row = {
            "drop_lat": drop_lat, "drop_lon": drop_lon,
            "order_size": order_size, "order_value": order_value,
            "promised_eta": promised_eta,
            "hour": hour, "day": day, "month": month,
            "weekday": weekday,
            "is_weekend": int(weekday >= 5),
            "lat": rest_lat, "lon": rest_lon,
            "avg_rating": avg_rating, "prep_capacity": prep_capacity,
            "lat_rider": rider_lat, "lon_rider": rider_lon,
            "completed_orders": completed, "shift_hours": shift_hours,
            "current_load": current_load,
            "peak_hour": peak_hour_flag(hour),
            "rider_restaurant_distance": d_rider_rest,
            "restaurant_customer_distance": d_rest_cust,
            "total_distance": total_dist,
            "vehicle_speed": speed,
            "estimated_travel_time": travel_time,
            "restaurant_load": order_size * prep_capacity,
            "restaurant_load_ratio": current_load / (prep_capacity + 1),
            "restaurant_efficiency": avg_rating * prep_capacity,
            "load_ratio": current_load / (prep_capacity + 1),
            "order_complexity": order_size * order_value,
            "cuisine_Beverages":     int(cuisine=="Beverages"),
            "cuisine_Biryani":       int(cuisine=="Biryani"),
            "cuisine_Chinese":       int(cuisine=="Chinese"),
            "cuisine_Continental":   int(cuisine=="Continental"),
            "cuisine_Fast_Food":     int(cuisine=="Fast Food"),
            "cuisine_Healthy_Bowls": int(cuisine=="Healthy Bowls"),
            "cuisine_Italian":       int(cuisine=="Italian"),
            "cuisine_North_Indian":  int(cuisine=="North Indian"),
            "cuisine_South_Indian":  int(cuisine=="South Indian"),
            "vehicle_type_bike": int(vehicle=="bike"),
            "vehicle_type_car":  int(vehicle=="car"),
            "rider_experience_Expert":       int(exp=="Expert"),
            "rider_experience_Intermediate": int(exp=="Intermediate"),
        }
        features = pd.DataFrame([row])

        features = features[FEATURE_COLS]

        return features

    def predict(self, req):
        features     = self._build_features(req)
        eta          = float(self.model.predict(features)[0])
        eta          = max(5.0, round(eta, 1))

        # Confidence Score
        promised_eta = float(req.get("promised_eta", eta))

        confidence = max(
            60,
            min(
                99,
                100 - abs(eta - promised_eta)
                )
        )

        # ETA Category
        if eta <= 20:
            eta_category = "Fast"
        elif eta <= 35:
            eta_category = "Normal"
        else:
            eta_category = "Delayed"

        # Expected Delivery Time
        expected_delivery_time = (
            datetime.now() +
            timedelta(minutes=eta)
        ).strftime("%I:%M %p")

        rest_lat  = float(req["lat"])
        rest_lon  = float(req["lon"])
        rider_lat = float(req.get("lat_rider") or rest_lat)
        rider_lon = float(req.get("lon_rider") or rest_lon)
        drop_lat  = float(req["drop_lat"])
        drop_lon  = float(req["drop_lon"])
        vehicle   = normalise_vehicle(req.get("vehicle_type","bike"))
        speed     = SPEED_MAP.get(vehicle, 40)
        now       = datetime.now()
        hour      = int(req.get("hour") or now.hour)
        avg_rating = float(req.get("avg_rating", 4.0))
        prep_capacity = int(req.get("prep_capacity", 10))
        order_size = int(req.get("order_size", 2))
        completed_orders = float(req.get("completed_orders", 100))
        current_load = float(req.get("current_load", 1))
        

        d_rider_rest = haversine_km(rider_lat, rider_lon, rest_lat, rest_lon)
        d_rest_cust  = haversine_km(rest_lat, rest_lon, drop_lat, drop_lon)
        total_dist   = d_rider_rest + d_rest_cust
        travel_time  = (d_rest_cust / speed) * 60

# ---------- DEBUG ----------
        print("=" * 60)
        print("Restaurant :", rest_lat, rest_lon)
        print("Rider      :", rider_lat, rider_lon)
        print("Customer   :", drop_lat, drop_lon)

        print("Rider -> Restaurant :", round(d_rider_rest, 2), "km")
        print("Restaurant -> Customer :", round(d_rest_cust, 2), "km")
        print("Total Distance :", round(total_dist, 2), "km")
        print("=" * 60)
# ---------------------------
        summary = (
        f"The ETA is mainly influenced by the total distance of "
        f"{round(total_dist,2)} km, the restaurant workload, "
        f"and the rider's experience."
        )
        return {
        "predicted_eta_min": eta,
        "confidence": round(confidence, 1),
        "eta_category": eta_category,
        "expected_delivery_time": expected_delivery_time,
        "summary": summary,

        "breakdown": {
            "rider_to_restaurant_km": round(d_rider_rest, 2),
            "restaurant_to_customer_km": round(d_rest_cust, 2),
            "total_distance_km": round(total_dist, 2),
            "vehicle": vehicle,
            "estimated_travel_time_min": round(travel_time, 1),
            "is_peak_hour": bool(peak_hour_flag(hour)),
            "restaurant_rating": avg_rating,
            "restaurant_load": order_size * prep_capacity,
            "completed_orders": completed_orders,
            "current_load": current_load
        },

        "model_info": {
            "algorithm": "LightGBM",
            "mae_min": 3.184,
            "rmse_min": 6.424,
            "r2": 0.5811
        }
    }