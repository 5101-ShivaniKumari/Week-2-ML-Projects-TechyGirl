# Week 2 ML Projects - TechyGirl

## 📌 Project Title
Week 2 Machine Learning Assignment – Linear Regression & Classification

## 🎯 Objective
This repo has the work our group did for the Week 2 ML assignment. The main idea was to actually understand how regression and classification models work instead of just calling a library function — so we built Linear Regression completely from scratch using NumPy, and then used a real dataset to build a classification model. Along the way we also learned about evaluation metrics, how to pick the right algorithm, and how to actually use GitHub as a team instead of just emailing files to each other.

## 📊 Dataset
- **Linear Regression:** We generated our own small dataset using NumPy — Hours Studied vs Marks Scored, with a bit of random noise added so it isn't a perfectly straight line (more realistic that way).
- **Classification Model:** We used the **Pima Indians Diabetes Dataset** (originally from the UCI Machine Learning Repository). It has features like **Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, Age** and we're predicting **whether the patient has diabetes (Outcome: 0 = No, 1 = Yes)**. We trained a Logistic Regression model on this, since it's a binary classification problem, and got an accuracy of about 74.68%.

## 🛠️ Technologies Used
- Python 3
- NumPy (for the regression model)
- Matplotlib (for the graphs)
- Pandas (for handling the classification dataset)
- Scikit-learn (only for the classification part — not used anywhere in the regression task, as per the rules)
- Jupyter Notebook / VS Code

## 👥 Team Members
| Name | Task Assigned |
|------|----------------|
| Anshika Kumawat | Task 1 — Model Evaluation Challenge |
| Shivani Kumari | Task 2 — Linear Regression from Scratch |
| Samridhi Kumari | Task 3 — Classification Sprint |
| Khushi Rani | Task 4 & 5 — Model Selection Strategy + Explainable AI |

*(Group: TechyGirl, MCA 2nd Year)*

## 📷 Screenshots
Add screenshots after running the code, for example:

![Linear Regression Output](screenshots/linear_regression_output.png)
![Classification Accuracy](screenshots/classification_accuracy.png)

## 🚀 How to Run the Project

First install the libraries you'll need:
```bash
pip install numpy matplotlib pandas scikit-learn
```

**To run the Linear Regression model:**
```bash
cd linear-regression
python3 linear_regression_scratch.py
```

**To run the Classification model:**
```bash
cd classification-model
python3 classification_model.py
```

## 📁 Folder Structure
```
Week2-ML-Projects-TechyGirl/
│
├── linear-regression/
│   └── linear_regression_scratch.py
│
├── classification-model/
│   ├── classification_model.py
│   └── dataset.csv
│
├── screenshots/
│   ├── linear_regression_output.png
│   └── classification_accuracy.png
│
└── README.md
```

## 🙌 What We Learned
This assignment helped us see that accuracy alone doesn't tell the full story when judging a model, how linear regression actually works behind the scenes instead of just being a one-liner in sklearn, and most importantly — how to split work, push code, and stay on the same page as a team using Git and GitHub.
