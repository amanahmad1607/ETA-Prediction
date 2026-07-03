export interface Restaurant {
  id: number;
  name: string;
  lat: number;
  lon: number;
  cuisine: string;
  avg_rating: number;
  prep_capacity: number;
}

export interface Rider {
  id: number;
  lat: number;
  lon: number;
  vehicle_type: string;
  completed_orders: number;
  shift_hours: number;
  current_load: number;
}
export interface PredictRequest {
  lat: number;
  lon: number;
  lat_rider: number;
  lon_rider: number;
  drop_lat: number;
  drop_lon: number;
  vehicle_type: string;
  order_size: number;
  order_value: number;
  cuisine: string;
  hour: number;
  current_load: number;
  shift_hours: number;
  completed_orders: number;
  prep_capacity: number;
  avg_rating: number;
  promised_eta: number;
}

export interface PredictResponse {
  predicted_eta_min: number;
  confidence: number;
  eta_category: string;
  expected_delivery_time: string;
  summary: string;

  breakdown: {
    rider_to_restaurant_km: number;
    restaurant_to_customer_km: number;
    total_distance_km: number;
    vehicle: string;
    estimated_travel_time_min: number;
    is_peak_hour: boolean;
    restaurant_rating: number;
    restaurant_load: number;
    completed_orders: number;
    current_load: number;
  };

  model_info: {
    algorithm: string;
    mae_min: number;
    rmse_min: number;
    r2: number;
  };
}