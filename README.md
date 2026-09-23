# FDM Wildfire Prediction

A machine learning-based wildfire prediction system developed for the Fundamentals of Data Mining (FDM) group project.

## Project Idea

The system will use historical wildfire and environmental data to train machine learning models and predict wildfire-related outcomes for new/unseen data.

## Planned Workflow

Dataset  
↓  
Data Cleaning  
↓  
Preprocessing  
↓  
EDA  
↓  
Feature Engineering  
↓  
Train/Test Split  
↓  
Model Training  
↓  
Hyperparameter Tuning  
↓  
Model Evaluation  
↓  
Final Model  
↓  
FastAPI  
↓  
React Frontend  
↓  
MongoDB

## Technology Stack

### Frontend
- React
- TypeScript
- Vite
- Tailwind CSS
- Axios
- React Router
- Recharts
- React Hook Form
- Lucide React
- Oxlint

### Backend
- Python
- FastAPI
- Uvicorn
- Pydantic
- PyMongo

### Machine Learning
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn
- Joblib
- Matplotlib

### Database
- MongoDB Atlas

## Project Structure

```text
fdm-mini-project/
│
├── frontend/              # React frontend
│   └── src/
│       ├── components/    # Reusable UI components
│       ├── pages/         # Application pages
│       ├── services/      # API communication
│       ├── layouts/       # Page layouts
│       ├── hooks/         # React hooks
│       ├── types/         # TypeScript types
│       └── assets/        # Images/assets
│
├── backend/               # FastAPI backend
│   ├── app/
│   │   ├── api/           # API routes
│   │   ├── core/          # Configuration
│   │   ├── db/            # MongoDB connection
│   │   ├── schemas/       # Pydantic schemas
│   │   ├── services/      # Backend logic
│   │   ├── ml/            # Model prediction/loading
│   │   └── main.py        # FastAPI entry point
│   ├── tests/
│   ├── .env.example
│   ├── package.json
│   └── requirements.txt
│
├── ml/                    # Machine learning
│   ├── notebooks/         # Jupyter notebooks
│   ├── src/               # ML source code
│   └── artifacts/         # Trained models
│
├── data/
│   ├── raw/               # Original dataset
│   ├── processed/         # Cleaned dataset
│   └── README.md
│
├── docs/
│   ├── sow/               # Statement of Work
│   ├── diagrams/          # System diagrams
│   └── report/            # Final report
│
├── tests/                 # Project tests
├── .gitignore
└── README.md
```

## MongoDB

MongoDB Atlas is used for application data such as prediction history.

```text
DataNexus DS Team
└── FDM Wildfire Prediction
    └── FDM-Wildfire-Cluster
        └── wildfire_prediction
            └── predictions
```

The main wildfire training dataset will be kept in `data/` rather than stored entirely in MongoDB.

## Environment Setup

### Requirements

- Node.js
- npm
- Python 3.11+
- Git
- MongoDB Atlas

## Frontend

Open a terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend:

```text
http://localhost:5173
```

## Backend

Open a second terminal:

```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
npm start
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

Health checks:

```text
http://127.0.0.1:8000/api/health
http://127.0.0.1:8000/api/database-health
```

## Backend Environment

Create:

```text
backend/.env
```

Add:

```env
MONGODB_URI=your_mongodb_connection_string
MONGODB_DB=wildfire_prediction
FRONTEND_URL=http://localhost:5173
```

Never commit the real `.env` file.

## Run Full Project

### Terminal 1 — Frontend

```bash
cd frontend
npm run dev
```

### Terminal 2 — Backend

```powershell
cd backend
.venv\Scripts\Activate.ps1
npm start
```

## Architecture

```text
React Frontend
      ↓
FastAPI Backend
      ↓
Machine Learning Model
      ↓
Prediction
      ↓
MongoDB
```

## Development Stages

```text
1. Environment Setup
2. Dataset Selection
3. Dataset Understanding
4. Data Cleaning
5. Data Preprocessing
6. EDA
7. Feature Engineering
8. Model Training
9. Hyperparameter Tuning
10. Model Evaluation
11. Final Model
12. FastAPI Prediction API
13. React Prediction UI
14. MongoDB Prediction History
15. Testing
16. Documentation
```

## Git Workflow

Create a feature branch:

```bash
git checkout -b feature/your-feature-name
```

Commit:

```bash
git add .
git commit -m "feat: description"
```

Push:

```bash
git push origin feature/your-feature-name
```

Create a Pull Request to `main`.

## Security

Never commit:

```text
.env
MongoDB passwords
API keys
Secret keys
Large private datasets
```

## Current Status

- [x] GitHub repository
- [x] Project structure
- [x] React + Vite + TypeScript
- [x] Tailwind CSS
- [x] FastAPI
- [x] Uvicorn
- [x] MongoDB Atlas
- [x] FastAPI → MongoDB connection
- [x] Basic health endpoints
- [ ] Final dataset analysis
- [ ] Data preprocessing
- [ ] EDA
- [ ] Feature engineering
- [ ] ML model training
- [ ] Model evaluation
- [ ] Prediction API
- [ ] Prediction frontend
- [ ] Prediction history
- [ ] Final testing
- [ ] Final documentation

## Academic Project

This project is developed as part of the Fundamentals of Data Mining module and is intended for academic purposes.
