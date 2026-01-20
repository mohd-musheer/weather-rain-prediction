# 🌦 Rainfall Prediction using XGBoost

A machine learning–powered web application that predicts whether it will **rain tomorrow** based on historical weather conditions.  
The model is built using **XGBoost** and achieves approximately **86% accuracy** on a large, cleaned Australian weather dataset.

---

live : https://weather-rain-prediction.onrender.com

docker : 

## 🚀 Features

- 🌧 Predicts **Rain / No Rain** for the next day
- ⚡ Powered by **XGBoost Classifier**
- 🧹 Trained on a **cleaned & leakage-free dataset** (~500K rows)
- 🎨 Modern, interactive UI with dynamic background changes
- ⏳ Loading indicator during prediction
- 🎯 Demo data button for quick testing
- 🔗 FastAPI backend (REST API)
- 📦 Model published & reusable

---

## 🧠 Machine Learning Model

- **Algorithm:** XGBoost (Extreme Gradient Boosting)
- **Problem Type:** Binary Classification
- **Target Variable:** `RainTomorrow`  
  - `1` → Rain  
  - `0` → No Rain
- **Accuracy:** ~**86%** on unseen test data
- **Key Features Used:**
  - Temperature (Min/Max/9AM/3PM)
  - Humidity (9AM/3PM)
  - Pressure (9AM/3PM)
  - Wind speed & direction
  - Cloud cover
  - Location
  - Temporal features (Day, Month)

> ⚠️ Data leakage columns (e.g. `RISK_MM`) were removed to ensure realistic performance.

---

## 🖥️ Web Interface

The UI allows users to:
- Select categorical values (Location, Wind Direction, RainToday)
- Enter numerical weather parameters
- Instantly view predictions with **animated background changes**
- Use a **Demo** button for quick input

---

## 🧩 Tech Stack
Metric,Value
Algorithm,XGBoost Classifier
Dataset Size,"50,000 Rows"
Accuracy Score,86%
Target Variable,RainTomorrow (Binary: Rain/No Rain)

---

## 📂 Project Structure

├── api.py # FastAPI backend
├── weather_predict.pkl # Trained XGBoost model
├── index.html # Frontend UI
├── README.md # Project documentation

yaml
Copy code

---

## ▶️ How to Run Locally

### 1️⃣ Install dependencies
```bash
pip install fastapi uvicorn pandas scikit-learn xgboost joblib
2️⃣ Start the API server
bash
Copy code
uvicorn api:app --reload
3️⃣ Open the UI
Open index.html in your browser
OR

Serve it using FastAPI static files

🔌 API Usage
Endpoint
bash
Copy code
POST /predict
Sample JSON Input
json
Copy code
{
  "Location": "Cairns",
  "MinTemp": 13.7,
  "MaxTemp": 27.6,
  "Humidity9am": 69,
  "Humidity3pm": 53,
  "Pressure9am": 1017.8,
  "Pressure3pm": 1013.5,
  "RainToday": "No",
  "Day": 4,
  "Month": 8
}
Sample Response
json
Copy code
{
  "result": "Rain"
}
📊 Model Performance
Metric	Value
Accuracy	~86%
Overfitting	No
Data Leakage	Removed
Generalization	Good

🔮 Future Improvements
Show rainfall probability (%)

Add real-time weather API integration

Improve rain-class recall with imbalance handling

Deploy to cloud (Render / Railway / AWS)

Mobile-first UI enhancements

👤 Author
Mohd Musheer
Machine Learning & Backend Developer

⭐ Acknowledgements
Australian Weather Dataset

Kaggle community

XGBoost documentation

If you find this project useful, feel free to ⭐ star the repository!

yaml
Copy code

---

## 🏆 Why this README is strong

✔ Clear problem statement  
✔ Mentions **XGBoost explicitly**  
✔ Honest accuracy (86%)  
✔ Explains data leakage handling  
✔ Recruiter-friendly  
✔ GitHub-optimized  

If you want next:
- Add **badges** (Python, XGBoost, FastAPI)
- Short **project demo GIF**
- Docker instructions
- Cloud deployment guide

Just say 👍