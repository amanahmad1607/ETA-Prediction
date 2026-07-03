import { useState } from "react";
import api from "../../services/api";
import type {
  Restaurant,
  Rider,
  PredictResponse,
} from "../../types/prediction";

import RestaurantDropdown from "../dropdowns/RestaurantDropdown";
import RiderDropdown from "../dropdowns/RiderDropdown";

interface Props {
  onPrediction: (data: PredictResponse) => void;
}

export default function PredictionForm({ onPrediction }: Props) {
  const [restaurant, setRestaurant] = useState<Restaurant | null>(null);
  const [rider, setRider] = useState<Rider | null>(null);

  const [dropLat, setDropLat] = useState(12.9800);
  const [dropLon, setDropLon] = useState(77.6100);

  const [orderSize, setOrderSize] = useState(2);
  const [orderValue, setOrderValue] = useState(350);

  const [loading, setLoading] = useState(false);

  const predictETA = async () => {
    if (!restaurant || !rider) {
      alert("Please select restaurant and rider.");
      return;
    }

    setLoading(true);

    try {
      const response = await api.post("/predict", {
        lat: restaurant.lat,
        lon: restaurant.lon,

        lat_rider: rider.lat,
        lon_rider: rider.lon,

        drop_lat: dropLat,
        drop_lon: dropLon,

        vehicle_type: rider.vehicle_type,

        order_size: orderSize,
        order_value: orderValue,

        cuisine: restaurant.cuisine,

        hour: new Date().getHours(),

        current_load: rider.current_load,
        shift_hours: rider.shift_hours,
        completed_orders: rider.completed_orders,

        prep_capacity: restaurant.prep_capacity,
        avg_rating: restaurant.avg_rating,

        promised_eta: 25,
      });

      onPrediction(response.data);

    } catch (err) {
      console.error(err);
      alert("Prediction failed.");
    }

    setLoading(false);
  };

  return (
    <div>

      <RestaurantDropdown
        value={restaurant}
        onChange={setRestaurant}
      />

      <RiderDropdown
        value={rider}
        onChange={setRider}
      />

      <div className="grid grid-cols-2 gap-4 mb-4">

        <input
          type="number"
          placeholder="Customer Latitude"
          value={dropLat}
          onChange={(e) => setDropLat(Number(e.target.value))}
          className="border rounded-lg p-3"
        />

        <input
          type="number"
          placeholder="Customer Longitude"
          value={dropLon}
          onChange={(e) => setDropLon(Number(e.target.value))}
          className="border rounded-lg p-3"
        />

      </div>

      <div className="grid grid-cols-2 gap-4 mb-4">

        <input
          type="number"
          placeholder="Order Size"
          value={orderSize}
          onChange={(e) => setOrderSize(Number(e.target.value))}
          className="border rounded-lg p-3"
        />

        <input
          type="number"
          placeholder="Order Value"
          value={orderValue}
          onChange={(e) => setOrderValue(Number(e.target.value))}
          className="border rounded-lg p-3"
        />

      </div>

      <button
        onClick={predictETA}
        disabled={loading}
        className="w-full bg-blue-600 hover:bg-blue-700 text-white rounded-lg p-3"
      >
        {loading ? "Predicting..." : "Predict ETA"}
      </button>

    </div>
  );
}