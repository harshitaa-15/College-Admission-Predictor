<h1 align="center">🎓 College Admission Predictor</h1>

<p align="center">
  Predict your chances of getting into your dream college using Machine Learning 🚀
</p>

<p align="center">
  <img src="https://medicaldialogues.in/h-upload/2024/08/28/750x450_249902-admission.webp" width="1000"/>
</p>

## Project Overview :

- The College Admission Prediction System is a Machine Learning–based web application that predicts the probability of getting admission into a college based on student academic and personal details.
- This project helps students estimate their admission chances using important parameters such as entrance score, board percentage, stream preference, and extracurricular performance.
- The application is built using Machine Learning (Linear Regression) and deployed using Streamlit for an interactive user interface.


## Features :

- Predict college admission probability
- User-friendly web interface
- Real-time prediction
- Machine Learning based decision support
- Interactive input system

## Machine Learning Model :

- `Algorithm Used:` Linear Regression
- `Model File:` admission_prediction_model (1).pkl
- `Library Used:` joblib

The model predicts admission probability based on multiple student attributes.

## Input Parameters :

The prediction is based on the following inputs:

- Age
- Gender
- Category
- State
- Preferred Stream
- Entrance Exam
- Entrance Score
- Board Percentage
- Extracurricular Score

## Tech Stack :

| Technology       | Usage                |
| ---------------- | -------------------- |
| Python           | Programming Language |
| Streamlit        | Web Application      |
| NumPy            | Data Processing      |
| Joblib           | Model Loading        |
| Machine Learning | Prediction Model     |


## Project Structure :
```
📁 College-Admission-Prediction
│
├── app.py
├── admission_prediction_model (1).pkl
├── requirements.txt
├── admission.jpg
├── college.webp
└── README.md
```

## How It Works :

1. User enters academic and personal details.
2. Inputs are converted into numerical format.
3. Trained ML model processes the data.
4. System predicts admission probability.
5. Result is displayed with admission chances.
