# Insurance Premium Prediction ML Pipeline

An end-to-end Machine Learning project that predicts an individual's insurance premium category based on demographic, lifestyle, and financial attributes.

The project follows a production-oriented ML architecture with modular pipelines, centralized logging, exception handling, FastAPI backend, and Streamlit frontend.

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
- Production-ready folder structure

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Machine Learning | Scikit-Learn |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Backend | FastAPI |
| Frontend | Streamlit |
| Model Serialization | Pickle |
| Packaging | setuptools |

---

## Project Structure

```
insurance-premium-prediction-ml-pipeline
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
├── requirements.txt
├── setup.py
├── README.md
└── .gitignore
```

---

## Dataset Features

The model is trained using the following input features:

- Age
- Height
- Weight
- Annual Income
- Smoking Status
- City
- Occupation

### Target

Insurance Premium Category

---

## Installation

Clone the repository

```bash
git clone https://github.com/vviiishu/Insurance-Premium-Prediction-ML-Pipeline.git

cd Insurance-Premium-Prediction-ML-Pipeline
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Train the Model

Place the dataset inside

```
notebook/insurance.csv
```

Run

```bash
python -m src.pipeline.training_pipeline
```

Artifacts generated

```
artifacts/
├── raw.csv
├── train.csv
├── test.csv
└── model.pkl
```

---

## Run FastAPI Backend

```bash
uvicorn app:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Run Streamlit Frontend

```bash
streamlit run Frontend.py
```

---

## Prediction Pipeline

To perform predictions directly without running the API:

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
Model Serialization
   │
   ▼
Prediction Pipeline
   │
   ▼
FastAPI
   │
   ▼
Streamlit UI
```

---

## Future Improvements

- Model Monitoring
- MLflow Integration
- Unit Testing
- Kubernetes Deployment

---

## Author

**Vishal Kumar Puri**

Data Analyst | Machine Learning | Python | FastAPI | Streamlit | SQL | Power BI

LinkedIn:
https://www.linkedin.com/in/vishal-kumar-puri-846ba5288

GitHub:
https://github.com/vviiishu