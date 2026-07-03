import { useEffect, useState } from "react";
import api from "../../services/api";
import type { Restaurant } from "../../types/prediction";

interface Props {
  value: Restaurant | null;
  onChange: (restaurant: Restaurant) => void;
}

export default function RestaurantDropdown({
  value,
  onChange,
}: Props) {
  const [restaurants, setRestaurants] = useState<Restaurant[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchRestaurants = async () => {
      try {
        const res = await api.get("/restaurants");
        setRestaurants(res.data);
      } catch (err) {
        console.error("Error fetching restaurants", err);
      } finally {
        setLoading(false);
      }
    };

    fetchRestaurants();
  }, []);

  return (
    <div className="mb-4">
      <label className="block mb-2 font-semibold">
        Restaurant
      </label>

      <select
        className="w-full border rounded-lg p-3"
        value={value?.id ?? ""}
        onChange={(e) => {
          const restaurant = restaurants.find(
            (r) => r.id === Number(e.target.value)
          );
          if (restaurant) onChange(restaurant);
        }}
      >
        <option value="">
          {loading ? "Loading..." : "Select Restaurant"}
        </option>

        {restaurants.map((r) => (
          <option key={r.id} value={r.id}>
            {r.name}
          </option>
        ))}
      </select>
    </div>
  );
}