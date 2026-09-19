# Medical-Insurance-Prediction-

# 🏥 Medical Insurance Cost Predictor

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-Model-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge"/>
</p>

<p align="center">
  An interactive web application that predicts medical insurance charges based on personal health and demographic factors, powered by a trained Linear Regression model.
</p>

---

## 📌 Table of Contents

- [Overview](#overview)
- [Live Demo](#live-demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Model Details](#model-details)
- [Sample Prediction](#sample-prediction)
- [Key Learnings](#key-learnings)
- [Author](#author)

---

## 🔍 Overview

Medical insurance costs vary significantly across individuals based on age, lifestyle, and health factors. This project builds an end-to-end ML pipeline — from data preprocessing and model training to a fully deployed Streamlit web app — that estimates insurance charges for a given user profile.

This project demonstrates skills in:
- Supervised Machine Learning (Regression)
- Data preprocessing and feature encoding
- Model serialization with `pickle`
- Building and deploying interactive ML apps with Streamlit

---

## 🚀 Live Demo

> 🔗 **[Click here to try the app](#)** ← *(Replace with your Streamlit Cloud / Hugging Face Spaces link)*

![App Demo](assets/demo.gif) <!-- Add a screen recording GIF here -->

---

## ✨ Features

- 🎛️ **Interactive UI** — Clean two-column input form for fast data entry
- 🔢 **Real-time Prediction** — Instant cost estimate on button click
- 📊 **Contextual Metrics** — Displays Age, BMI, and Smoker status as metric cards
- ⚖️ **BMI Classifier** — Auto-classifies BMI into Underweight / Normal / Overweight / Obese
- ⚡ **Model Caching** — `@st.cache_resource` ensures fast repeated loads

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| ML Model | Scikit-learn (Linear Regression) |
| Web App | Streamlit |
| Data Handling | NumPy, Pandas |
| Model Persistence | Pickle |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```
medical-insurance-predictor/
│
├── app.py                        # Streamlit application
├── medical_insurance_model.pkl   # Trained Linear Regression model
├── insurance.csv                 # Dataset (source: Kaggle)
├── notebook.ipynb                # EDA + Model training notebook
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/medical-insurance-predictor.git
cd medical-insurance-predictor
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

### 📦 requirements.txt

```
streamlit
numpy
scikit-learn
```

---

## 🤖 Model Details

| Parameter | Details |
|---|---|
| Algorithm | Linear Regression |
| Dataset | [Medical Cost Personal Dataset — Kaggle](https://www.kaggle.com/datasets/mirichoi0218/insurance) |
| Training Samples | ~1,338 records |
| Target Variable | `charges` (USD) |

### Feature Encoding

| Feature | Encoding |
|---|---|
| Sex | `male = 0`, `female = 1` |
| Smoker | `yes = 0`, `no = 1` |
| Region | `southeast = 0`, `southwest = 1`, `northeast = 2`, `northwest = 3` |

### Input Features

| Feature | Type | Range |
|---|---|---|
| Age | Integer | 18 – 100 |
| Sex | Categorical | Male / Female |
| BMI | Float | 10.0 – 60.0 |
| Children | Integer | 0 – 10 |
| Smoker | Categorical | Yes / No |
| Region | Categorical | SE / SW / NE / NW |

---

## 🧪 Sample Prediction

| Input | Value |
|---|---|
| Age | 35 |
| Sex | Male |
| BMI | 27.5 |
| Children | 1 |
| Smoker | No |
| Region | Southeast |

> **Predicted Charge: ~$5,432.00** *(results may vary by model)*

---

## 💡 Key Learnings

- How to preprocess and encode categorical features for regression models
- Using `pickle` to serialize and reload trained ML models
- Building production-ready Streamlit apps with caching and form layouts
- Connecting model inference output to a clean, user-friendly UI


## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
