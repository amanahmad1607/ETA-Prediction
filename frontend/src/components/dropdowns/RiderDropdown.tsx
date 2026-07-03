import { useEffect, useState } from "react";
import api from "../../services/api";
import type { Rider } from "../../types/prediction";

interface Props {
  value: Rider | null;
  onChange: (rider: Rider) => void;
}

export default function RiderDropdown({
  value,
  onChange,
}: Props) {
  const [riders, setRiders] = useState<Rider[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchRiders = async () => {
      try {
        const res = await api.get("/riders");
        setRiders(res.data);
      } catch (err) {
        console.error("Error fetching riders", err);
      } finally {
        setLoading(false);
      }
    };

    fetchRiders();
  }, []);

  return (
    <div className="mb-4">
      <label className="block mb-2 font-semibold">
        Rider
      </label>

      <select
        className="w-full border rounded-lg p-3"
        value={value?.id ?? ""}
        onChange={(e) => {
          const rider = riders.find(
            (r) => r.id === Number(e.target.value)
          );
          if (rider) onChange(rider);
        }}
      >
        <option value="">
          {loading ? "Loading..." : "Select Rider"}
        </option>

        {riders.map((r) => (
          <option key={r.id} value={r.id}>
            Rider #{r.id}
          </option>
        ))}
      </select>
    </div>
  );
}