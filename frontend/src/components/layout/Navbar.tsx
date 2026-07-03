import { Truck } from "lucide-react";

export default function Navbar() {
  return (
    <nav className="bg-white shadow-md border-b">
      <div className="max-w-7xl mx-auto h-16 px-6 flex items-center justify-between">

        <div className="flex items-center gap-3">
          <Truck className="text-blue-600" size={34} />
          <div>
            <h1 className="text-2xl font-bold text-blue-600">
              ETA Prediction Platform
            </h1>
            <p className="text-sm text-gray-500">
              AI Powered Delivery Time Prediction
            </p>
          </div>
        </div>

      </div>
    </nav>
  );
}