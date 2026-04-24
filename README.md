# Inliefde Wine Predict System (SIS-3)

This project demonstrates a complete Machine Learning system for Wine Classification. It includes training, experiment tracking with MLflow, a FastAPI backend, and a Streamlit frontend, all orchestrated via Docker Compose.

## System Architecture

```text
User → Streamlit UI (Frontend)
        ↓
     FastAPI (Backend)
        ↓
     RandomForest Model
```
*(Training phase tracked fully via MLflow)*

## Project Structure

```text
├── app.py                 # Streamlit UI frontend
├── main.py                # FastAPI backend serving the model
├── train.py               # Script to train, track via MLflow, and save the model
├── requirements.txt       # Python dependencies
├── Dockerfile             # Container instructions for FastAPI
├── streamlit.Dockerfile   # Container instructions for Streamlit
├── docker-compose.yml     # Orchestration for API and UI services
└── README.md              # Project instructions
```

## Step 1: Train the Model & Track with MLflow

Before running the APIs, you must properly train the system so that `model.joblib` and the `mlruns` registry are populated natively. Run this locally:

```bash
pip install -r requirements.txt
python train.py
```
This script will:
1. Log metrics/parameters locally.
2. Dump `model.joblib`.
3. Register `Wine_RF_Model` to the MLflow Model Registry.

To view your tracking dashboard, launch MLflow locally:
```bash
mlflow ui
```
Navigate to `http://localhost:5000` to view the registry.

## Step 2: Spin Up the Stack via Docker

We use **Docker Compose** to run the frontend and backend simultaneously in isolated containers that communicate with each other.

```bash
docker-compose up --build -d
```
*(If you are on newer docker versions without docker-compose, use `docker compose up --build -d`)*

## Step 3: Test the Application

Navigate to your Streamlit frontend inside your browser:
- **UI Website:** [http://localhost:8501](http://localhost:8501)

You can view the raw API directly as well if needed:
- **API Root:** [http://localhost:8000/](http://localhost:8000/)
- **Swagger Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)
