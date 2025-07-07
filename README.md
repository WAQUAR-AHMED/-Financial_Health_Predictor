# 💰 Financial Health Predictor

An AI-powered Streamlit web app that predicts your financial health based on your income, spending, and savings. It uses a machine learning model to classify your financial status as **Healthy**, **Moderate**, or **Poor**, and gives personalized budgeting advice.

---

## 🚀 Demo

Try the live app on [Hugging Face Spaces](https://huggingface.co/spaces/waquarahmed/Financial_Health_Predictor)  


---

## 📊 Features

- Input monthly **income**, **essential spending**, **discretionary spending**, and **savings**
- Predicts your **financial health status**
- Gives actionable financial advice based on ML prediction
- Built using **Streamlit** and **scikit-learn**
- Lightweight and easy to deploy

---

## 🧠 Model Info

- Algorithm: `RandomForestClassifier`
- Trained on: Synthetic dummy financial dataset
- Target classes: `Healthy`, `Moderate`, `Poor`
- Encoded using `LabelEncoder`

---

## Model Performance

![image](https://github.com/user-attachments/assets/fed38b5a-1bc7-4784-b914-ba998b285973)

![image](https://github.com/user-attachments/assets/6f7f8f5e-da49-4eac-a2b9-e722473a839f)

---

## 🖥️ Tech Stack

- Python 🐍
- Streamlit 📊
- scikit-learn 🤖
- pandas, joblib

---

## 🛠️ Installation

1. Clone the repo:

git clone https://github.com/WAQUAR-AHMED/-Financial_Health_Predictor.git cd finance-health-predictor

2. Install dependencies:

  pip install -r requirements.txt

3. Run the app:

  streamlit run app.py

---

## 📁 File Structure

├── app.py # Streamlit web app

├── model.pkl # Trained ML model

├── label_encoder.pkl # Encoded target labels

├── dummy_financial_data.csv # Sample dataset (optional)

├── requirements.txt # Python dependencies

└── README.md # This file

---

## 📦 Deploying to Hugging Face Spaces

1. Create a new Space using the `Streamlit` SDK  
2. Upload all the above files  
3. Hugging Face will automatically build and run your app

---

## 🤝 Contributing

Contributions, feedback, and ideas are welcome!  
Feel free to fork this repo and open pull requests.

---

## 📄 License

MIT License – Use freely, but give credit 🙌

---

## 🙋‍♂️ Author

**Waquar Ahmed**  
Connect on [LinkedIn](https://www.linkedin.com/in/waquarahmed)

