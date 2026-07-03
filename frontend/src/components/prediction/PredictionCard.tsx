import type { PredictResponse } from "../../types/prediction";

interface Props {
  prediction: PredictResponse | null;
}

export default function PredictionCard({ prediction }: Props) {

  if (!prediction)
    return <p>No prediction yet.</p>;

  return (

    <div className="space-y-4">

      <div>

        <h2 className="text-4xl font-bold text-blue-600">

          {prediction.predicted_eta_min} min

        </h2>

        <p>{prediction.eta_category}</p>

      </div>

      <div>

        <p>

          Confidence :

          <strong>

            {prediction.confidence}%

          </strong>

        </p>

      </div>

      <div>

        <p>

          Expected Delivery :

          <strong>

            {prediction.expected_delivery_time}

          </strong>

        </p>

      </div>

      <div>

        <p>{prediction.summary}</p>

      </div>

    </div>

  );

}