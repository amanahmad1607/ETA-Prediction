import { useState } from "react";

import Navbar from "../components/layout/Navbar";
import Card from "../components/common/Card";

import PredictionForm from "../components/prediction/PredictionForm";
import PredictionCard from "../components/prediction/PredictionCard";
import BreakdownCard from "../components/prediction/BreakdownCard";
import type { PredictResponse } from "../types/prediction";
import AIChat from "../components/ai/AIChat";

export default function Dashboard() {

    const [prediction, setPrediction] =
        useState<PredictResponse | null>(null);

    return (

        <div className="min-h-screen bg-slate-100">

            <Navbar />

            <div className="max-w-7xl mx-auto p-8">

                <h2 className="text-3xl font-bold mb-2">

                    Delivery ETA Prediction

                </h2>

                <p className="text-gray-600 mb-8">

                    Predict delivery time using AI-powered LightGBM.

                </p>

                <div className="grid lg:grid-cols-2 gap-8">

                    <Card>

                        <PredictionForm
                            onPrediction={setPrediction}
                        />

                    </Card>

                    <div className="space-y-6">

                        <Card>

                            <PredictionCard
                                prediction={prediction}
                            />

                        </Card>

                        <Card>

                            <h2 className="text-xl font-bold mb-4">

                                📊 Breakdown

                            </h2>

                            <BreakdownCard
                                prediction={prediction}
                            />

                        </Card>
                        <Card>

                            <AIChat />

                        </Card>

                    </div>

                </div>

            </div>

        </div>

    );

}