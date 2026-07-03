"""
EulerQ ETA Prediction Platform — FastAPI Backend
Endpoints: GET /health, POST /predict, POST /ai/query, GET /restaurants, GET /model/info
"""
import os, time
import traceback
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional

from app.predictor import ETAPredictor
from app.ai_assistant import answer_question

# ── app setup ─────────────────────────────────────────────────────────────────
app = FastAPI(
    title="EulerQ ETA Prediction API",
    description="AI-powered delivery ETA prediction for Bengaluru quick-commerce",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

START_TIME  = time.time()
BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH  = os.path.join(BASE_DIR, "eta_prediction_model.pkl")
predictor   = ETAPredictor(MODEL_PATH)

# ── schemas ───────────────────────────────────────────────────────────────────

class PredictRequest(BaseModel):
    lat:   float = Field(..., example=12.9716)
    lon:   float = Field(..., example=77.5946)
    lat_rider:        float = Field(..., example=12.965)
    lon_rider:        float = Field(..., example=77.589)
    drop_lat:         float = Field(..., example=12.980)
    drop_lon:         float = Field(..., example=77.610)
    vehicle_type:     str   = Field(..., example="bike")
    order_size:       int   = Field(..., ge=1, le=50, example=3)
    order_value:      float = Field(..., ge=0, example=450.0)
    cuisine:          Optional[str]   = Field("North Indian", example="Biryani")
    hour:             Optional[int]   = Field(None, ge=0, le=23)
    current_load:     Optional[float] = Field(1.0)
    shift_hours:      Optional[float] = Field(4.0)
    completed_orders: Optional[float] = Field(100.0)
    prep_capacity:    Optional[int]   = Field(10)
    avg_rating:       Optional[float] = Field(4.0)
    promised_eta:     Optional[float] = Field(None)


class AIRequest(BaseModel):
    question:           str            = Field(..., example="Why was this ETA predicted?")
    prediction_context: Optional[dict] = None


# ── endpoints ─────────────────────────────────────────────────────────────────

@app.get("/health")
def health():
    return {
        "status": "ok",
        "uptime_seconds": round(time.time() - START_TIME, 1),
        "model_loaded": True,
    }


@app.post("/predict")
def predict(req: PredictRequest):
    try:
        result = predictor.predict(req.model_dump())
        return result
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ai/query")
async def ai_query(req: AIRequest):
    try:
        answer = await answer_question(req.question, req.prediction_context)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/restaurants")
def list_restaurants():
    """Returns a sample list of Bengaluru restaurants for the frontend dropdown."""
    import pandas as pd
    try:
        rest_df = pd.read_csv(os.path.join(BASE_DIR, "restaurants.csv"))
        rest_df = rest_df.drop_duplicates().dropna(subset=["lat","lon"])
        cols = ["id","name","lat","lon","cuisine","avg_rating","prep_capacity"]
        cols = [c for c in cols if c in rest_df.columns]
        return rest_df[cols].head(100).fillna("").to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/riders")
def list_riders():
    """Returns a sample list of riders for the frontend dropdown."""
    import pandas as pd
    try:
        riders_df = pd.read_csv(os.path.join(BASE_DIR, "riders.csv"))
        riders_df = riders_df.drop_duplicates()
        cols = ["id","lat","lon","vehicle_type","completed_orders","shift_hours","current_load"]
        cols = [c for c in cols if c in riders_df.columns]
        return riders_df[cols].head(100).fillna(0).to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/model/info")
def model_info():
    return {
        "algorithm": "LightGBM (LGBMRegressor)",
        "n_estimators": 1000,
        "features": 42,
        "training_rows": 214489,
        "metrics": {"mae_min": 3.184, "rmse_min": 6.424, "r2": 0.5811},
        "feature_list": predictor.model.feature_name_,
    }