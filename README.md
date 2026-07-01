# Insurance Premium Prediction ML Pipeline

An end-to-end Machine Learning project that predicts an individual's insurance premium category based on demographic, lifestyle, and financial attributes.

The project follows a production-oriented ML architecture with modular pipelines, centralized logging, exception handling, FastAPI backend, Streamlit frontend, and Docker support.

---

## Features

- End-to-End ML Pipeline
- Modular project architecture
- Automated data ingestion
- Data preprocessing and feature engineering
- Model training and serialization
- Prediction pipeline
- FastAPI REST API
- Streamlit Web Application
- Centralized logging
- Custom exception handling
- Docker containerization
- GitHub Codespaces support
- Production-ready folder structure

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python 3.10 |
| Machine Learning | Scikit-Learn |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Backend | FastAPI, Uvicorn |
| Frontend | Streamlit |
| Model Serialization | Pickle |
| Containerization | Docker, Docker Compose |
| Dev Environment | GitHub Codespaces |
| Packaging | setuptools |

---

## Project Structure

```
Insurance-Premium-Prediction-ML-Pipeline/
│
├── .devcontainer/
│   └── devcontainer.json          # GitHub Codespaces configuration
│
├── artifacts/
│   ├── raw.csv
│   ├── train.csv
│   ├── test.csv
│   └── model.pkl
│
├── notebook/
│   ├── insurance.csv
│   └── FE_EDA_and_Model_Training.ipynb
│
├── logs/
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── training_pipeline.py
│   │   └── prediction_pipeline.py
│   │
│   ├── logger.py
│   ├── exception.py
│   └── utils.py
│
├── app.py
├── Frontend.py
├── Dockerfile                     # FastAPI backend image
├── Dockerfile.frontend            # Streamlit frontend image
├── docker-compose.yml             # Orchestrates both services
├── requirements.txt
├── setup.py
├── README.md
└── .gitignore
```

---

## Dataset Features

The model is trained using the following input features:

| Feature | Description |
|---------|-------------|
| Age | Age of the individual |
| Height | Height in metres |
| Weight | Weight in kilograms |
| Annual Income | Income in LPA |
| Smoking Status | Whether the individual smokes |
| City | City of residence |
| Occupation | Type of employment |

### Target

Insurance Premium Category (`Low`, `Medium`, `High`)

---

## Option A — Run Locally

### Installation

```bash
git clone https://github.com/vviiishu/Insurance-Premium-Prediction-ML-Pipeline.git
cd Insurance-Premium-Prediction-ML-Pipeline
pip install -r requirements.txt
```

### Train the Model

Place the dataset at `notebook/insurance.csv`, then run:

```bash
python -m src.pipeline.training_pipeline
```

Artifacts generated:

```
artifacts/
├── raw.csv
├── train.csv
├── test.csv
└── model.pkl
```

### Run FastAPI Backend

```bash
uvicorn app:app --reload
```

| | URL |
|--|-----|
| Backend | http://127.0.0.1:8000 |
| Swagger Docs | http://127.0.0.1:8000/docs |

### Run Streamlit Frontend

Open a second terminal:

```bash
streamlit run Frontend.py
```

Frontend available at `http://localhost:8501`

---

## Option B — Run with Docker

### Prerequisites

- Docker installed
- Docker Compose installed

### Steps

**1. Train the model first (only needed once)**

```bash
pip install -r requirements.txt
python -m src.pipeline.training_pipeline
```

**2. Build and start both containers**

```bash
docker-compose up --build
```

**3. Access the apps**

| Service | URL |
|---------|-----|
| Streamlit Frontend | http://localhost:8501 |
| FastAPI Backend | http://localhost:8000 |
| Swagger Docs | http://localhost:8000/docs |

**4. Stop the containers**

```bash
docker-compose down
```

### Docker Architecture

```
docker-compose
├── backend  (Dockerfile)           → FastAPI on port 8000
└── frontend (Dockerfile.frontend)  → Streamlit on port 8501
```

The frontend container communicates with the backend using the internal Docker network service name `http://backend:8000` — no manual IP configuration needed.

---

## Option C — Run on GitHub Codespaces

This repo includes a `.devcontainer/devcontainer.json` configuration that sets up the full environment automatically in GitHub Codespaces with Python 3.10 and Docker pre-installed.

### Steps

**1. Open in Codespaces**

Go to the GitHub repo → click the green **Code** button → **Codespaces** tab → **Create codespace on main**

**2. Wait for setup to complete**

Codespaces will automatically:
- Install Python 3.10
- Install Docker
- Run `pip install -r requirements.txt`

**3. Train the model**

```bash
python -m src.pipeline.training_pipeline
```

**4. Run with Docker Compose**

```bash
docker-compose up --build
```

**5. Access the apps**

Go to the **Ports** tab at the bottom of VS Code in the browser:

| Port | Service |
|------|---------|
| 8000 | FastAPI — click globe icon to open Swagger docs |
| 8501 | Streamlit — click globe icon to open the app |

Codespaces provides public HTTPS URLs for each forwarded port automatically.

---

## Prediction Pipeline (without API)

To run predictions directly:

```bash
python -m src.pipeline.prediction_pipeline
```

---

## Workflow

```
Dataset
   │
   ▼
Data Ingestion
   │
   ▼
Train-Test Split
   │
   ▼
Data Transformation
   │
   ▼
Feature Engineering
   │
   ▼
Model Training
   │
   ▼
Model Serialization  →  artifacts/model.pkl
   │
   ▼
Prediction Pipeline
   │
   ├──▶  FastAPI (app.py)
   │         │
   │         ▼
   └──▶  Streamlit (Frontend.py)
```

---

## API Reference

### POST `/predict`

Predicts the insurance premium category for a given user.

**Request Body**

```json
{
  "age": 30,
  "weight": 65.0,
  "height": 1.70,
  "income_lpa": 10.0,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

**Response**

```json
{
  "predicted_category": "Low"
}
```

**Occupation values:** `retired`, `freelancer`, `student`, `government_job`, `business_owner`, `unemployed`, `private_job`

---

## Future Improvements

- Model Monitoring
- MLflow Integration
- Unit Testing
- CI/CD with GitHub Actions
- Kubernetes Deployment
- Model versioning

---

## Author

**Vishal Kumar Puri**

Data Analyst | Machine Learning | Python | FastAPI | Streamlit | SQL | Power BI

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/vishal-kumar-puri-846ba5288)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/vviiishu)