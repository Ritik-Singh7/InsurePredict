import os
from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = (BASE_DIR / "../frontend").resolve()
MODEL_PATH = BASE_DIR / "insurance_model.pkl"

app = Flask(
    __name__,
    static_folder=str(FRONTEND_DIR),
    static_url_path=""
)

CORS(app)

bundle = joblib.load(MODEL_PATH)

model = bundle["model"]
scaler = bundle["scaler"]
feature_columns = bundle["feature_columns"]


@app.route("/")
def home():
    return send_from_directory(str(FRONTEND_DIR), "index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({"error": "A valid JSON object is required"}), 400

        age = float(data["age"])
        sex = str(data["sex"]).lower()
        bmi = float(data["bmi"])
        children = int(data["children"])
        smoker = str(data["smoker"]).lower()
        region = str(data["region"]).lower()

        if not all(map(lambda x: __import__("math").isfinite(x),
                       [age, bmi, children])):
            return jsonify({"error": "Values must be finite numbers"}), 400

        if not 18 <= age <= 100:
            return jsonify({"error": "Age must be between 18 and 100"}), 400

        if not 10 <= bmi <= 80:
            return jsonify({"error": "Please enter a valid BMI"}), 400

        if children < 0 or children > 20:
            return jsonify({"error": "Children must be between 0 and 20"}), 400

        if sex not in ["male", "female"]:
            return jsonify({"error": "Invalid sex value"}), 400

        if smoker not in ["yes", "no"]:
            return jsonify({"error": "Invalid smoker value"}), 400

        if region not in [
            "northeast", "northwest", "southeast", "southwest"
        ]:
            return jsonify({"error": "Invalid region value"}), 400

        numerical_data = pd.DataFrame(
            [[age, bmi, children]],
            columns=["age", "bmi", "children"]
        )

        scaled_values = scaler.transform(numerical_data)[0]

        input_data = {column: 0 for column in feature_columns}

        input_data["age"] = scaled_values[0]
        input_data["bmi"] = scaled_values[1]
        input_data["children"] = scaled_values[2]

        input_data["sex"] = 1 if sex == "male" else 0
        input_data["smoker"] = 1 if smoker == "yes" else 0

        if region != "northeast":
            input_data[f"region_{region}"] = 1

        input_df = pd.DataFrame(
            [input_data],
            columns=feature_columns
        )

        prediction = model.predict(input_df)[0]

        return jsonify({"prediction": round(float(prediction), 2)})

    except (KeyError, TypeError, ValueError, OverflowError) as error:
        return jsonify({"error": f"Invalid input: {error}"}), 400

    except Exception:
        app.logger.exception("Prediction failed")
        return jsonify({"error": "Prediction failed. Check backend logs."}), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
