# 🩺 Lung Cancer Prediction

A Streamlit web application that predicts the presence of lung cancer based on patient symptoms indicators using a trained machine learning model.

---

## 🎯 Objective

Predict whether a patient has lung cancer based on features like smoking, anxiety, peer pressure, coughing, and more.

---

## 🔍 Dataset

- 📂 Source: [Kaggle - Lung Cancer Dataset](https://www.kaggle.com/datasets/nancyalaswad90/lung-cancer)
- 🧪 Type: Tabular, binary classification
- 🏷️ Target: `LUNG_CANCER` (0 = No, 1 = Yes)

---

## 📦 Technologies Used

- Pandas, NumPy
- Python 
- Scikit-learn
- Streamlit

---

## 🧠 How It Works

1. User inputs patient data using a web form
2. Streamlit sends features to the trained model (`lung_model.pkl`)
3. Model returns prediction: 0 = No Cancer, 1 = Lung Cancer
4. Output is shown in real-time with visual feedback

---

## 🖥 How to Run Locally

```bash
# Clone repo
git clone https://github.com/HarshaMotupalli/lung-cancer-predictor.git
cd lung-cancer-predictor

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
