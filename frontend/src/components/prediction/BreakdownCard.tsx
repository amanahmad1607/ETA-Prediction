import type { PredictResponse } from "../../types/prediction";
import {
    Route,
    Bike,
    Clock3,
    Star,
    Users,
    BriefcaseBusiness,
    Activity,
    Truck,
} from "lucide-react";

interface Props {
    prediction: PredictResponse | null;
}

export default function BreakdownCard({ prediction }: Props) {

    if (!prediction) {
        return (
            <div className="text-center py-10 text-gray-500">
                Make a prediction to see delivery insights.
            </div>
        );
    }

    const b = prediction.breakdown;

    return (

        <div className="grid grid-cols-2 gap-4">

            <InfoCard
                icon={<Route className="text-blue-600" />}
                title="Distance"
                value={`${b.total_distance_km} km`}
            />

            <InfoCard
                icon={<Clock3 className="text-green-600" />}
                title="Travel Time"
                value={`${b.estimated_travel_time_min} min`}
            />

            <InfoCard
                icon={<Bike className="text-orange-600" />}
                title="Vehicle"
                value={b.vehicle}
            />

            <InfoCard
                icon={<Activity className="text-red-600" />}
                title="Peak Hour"
                value={b.is_peak_hour ? "Yes" : "No"}
            />

            <InfoCard
                icon={<Star className="text-yellow-500" />}
                title="Rating"
                value={b.restaurant_rating}
            />

            <InfoCard
                icon={<Truck className="text-purple-600" />}
                title="Restaurant Load"
                value={b.restaurant_load}
            />

            <InfoCard
                icon={<Users className="text-indigo-600" />}
                title="Orders"
                value={b.completed_orders}
            />

            <InfoCard
                icon={<BriefcaseBusiness className="text-pink-600" />}
                title="Current Load"
                value={b.current_load}
            />

        </div>

    );

}

interface CardProps {
    icon: React.ReactNode;
    title: string;
    value: string | number;
}

function InfoCard({ icon, title, value }: CardProps) {

    return (

        <div className="bg-white rounded-xl shadow border p-4 hover:shadow-lg transition">

            <div className="flex items-center gap-2 mb-3">

                {icon}

                <span className="text-gray-600 font-medium">

                    {title}

                </span>

            </div>

            <div className="text-xl font-bold">

                {value}

            </div>

        </div>

    );

}