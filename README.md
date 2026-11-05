# InsurePredict

<p align="center">
  <strong>Machine learning-powered health insurance charge estimator</strong>
</p>

<p align="center">
  <a href="https://insurepredict-oi6h.onrender.com/"><img src="https://img.shields.io/badge/Live_Demo-Open_InsurePredict-245B47?style=for-the-badge" alt="Live demo"></a>
  <a href="https://github.com/Ritik-Singh7/InsurePredict"><img src="https://img.shields.io/badge/GitHub-Source_Code-181717?style=for-the-badge&logo=github" alt="GitHub repository"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Backend-000000?logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/Scikit--learn-Machine_Learning-F7931E?logo=scikitlearn&logoColor=white" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-E34F26" alt="Frontend">
  <img src="https://img.shields.io/badge/Deployment-Render-46E3B7?logo=render" alt="Render">
</p>

---

## 🌐 Live Demo

**Try the application:** [https://insurepredict-oi6h.onrender.com/](https://insurepredict-oi6h.onrender.com/)

InsurePredict is deployed on Render. Enter a few profile details and submit the form to receive an estimated yearly medical insurance charge.

> Depending on the hosting instance state, the first request may take a little longer to respond.

## 📸 Application Screenshot

![InsurePredict application showing the profile form and estimate panel](screenshots/insurepredict.jpg)

*The application has one main prediction screen, with profile inputs on the left and the estimate panel on the right.*

## 📌 Project Overview

InsurePredict is a machine learning web application that estimates individual medical insurance charges using demographic and lifestyle-related information.

The user enters age, gender, Body Mass Index (BMI), number of children, smoking status, and residential region. The frontend sends these values to a Flask endpoint. The backend validates the input, scales the numerical features, constructs the feature vector expected by the trained model, and returns a prediction.

## ✨ Features

- **Insurance charge estimation** from six user-provided profile features.
- **Gradient Boosting model** loaded from a serialized model bundle.
- **Input validation** for numeric values and categorical fields.
- **Consistent preprocessing** using the saved scaler during inference.
- **Flask JSON API** exposed through the `/predict` endpoint.
- **Interactive web interface** built with HTML, CSS, and JavaScript.
- **User feedback** for loading, successful estimates, and API errors.
- **Live deployment** on Render.

## 🧰 Tech Stack

| Area | Tools |
|---|---|
| Programming language | Python |
| Data manipulation | Pandas |
| Machine learning | Scikit-learn |
| Model persistence | Joblib |
| Backend and API | Flask, Flask-CORS |
| Frontend | HTML, CSS, JavaScript |
| Dataset | `insurance.csv` |
| Notebook | Jupyter Notebook |
| Deployment | Render |
| Version control | Git, GitHub |

## 🧠 Model Information

The backend loads the trained model bundle from `backend/insurance_model.pkl`. The bundle contains the estimator, the fitted numerical scaler, and the feature-column order required for inference.

The application identifies the deployed estimator as **Gradient Boosting** and displays an **R² score of 89.90%**.

| Model detail | Value |
|---|---:|
| Estimator | Gradient Boosting |
| R² score displayed in the application | 89.90% |

The R² score describes model fit on an evaluation dataset. It does not mean that every individual prediction is guaranteed to be accurate by 89.90%.

## 📊 Prediction Inputs

| Input | Description | Accepted values |
|---|---|---|
| Age | Age of the individual | 18–100 |
| Gender | Gender category | `male`, `female` |
| BMI | Body Mass Index | 10–80 (backend validation) |
| Children | Number of dependent children | 0–20 (backend validation) |
| Smoking status | Whether the individual smokes | `yes`, `no` |
| Region | Residential region | `northeast`, `northwest`, `southeast`, `southwest` |

**Target variable:** `charges` — medical insurance charges.

## 🔄 How It Works

1. The user fills in the profile form in the browser.
2. JavaScript sends the values as a JSON `POST` request to `/predict`.
3. Flask validates the submitted values.
4. The backend scales the numerical inputs and builds the feature vector in the order expected by the model.
5. The trained Gradient Boosting model predicts the insurance charge.
6. Flask returns the prediction as JSON, and the frontend formats it as a currency amount.

## 📁 Repository Structure

```text
InsurePredict/
├── backend/
│   ├── app.py
│   ├── insurance_model.pkl
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── screenshots/
│   └── insurepredict.jpg
├── insurance.csv
├── project01.ipynb
└── README.md
```

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Ritik-Singh7/InsurePredict.git
cd InsurePredict
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r backend/requirements.txt
```

The backend requirements include Flask, Flask-CORS, Pandas, Scikit-learn, Joblib, and Gunicorn.

### 4. Start the application

Run this command from the repository root:

```bash
python backend/app.py
```

Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser. Flask serves the frontend and prediction endpoint from the same application.

## 🔌 API Reference

### Predict insurance charges

| Property | Value |
|---|---|
| Endpoint | `/predict` |
| HTTP method | `POST` |
| Request content type | `application/json` |

**Example request**

```json
{
  "age": 34,
  "sex": "male",
  "bmi": 24,
  "children": 1,
  "smoker": "no",
  "region": "southeast"
}
```

**Example success response**

```json
{
  "prediction": 6610.68
}
```

*The response above is an illustrative example based on the supplied screenshot. Actual predictions depend on the model and submitted values.*

**Example validation error**

```json
{
  "error": "Age must be between 18 and 100"
}
```

The API returns HTTP 400 for invalid input and HTTP 500 if an unexpected prediction error occurs.

## 🧪 Dataset and Notebook

- `insurance.csv` — dataset used for the project.
- `project01.ipynb` — Jupyter Notebook containing the project analysis and experimentation.

## 🚀 Deployment

The application is hosted on **Render**:

[Open InsurePredict](https://insurepredict-oi6h.onrender.com/)

The Flask application reads the deployment-provided `PORT` environment variable and binds to `0.0.0.0` for hosting.

## ⚠️ Disclaimer

InsurePredict is an educational machine learning project. Its outputs are statistical estimates only. They are not official insurance quotes, underwriting decisions, medical advice, or financial advice.

## 👨‍💻 Author

**Ritik Singh** — B.Tech Computer Science Engineering Student

- GitHub: [Ritik-Singh7](https://github.com/Ritik-Singh7)
- LinkedIn: [Ritik Singh](https://www.linkedin.com/in/ritik-singh-a8ba0233a/)

---

<p align="center">Built with Python, Flask, and Scikit-learn.</p>
