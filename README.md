🦴 Bone Mineral Density (BMD) Prediction using Machine Learning

An end-to-end Machine Learning project that predicts Bone Mineral Density (BMD) values using patient demographic and lifestyle attributes.
The project demonstrates the complete ML pipeline from data preprocessing to deployment.

🚀 Live Demo

Try the deployed ML application:

👉 HuggingFace Space:
https://huggingface.co/spaces/TharunNandula/BMD_Value

📌 Project Overview

Bone Mineral Density (BMD) is an important indicator used in diagnosing conditions like osteoporosis and assessing overall bone health.

This project builds multiple regression models to predict BMD values using patient health and lifestyle features.

The objective was to:

Build multiple ML models

Compare their performance

Apply hyperparameter tuning

Select the best model

Deploy the model as an interactive web application

📂 Project Structure
BMD-ML-Prediction
│
├── data
│   └── bmd_dataset.csv
│
├── src
│   └── bmd_ml.py
│
├── model
│   └── BMD_RG_value.pkl
│
├── app.py
│
├── requirements.txt
│
└── README.md
⚙️ Machine Learning Workflow

The project follows a structured ML pipeline:

1️⃣ Data Cleaning

Handling missing values

Removing duplicates

Exploratory data analysis

2️⃣ Data Splitting

Train-Test Split (80/20)

3️⃣ Data Preprocessing

StandardScaler for numerical features

OneHotEncoder for categorical features

ColumnTransformer for combined preprocessing

4️⃣ Model Building

Multiple regression models were trained:

KNN Regressor

Decision Tree Regressor

Linear Regression

Random Forest Regressor

AdaBoost Regressor

Gradient Boosting Regressor

XGBoost Regressor

Voting Regressor

Stacking Regressor

5️⃣ Model Evaluation

Models were evaluated using:

R² Score

RMSE (Root Mean Squared Error)

MSE (Mean Squared Error)

6️⃣ Hyperparameter Tuning

Used GridSearchCV to optimize model performance.

7️⃣ Best Model Selection

The best model was selected based on highest R² score and lowest RMSE.

8️⃣ Model Serialization

The final model was saved using Joblib:

BMD_RG.pkl


9️⃣ Deployment

The trained model is deployed using Streamlit and hosted on HuggingFace Spaces.

📊 Technologies Used

Python

Pandas

NumPy

Scikit-learn

XGBoost

Matplotlib

Seaborn

Streamlit

Joblib

📈 Example Model Results
Model	R² Score
KNN Regressor	Moderate
Decision Tree	Good
Random Forest	High
Gradient Boosting	High
Linear Regression	Best Performance
