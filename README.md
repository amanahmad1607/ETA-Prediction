<div align="center">

# 🚚 ETA Prediction Platform
### AI-Powered Delivery Time Prediction using FastAPI, LightGBM, React & TypeScript

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green?logo=fastapi)
![React](https://img.shields.io/badge/React-18-61DAFB?logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue?logo=typescript)
![LightGBM](https://img.shields.io/badge/LightGBM-ML-orange)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![Vercel](https://img.shields.io/badge/Frontend-Vercel-black?logo=vercel)
![Render](https://img.shields.io/badge/Backend-Render-46E3B7)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

An end-to-end AI-powered ETA (Estimated Time of Arrival) prediction platform for food delivery and quick-commerce logistics. The platform leverages a LightGBM machine learning model, FastAPI backend, React + TypeScript frontend, AI assistant, and Dockerized deployment to predict delivery times accurately while providing detailed prediction explanations.

</div>

---

# 🌐 Live Demo

## Frontend

https://eta-prediction-ecru.vercel.app

## Backend API

https://eta-backend-xl9d.onrender.com

## Swagger Documentation

https://eta-backend-xl9d.onrender.com/docs

## GitHub Repository

https://github.com/amanahmad1607/ETA-Prediction

---

# 📌 Table of Contents

- Project Overview
- Problem Statement
- Solution Overview
- Key Features
- Technology Stack
- System Architecture
- Project Workflow
- Folder Structure
- Installation Guide
- Running Locally
- Docker Deployment
- Cloud Deployment
- Screenshots
- License

---

# 📖 Project Overview

Modern food delivery platforms such as Swiggy, Zomato, Uber Eats, and DoorDash rely heavily on accurate Estimated Time of Arrival (ETA) predictions. Incorrect ETAs reduce customer trust, increase operational inefficiencies, and impact rider allocation.

This project presents an AI-powered ETA Prediction Platform that estimates delivery time using a trained LightGBM regression model. The system integrates operational, spatial, and temporal features such as rider location, restaurant capacity, order characteristics, vehicle type, and travel distance to generate accurate predictions.

In addition to ETA prediction, the platform includes an AI assistant capable of explaining predictions and answering user queries regarding delivery performance.

---

# ❗ Problem Statement

Delivery companies face several operational challenges:

- Inaccurate delivery time estimation
- Dynamic rider allocation
- Varying restaurant preparation times
- Traffic and peak-hour delays
- Customer dissatisfaction due to inaccurate ETAs

Traditional rule-based systems often fail to capture complex relationships among multiple influencing factors.

This project addresses these issues using machine learning.

---

# 💡 Solution Overview

The system predicts delivery ETA using a LightGBM regression model trained on engineered delivery features.

Workflow:

Restaurant Selection
↓

Rider Selection
↓

Feature Engineering

↓

LightGBM Model

↓

ETA Prediction

↓

Prediction Explanation

↓

AI Assistant

---

# ⭐ Key Features

## Machine Learning

- LightGBM Regression Model
- 42 engineered features
- Real-time ETA prediction
- Confidence score
- ETA categorization
- Prediction breakdown

---

## Backend

- FastAPI REST API
- Automatic Swagger documentation
- Restaurant API
- Rider API
- AI Assistant API
- Model information endpoint
- CORS enabled
- Dockerized

---

## Frontend

- React
- TypeScript
- Tailwind CSS
- Responsive design
- Restaurant dropdown
- Rider dropdown
- ETA prediction dashboard
- Breakdown cards
- AI assistant
- Loading animations
- Error handling

---

## AI Assistant

The integrated AI assistant can answer questions such as:

- Why is my ETA high?
- How is ETA calculated?
- How can delivery become faster?
- What factors affect delivery time?
- Explain this prediction.

---

## Deployment

- Docker
- Docker Compose
- GitHub
- Render
- Vercel
- Automatic CI/CD

---

# 🛠 Technology Stack

| Category | Technology |
|------------|----------------|
| Language | Python |
| Backend | FastAPI |
| Frontend | React + TypeScript |
| Styling | Tailwind CSS |
| ML Model | LightGBM |
| Data Processing | Pandas, NumPy |
| API Testing | Swagger |
| AI Assistant | Groq LLM |
| Containerization | Docker |
| Deployment | Render + Vercel |
| Version Control | Git & GitHub |

---

# 🏗 System Architecture

```text
                    User

                      │

                      ▼

             React Frontend
          (TypeScript + Tailwind)

                      │
             REST API Requests

                      ▼

               FastAPI Backend

                      │

          Feature Engineering

                      ▼

          LightGBM ETA Predictor

                      │

      Prediction + Confidence Score

                      │

         AI Assistant Explanation

                      ▼

            JSON Response

                      │

                      ▼

             React Dashboard
```

---

# 🔄 Application Workflow

```text
User

↓

Select Restaurant

↓

Select Rider

↓

Enter Order Details

↓

React Frontend

↓

FastAPI Backend

↓

Feature Engineering

↓

LightGBM Model

↓

ETA Prediction

↓

AI Explanation

↓

Dashboard Results
```

---

# 📂 Project Structure

```text
ETA-Prediction/

├── backend/
│
│   ├── app/
│   │   ├── predictor.py
│   │   ├── ai_assistant.py
│   │   ├── __init__.py
│   │
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── eta_prediction_model.pkl
│   ├── restaurants.csv
│   └── riders.csv
│
├── frontend/
│
│   ├── src/
│   │
│   ├── components/
│   ├── pages/
│   ├── services/
│   ├── types/
│   ├── Dockerfile
│   ├── package.json
│   └── vite.config.ts
│
├── docker-compose.yml
│
├── README.md
│
└── LICENSE
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/amanahmad1607/ETA-Prediction.git

cd ETA-Prediction
```

---

## Backend Setup

```bash
cd backend

python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
uvicorn main:app --reload
```

Backend

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend

```
http://localhost:5173
```

---

# 🐳 Docker

Backend

```bash
docker build -t eta-backend backend

docker run -p 8000:8000 eta-backend
```

Frontend

```bash
docker build -t eta-frontend frontend

docker run -p 5173:5173 eta-frontend
```

Docker Compose

```bash
docker compose up
```

---

# ☁ Cloud Deployment

## Backend

Hosted on Render

https://eta-backend-xl9d.onrender.com

---

## Frontend

Hosted on Vercel

https://eta-prediction-ecru.vercel.app

---

# 📸 Screenshots

> Add screenshots here.

Suggested screenshots:

- Dashboard
- Prediction Form
- Prediction Result
- Breakdown Cards
- AI Assistant
- Swagger API
- Docker Containers

Example:

```
docs/images/dashboard.png

docs/images/result.png

docs/images/chat.png
```

---

# 📜 License

This project is licensed under the MIT License.

---

<div align="center">

⭐ If you found this project useful, consider giving it a star on GitHub!

</div>


# 📊 Dataset Analysis

## Dataset Overview

The ETA Prediction model is trained on a structured delivery dataset containing information related to restaurants, riders, orders, delivery locations, and operational conditions.

Each record represents a single completed delivery and includes spatial, temporal, operational, and order-specific information used to predict the Estimated Time of Arrival (ETA).

### Dataset Characteristics

| Property | Value |
|----------|--------|
| Dataset Type | Structured Tabular Data |
| Problem Type | Regression |
| Target Variable | Delivery ETA (minutes) |
| Model | LightGBM Regressor |
| Features Used | 42 |
| Prediction Type | Continuous |

---

# Dataset Schema

The dataset contains information from four major domains:

## 1. Restaurant Information

- Restaurant Latitude
- Restaurant Longitude
- Average Rating
- Preparation Capacity
- Cuisine Type

These features represent restaurant efficiency and preparation capability.

---

## 2. Rider Information

- Rider Latitude
- Rider Longitude
- Completed Orders
- Shift Hours
- Current Delivery Load
- Experience Level

These features model rider availability and operational efficiency.

---

## 3. Order Information

- Order Size
- Order Value
- Cuisine
- Vehicle Type
- Promised ETA

These variables describe the complexity of the delivery.

---

## 4. Delivery Information

- Customer Latitude
- Customer Longitude
- Travel Distance
- Peak Hour
- Estimated Travel Time
- Total Distance

These are the most important predictors influencing ETA.

---

# 🎯 Target Variable

The machine learning model predicts:

```

Delivery ETA (minutes)

```

This is a continuous numerical variable.

Example

| Delivery | Actual ETA |
|----------|------------|
| Order 1 | 18.4 min |
| Order 2 | 27.8 min |
| Order 3 | 42.3 min |

---

# 🧹 Data Preprocessing

Before training the model, several preprocessing steps were applied.

## Missing Values

Missing values were handled using default operational values.

Examples:

| Feature | Default Value |
|-----------|--------------|
| Average Rating | 4.0 |
| Prep Capacity | 10 |
| Current Load | 1 |
| Shift Hours | 4 |
| Completed Orders | 100 |

This ensured no missing values remained during training.

---

## Data Type Conversion

Categorical variables were converted into machine-learning compatible formats.

Examples:

```

Bike

↓

vehicle_type_bike = 1

vehicle_type_car = 0

```

Cuisine categories were transformed using one-hot encoding.

---

## Date-Time Processing

Temporal features were extracted from timestamps.

Generated features include:

- Hour
- Day
- Month
- Weekday
- Weekend Flag

These improve prediction during peak operational periods.

---

# 📈 Feature Engineering

One of the strongest aspects of the project is extensive feature engineering.

Although the raw dataset contains basic delivery information, multiple derived features were generated to improve prediction performance.

---

## Spatial Features

### Rider → Restaurant Distance

Calculated using the Haversine Formula.

```

Rider

↓

Restaurant

```

---

### Restaurant → Customer Distance

```

Restaurant

↓

Customer

```

---

### Total Distance

```

Rider

↓

Restaurant

↓

Customer

```

```
Total Distance =
Rider-Restaurant Distance
+
Restaurant-Customer Distance
```

---

# Vehicle Speed

Vehicle-specific average speeds are assigned.

| Vehicle | Speed |
|----------|---------|
| Bike | 40 km/h |
| Bicycle | 15 km/h |
| Car | 35 km/h |

Estimated travel time:

```
Travel Time

=

Distance

÷

Speed
```

---

# Peak Hour Feature

Peak delivery hours:

Morning

```
11 AM – 2 PM
```

Evening

```
6 PM – 10 PM
```

Binary encoding

```
Peak Hour = 1

Non Peak = 0
```

---

# Restaurant Features

Several restaurant-related engineered features improve prediction.

## Restaurant Load

```
Restaurant Load

=

Order Size

×

Preparation Capacity
```

---

## Restaurant Load Ratio

```
Current Rider Load

÷

Preparation Capacity
```

---

## Restaurant Efficiency

```
Average Rating

×

Preparation Capacity
```

Higher efficiency generally reduces ETA.

---

# Rider Features

Rider experience is categorized.

| Completed Orders | Experience |
|------------------|-------------|
| 0 – 500 | Beginner |
| 501 – 2000 | Intermediate |
| >2000 | Expert |

This feature helps model rider efficiency.

---

# Order Complexity

```
Order Complexity

=

Order Size

×

Order Value
```

Larger, higher-value orders typically require more preparation time.

---

# Final Feature Set

The model uses **42 engineered features**.

Feature groups include:

- Spatial Features
- Time Features
- Rider Features
- Restaurant Features
- Order Features
- Vehicle Features
- Cuisine Features
- Operational Features

---

# 🤖 Model Selection

Several regression algorithms were considered.

| Algorithm | Suitable |
|------------|----------|
| Linear Regression | ❌ |
| Decision Tree | ⚠️ |
| Random Forest | ✅ |
| XGBoost | ✅ |
| CatBoost | ✅ |
| **LightGBM** | ⭐ Selected |

---

# Why LightGBM?

LightGBM was selected because it provides:

- Fast training
- Low memory usage
- High accuracy
- Handles non-linear relationships
- Works well on tabular datasets
- Excellent feature interaction modeling

It is widely used in production ML systems for structured data problems.

---

# Model Training Pipeline

```
Raw Dataset

↓

Cleaning

↓

Feature Engineering

↓

Train/Test Split

↓

LightGBM Training

↓

Hyperparameter Optimization

↓

Evaluation

↓

Model Serialization

↓

eta_prediction_model.pkl
```

---

# Model Serialization

After training, the model was stored using Joblib.

```python
joblib.dump(model, "eta_prediction_model.pkl")
```

During prediction:

```python
model = joblib.load("eta_prediction_model.pkl")
```

This allows fast inference without retraining.

---

# 📊 Model Evaluation

The model was evaluated using standard regression metrics.

## Mean Absolute Error (MAE)

```
3.184 minutes
```

Lower is better.

---

## Root Mean Squared Error (RMSE)

```
6.424 minutes
```

Measures average prediction deviation.

---

## R² Score

```
0.5811
```

This indicates the model explains approximately **58% of the variance** in delivery times on the evaluation dataset.

---

# Prediction Response

The backend returns:

```json
{
  "predicted_eta_min": 26.1,
  "confidence": 73.9,
  "eta_category": "Normal",
  "expected_delivery_time": "07:42 PM",
  "summary": "ETA is mainly influenced by total distance and restaurant workload."
}
```

---

# Model Strengths

✔ Extensive Feature Engineering

✔ Distance-based Prediction

✔ Restaurant Capacity Modeling

✔ Rider Experience Modeling

✔ Peak Hour Awareness

✔ Operational Features

✔ Real-time Prediction

✔ Explainable Results

✔ AI Assistant Integration

---

# Current Limitations

The current implementation does not explicitly model:

- Live traffic conditions
- Weather information
- Road closures
- Dynamic rider reassignment
- Restaurant preparation delays beyond capacity estimation
- GPS route optimization

These can be incorporated in future versions.

---

# Future Model Improvements

Potential enhancements include:

- XGBoost Comparison
- CatBoost Benchmarking
- Ensemble Models
- Deep Learning Regression
- Graph Neural Networks
- Live Traffic API Integration
- Real-time GPS Tracking
- Online Model Retraining
- MLOps Pipeline
- Drift Detection

---

# Summary

The ETA Prediction model combines extensive feature engineering with a LightGBM regression model to accurately estimate food delivery times. By integrating spatial, temporal, operational, rider, and restaurant information, the system delivers reliable ETA predictions suitable for real-world logistics applications.


# 📡 API Documentation

The ETA Prediction Platform exposes a RESTful API built with **FastAPI**. The API enables clients to predict delivery ETAs, retrieve restaurant and rider information, interact with the AI assistant, and inspect model metadata.

---

# API Overview

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/predict` | Predict delivery ETA |
| POST | `/ai/query` | AI assistant |
| GET | `/restaurants` | List restaurants |
| GET | `/riders` | List riders |
| GET | `/model/info` | Model metadata |
| GET | `/docs` | Swagger UI |

---

# Base URL

### Local

```
http://localhost:8000
```

### Production

```
https://eta-backend-xl9d.onrender.com
```

---

# Swagger Documentation

FastAPI automatically generates interactive API documentation.

Production:

```
https://eta-backend-xl9d.onrender.com/docs
```

Features:

- Interactive API testing
- Request validation
- Response schemas
- Example payloads
- Error documentation

---

# 1️⃣ Health Check API

## Endpoint

```http
GET /health
```

### Description

Checks whether the backend is running correctly and verifies that the ML model has been loaded.

---

### Request

```http
GET /health
```

---

### Response

```json
{
  "status": "ok",
  "uptime_seconds": 128.4,
  "model_loaded": true
}
```

---

### Response Fields

| Field | Type | Description |
|--------|------|-------------|
| status | string | API status |
| uptime_seconds | float | Server uptime |
| model_loaded | boolean | Indicates model availability |

---

# 2️⃣ ETA Prediction API

## Endpoint

```http
POST /predict
```

### Description

Predicts delivery ETA using the trained LightGBM regression model.

---

## Request Body

```json
{
  "lat": 12.9716,
  "lon": 77.5946,
  "lat_rider": 12.965,
  "lon_rider": 77.589,
  "drop_lat": 12.980,
  "drop_lon": 77.610,
  "vehicle_type": "bike",
  "order_size": 3,
  "order_value": 450,
  "cuisine": "North Indian",
  "hour": 19,
  "current_load": 1,
  "shift_hours": 4,
  "completed_orders": 1200,
  "prep_capacity": 12,
  "avg_rating": 4.5,
  "promised_eta": 25
}
```

---

## Request Parameters

| Parameter | Type | Description |
|------------|------|-------------|
| lat | float | Restaurant latitude |
| lon | float | Restaurant longitude |
| lat_rider | float | Rider latitude |
| lon_rider | float | Rider longitude |
| drop_lat | float | Customer latitude |
| drop_lon | float | Customer longitude |
| vehicle_type | string | bike/car/bicycle |
| order_size | integer | Number of items |
| order_value | float | Order value |
| cuisine | string | Cuisine type |
| hour | integer | Delivery hour |
| current_load | integer | Current rider load |
| shift_hours | float | Rider shift duration |
| completed_orders | integer | Completed deliveries |
| prep_capacity | integer | Restaurant preparation capacity |
| avg_rating | float | Restaurant rating |
| promised_eta | float | Expected ETA |

---

## Success Response

```json
{
  "predicted_eta_min": 26.1,
  "confidence": 73.9,
  "eta_category": "Normal",
  "expected_delivery_time": "07:42 PM",
  "summary": "The ETA is mainly influenced by total distance, restaurant workload and rider experience.",
  "breakdown": {
    "rider_to_restaurant_km": 0.95,
    "restaurant_to_customer_km": 1.91,
    "total_distance_km": 2.86,
    "vehicle": "bike",
    "estimated_travel_time_min": 2.9,
    "is_peak_hour": true,
    "restaurant_rating": 4.5,
    "restaurant_load": 36,
    "completed_orders": 1200,
    "current_load": 1
  },
  "model_info": {
    "algorithm": "LightGBM",
    "mae_min": 3.184,
    "rmse_min": 6.424,
    "r2": 0.5811
  }
}
```

---

## Response Description

### Prediction

| Field | Description |
|--------|-------------|
| predicted_eta_min | Predicted ETA |
| confidence | Confidence score |
| eta_category | Fast / Normal / Delayed |
| expected_delivery_time | Estimated arrival time |
| summary | Human-readable explanation |

---

### Breakdown

Contains detailed reasoning behind the prediction.

Includes

- Rider distance
- Customer distance
- Total distance
- Vehicle
- Travel time
- Peak hour
- Restaurant load
- Rider load

---

### Model Info

Provides information regarding

- Algorithm
- MAE
- RMSE
- R² Score

---

# 3️⃣ AI Assistant API

## Endpoint

```http
POST /ai/query
```

---

## Description

Provides natural language explanations about ETA predictions using an AI assistant.

---

## Request

```json
{
    "question":"Why is my ETA high?",
    "prediction_context":{
        "predicted_eta":26.1,
        "distance":2.86,
        "restaurant_load":36
    }
}
```

---

## Response

```json
{
    "answer":"Your ETA is mainly influenced by the total delivery distance and the restaurant workload. During busy hours, preparation time also contributes to the overall delivery estimate."
}
```

---

## Example Questions

- Why is my ETA high?
- Explain this prediction.
- How is ETA calculated?
- Can delivery become faster?
- Which feature affected ETA the most?

---

# 4️⃣ Restaurants API

## Endpoint

```http
GET /restaurants
```

---

## Description

Returns available restaurants for frontend dropdown selection.

---

## Example Response

```json
[
  {
    "id":1,
    "name":"Paradise Biryani",
    "lat":12.9716,
    "lon":77.5946,
    "cuisine":"Biryani",
    "avg_rating":4.6,
    "prep_capacity":15
  }
]
```

---

# 5️⃣ Riders API

## Endpoint

```http
GET /riders
```

---

## Description

Returns rider information for frontend selection.

---

## Example Response

```json
[
  {
    "id":11,
    "lat":12.965,
    "lon":77.589,
    "vehicle_type":"bike",
    "completed_orders":1320,
    "shift_hours":5,
    "current_load":1
  }
]
```

---

# 6️⃣ Model Information API

## Endpoint

```http
GET /model/info
```

---

## Description

Returns metadata about the trained ML model.

---

## Response

```json
{
  "algorithm":"LightGBM",
  "features":42,
  "training_rows":214489,
  "metrics":{
      "mae_min":3.184,
      "rmse_min":6.424,
      "r2":0.5811
  }
}
```

---

# HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 400 | Invalid Request |
| 404 | Resource Not Found |
| 422 | Validation Error |
| 500 | Internal Server Error |

---

# Error Response

```json
{
    "detail":"Validation Error"
}
```

---

# Authentication

Current version does **not** require authentication.

Future versions may include

- JWT Authentication
- OAuth2
- API Keys

---

# Rate Limiting

Current version

- No rate limiting

Future versions

- Redis
- API Gateway
- Request throttling

---

# API Workflow

```
Client

↓

HTTP Request

↓

FastAPI

↓

Validation

↓

Feature Engineering

↓

LightGBM Model

↓

Prediction

↓

AI Explanation

↓

JSON Response

↓

Frontend Dashboard
```

---

# Testing the API

The API can be tested using:

- Swagger UI
- Postman
- Insomnia
- cURL
- Frontend Application

---

# Example cURL Request

```bash
curl -X POST \
http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '{
  "lat":12.9716,
  "lon":77.5946,
  "lat_rider":12.965,
  "lon_rider":77.589,
  "drop_lat":12.980,
  "drop_lon":77.610,
  "vehicle_type":"bike",
  "order_size":3,
  "order_value":450,
  "cuisine":"North Indian",
  "hour":19,
  "current_load":1,
  "shift_hours":4,
  "completed_orders":1200,
  "prep_capacity":12,
  "avg_rating":4.5,
  "promised_eta":25
}'
```

---

# API Highlights

- FastAPI-based REST API
- Automatic request validation
- Interactive Swagger UI
- ML-powered ETA prediction
- AI-assisted explanations
- Modular endpoint design
- JSON-based communication
- Production-ready deployment

---

# 🚀 Deployment Guide

The ETA Prediction Platform is deployed as a cloud-native application using Docker containers and modern deployment platforms.

The project follows a full-stack deployment architecture:

```
GitHub
      │
      │
      ├──────────────┐
      │              │
      ▼              ▼
 Render          Vercel
 Backend        Frontend
      │              │
      └──── REST API ────┘
             │
             ▼
     LightGBM Predictor
```

---

# 🌍 Production Deployment

## Backend

Platform

```
Render
```

Live URL

```
https://eta-backend-xl9d.onrender.com
```

Swagger

```
https://eta-backend-xl9d.onrender.com/docs
```

---

## Frontend

Platform

```
Vercel
```

Live URL

```
https://eta-prediction-ecru.vercel.app
```

---

# 🐳 Docker

The application is fully containerized.

Separate Docker containers are created for

- Backend
- Frontend

This enables

- Consistent deployments
- Environment isolation
- Easy scalability
- Platform independence

---

# Backend Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh","-c","uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
```

---

# Frontend Dockerfile

```dockerfile
FROM node:22

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 5173

CMD ["npm","run","dev","--","--host"]
```

---

# Docker Compose

The project includes a Docker Compose configuration for running both services together.

```yaml
version: "3.9"

services:

  backend:

    build: ./backend

    ports:

      - "8000:8000"

  frontend:

    build: ./frontend

    ports:

      - "5173:5173"

    depends_on:

      - backend
```

---

# Running Using Docker

## Build Images

Backend

```bash
docker build -t eta-backend backend
```

Frontend

```bash
docker build -t eta-frontend frontend
```

---

## Run Backend

```bash
docker run -p 8000:8000 eta-backend
```

---

## Run Frontend

```bash
docker run -p 5173:5173 eta-frontend
```

---

## Using Docker Compose

```bash
docker compose up
```

Both services start automatically.

---

# ⚙ Environment Variables

## Backend

Example

```
GROQ_API_KEY=xxxxxxxxxxxxxxxx
```

---

## Frontend

Example

```
VITE_API_URL=https://eta-backend-xl9d.onrender.com
```

---

# Render Deployment

Backend deployment is hosted on Render.

Deployment Steps

1.

Connect GitHub Repository

↓

2.

Choose Root Directory

```
backend
```

↓

3.

Docker Runtime

↓

4.

Automatic Build

↓

5.

Deploy

---

Render automatically

```
GitHub Push

↓

Docker Build

↓

Container Deployment

↓

Public URL
```

---

# Vercel Deployment

Frontend deployment uses Vercel.

Deployment Steps

```
Import GitHub Repository

↓

Choose

frontend

↓

npm install

↓

npm run build

↓

Deploy
```

---

Environment Variable

```
VITE_API_URL

=

https://eta-backend-xl9d.onrender.com
```

---

# Continuous Integration / Continuous Deployment

The project uses GitHub integration with Render and Vercel.

Whenever code is pushed

```
git push
```

Automatic workflow

```
GitHub

↓

Render detects change

↓

Backend rebuild

↓

Deploy

────────────

GitHub

↓

Vercel detects change

↓

Frontend rebuild

↓

Deploy
```

No manual deployment is required after the initial setup.

---

# Production Architecture

```
                Internet

                    │

                    ▼

        React Frontend (Vercel)

                    │

          HTTPS REST API Calls

                    ▼

        FastAPI Backend (Render)

                    │

          Feature Engineering

                    ▼

          LightGBM Prediction

                    │

          AI Explanation Layer

                    ▼

              JSON Response
```

---

# Component Architecture

```
+------------------------+

      React Frontend

+------------------------+

            │

            ▼

+------------------------+

        FastAPI API

+------------------------+

      │            │

      ▼            ▼

Prediction     AI Assistant

      │

      ▼

LightGBM Model

      │

      ▼

Prediction Response
```

---

# Deployment Workflow

```
Developer

↓

Git Commit

↓

Git Push

↓

GitHub Repository

↓

Render

↓

Backend

↓

Vercel

↓

Frontend

↓

Production
```

---

# Monitoring

Current monitoring includes

- Render Logs
- FastAPI Exception Handling
- HTTP Status Codes
- Browser Console
- Swagger Testing

Future monitoring

- Prometheus
- Grafana
- OpenTelemetry
- Sentry
- ELK Stack

---

# Logging

Backend logs include

- API Requests
- Exceptions
- Prediction Errors
- Startup Logs

Future improvements

- Structured Logging
- JSON Logs
- Centralized Logging

---

# Security

Current Security Features

- Request Validation (Pydantic)
- Input Type Checking
- FastAPI Validation
- CORS Configuration
- Error Handling

Future Security Enhancements

- JWT Authentication
- OAuth2
- HTTPS Certificates
- API Keys
- Rate Limiting
- CSRF Protection
- Request Signing

---

# Scalability

The architecture supports horizontal scaling.

Possible scaling strategy

```
                 Load Balancer

                      │

      ┌───────────────┼───────────────┐

      ▼               ▼               ▼

 FastAPI 1      FastAPI 2      FastAPI 3

      │               │               │

      └────────── Shared ML Model ───────────┘
```

---

# Future Cloud Architecture

```
React

↓

CloudFront

↓

API Gateway

↓

FastAPI

↓

Redis Cache

↓

LightGBM

↓

PostgreSQL

↓

Monitoring
```

---

# Disaster Recovery

Recommended improvements

- Daily Model Backup
- Cloud Storage Backup
- Database Backup
- GitHub Repository Backup
- Infrastructure as Code

---

# Production Readiness Checklist

| Feature | Status |
|----------|---------|
| Docker | ✅ |
| Docker Compose | ✅ |
| Render Deployment | ✅ |
| Vercel Deployment | ✅ |
| CI/CD | ✅ |
| REST API | ✅ |
| ML Model | ✅ |
| AI Assistant | ✅ |
| Swagger | ✅ |
| Monitoring | Basic |
| Logging | Basic |
| Authentication | Planned |
| HTTPS | ✅ |
| Error Handling | ✅ |

---

# Deployment Summary

The ETA Prediction Platform follows a modern cloud-native deployment strategy using Docker containers, GitHub-based CI/CD, Render for backend hosting, and Vercel for frontend deployment. This architecture provides a scalable, maintainable, and production-ready environment while keeping deployment simple and automated.


# 🔮 Future Scope

The current ETA Prediction Platform demonstrates a complete end-to-end machine learning application. However, there are several opportunities for future enhancements to improve prediction accuracy, scalability, and user experience.

## Machine Learning Improvements

### Live Traffic Integration

Current ETA estimation relies primarily on historical and engineered features. Future versions can integrate:

- Google Maps Traffic API
- OpenStreetMap Traffic Data
- HERE Maps
- TomTom Traffic API

This would allow the model to incorporate real-time congestion into ETA predictions.

---

### Weather Integration

Weather conditions have a significant impact on delivery times.

Possible integrations:

- OpenWeather API
- WeatherAPI
- Tomorrow.io

Weather features could include:

- Rainfall
- Temperature
- Visibility
- Wind Speed
- Storm Alerts

---

### Advanced Machine Learning Models

Current model:

- LightGBM Regressor

Potential comparisons:

- XGBoost
- CatBoost
- Random Forest
- Extra Trees
- Neural Networks
- TabNet

Future versions may also use ensemble learning to improve prediction robustness.

---

### Continuous Model Retraining

Implement an automated ML pipeline that periodically retrains the model using newly collected delivery data.

Possible workflow:

```
New Delivery Data

↓

Data Validation

↓

Feature Engineering

↓

Model Training

↓

Evaluation

↓

Deploy Updated Model
```

---

### Explainable AI (XAI)

Integrate model interpretation techniques such as:

- SHAP Values
- LIME
- Partial Dependence Plots

This would provide users with more transparent explanations of predictions.

---

# 🚀 Future Product Features

## Authentication

Implement secure user authentication using:

- JWT Authentication
- OAuth 2.0
- Google Sign-In

---

## Order History

Store previous predictions to allow users to:

- View prediction history
- Compare historical ETAs
- Analyze delivery trends

---

## Interactive Maps

Integrate Google Maps or Leaflet to display:

- Restaurant Location
- Rider Location
- Customer Location
- Delivery Route

---

## Live Rider Tracking

Use WebSockets to provide real-time rider movement and continuously update ETA predictions.

---

## Notifications

Notify customers through:

- Email
- SMS
- Push Notifications

---

## Admin Dashboard

Develop an administrative portal to monitor:

- Delivery statistics
- Rider performance
- Restaurant efficiency
- Prediction accuracy

---

# ☁️ Scalability Roadmap

The platform can be extended into a production-grade distributed architecture.

```
Users

↓

Load Balancer

↓

React Frontend

↓

API Gateway

↓

FastAPI Cluster

↓

Redis Cache

↓

ML Prediction Service

↓

PostgreSQL

↓

Monitoring
```

---

# 📈 MLOps Roadmap

Future MLOps enhancements include:

- MLflow
- DVC
- Kubeflow
- Airflow
- Model Versioning
- Drift Detection
- Automated Retraining

---

# 📷 Screenshots

Include screenshots of the following pages.

## Home Dashboard

```
docs/images/dashboard.png
```

---

## Prediction Form

```
docs/images/form.png
```

---

## Prediction Result

```
docs/images/result.png
```

---

## Breakdown Card

```
docs/images/breakdown.png
```

---

## AI Assistant

```
docs/images/chat.png
```

---

## Swagger Documentation

```
docs/images/swagger.png
```

---

## Docker Containers

```
docs/images/docker.png
```

---

# 🎥 Demo Video Script

## Duration

Approximately **3–5 minutes**

---

### 1. Introduction (30 seconds)

"Hello everyone.

This project is an AI-powered ETA Prediction Platform built using FastAPI, LightGBM, React, and TypeScript. It predicts delivery times for food delivery services and provides AI-generated explanations for every prediction."

---

### 2. Architecture (45 seconds)

Explain:

- React Frontend
- FastAPI Backend
- LightGBM Model
- AI Assistant
- Docker
- Render
- Vercel

---

### 3. Frontend Demonstration (1 minute)

Show:

- Restaurant dropdown
- Rider dropdown
- Order form
- Predict button

Generate an ETA prediction.

---

### 4. Prediction Explanation (45 seconds)

Discuss:

- ETA
- Confidence Score
- Breakdown Cards
- Distance
- Rider Experience
- Restaurant Load

---

### 5. AI Assistant (30 seconds)

Ask questions such as:

- Why is my ETA high?
- How can delivery become faster?
- Explain this prediction.

Show AI-generated responses.

---

### 6. Backend (30 seconds)

Open Swagger:

```
/docs
```

Demonstrate:

- /predict
- /restaurants
- /riders
- /ai/query

---

### 7. Deployment (30 seconds)

Show:

GitHub Repository

↓

Render Backend

↓

Vercel Frontend

↓

Docker Support

---

### 8. Conclusion

"This project demonstrates full-stack AI application development using modern deployment practices, machine learning, and cloud-native architecture."

---

# ❓ Frequently Asked Questions

### Why LightGBM?

LightGBM performs exceptionally well on structured/tabular data while offering fast training and inference.

---

### Why FastAPI?

FastAPI provides automatic validation, excellent performance, and interactive API documentation.

---

### Why React + TypeScript?

React enables reusable UI components, while TypeScript improves code quality and maintainability.

---

### Why Docker?

Docker ensures consistent environments across development, testing, and deployment.

---

### Why Render + Vercel?

These platforms provide free, reliable hosting with automatic deployments integrated with GitHub.

---

# 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 📚 References

- FastAPI Documentation
- React Documentation
- TypeScript Documentation
- LightGBM Documentation
- Docker Documentation
- Vercel Documentation
- Render Documentation
- Pandas Documentation
- NumPy Documentation

---

# 🙏 Acknowledgements

Special thanks to:

- FastAPI Team
- React Team
- Microsoft TypeScript Team
- LightGBM Contributors
- Docker Community
- Render
- Vercel
- Open Source Community

---

# 📄 License

This project is licensed under the MIT License.

---

# ✅ Submission Checklist

## Source Code

- [x] FastAPI Backend
- [x] React + TypeScript Frontend
- [x] LightGBM Model
- [x] AI Assistant

---

## Machine Learning

- [x] Feature Engineering
- [x] Model Serialization
- [x] Evaluation Metrics
- [x] Prediction API

---

## Frontend

- [x] Dashboard
- [x] Dropdowns
- [x] Prediction Form
- [x] Breakdown Cards
- [x] AI Chat

---

## DevOps

- [x] Docker
- [x] Docker Compose
- [x] Render Deployment
- [x] Vercel Deployment
- [x] CI/CD

---

## Documentation

- [x] Project Overview
- [x] Architecture
- [x] API Documentation
- [x] Deployment Guide
- [x] Future Scope
- [x] README

---

## Live Links

### GitHub Repository

https://github.com/amanahmad1607/ETA-Prediction

### Frontend

https://eta-prediction-ecru.vercel.app

### Backend

https://eta-backend-xl9d.onrender.com

### Swagger Documentation

https://eta-backend-xl9d.onrender.com/docs

---

<div align="center">

# ⭐ Thank You

If you found this project useful, please consider giving it a ⭐ on GitHub.

Made with ❤️ using FastAPI, React, TypeScript, LightGBM, Docker, Render, and Vercel.

</div>
