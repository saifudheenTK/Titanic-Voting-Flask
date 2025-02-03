# 🚢 Titanic Survival Predictor  

A machine learning-powered web application that predicts Titanic survivors using an **ensemble Voting Classifier** and is deployed via **Flask**. The dataset is preprocessed, and multiple machine learning models (e.g., **Logistic Regression, Random Forest, and SVM**) are combined to improve accuracy.  

## 📌 Features  
✅ Uses an **ensemble Voting Classifier** for better prediction accuracy  

✅ Combines **Logistic Regression, Random Forest, and SVM** models  

✅ **Flask-based web app** for real-time predictions  

✅ **Preprocessed Titanic dataset** for better model performance  

✅ Simple web interface for user input  

## 🛠 Tech Stack  
- **Python**  
- **Flask** (for deployment)  
- **Scikit-learn** (for ML models)  
- **Pandas & NumPy** (for data preprocessing)  
- **Pickle** (for model storage)  

## 📂 Project Structure 
📦 Titanic-Survival-Predictor

├── model.pkl # Trained Voting Classifier model

├── model_training.ipynb # Jupyter Notebook for model training

├── passenger_survival_dataset # Titanic dataset used for training

├── requirements.txt # Dependencies

├── app.py # Flask application

└── README.md # Project documentation



## 🔧 Installation & Setup  
1️⃣ **Clone the repository**  

git clone https://github.com/saifudheenTK/Titanic-Survival-Predictor.git

2️⃣ Navigate to the project directory


cd Titanic-Survival-Predictor
3️⃣ Install dependencies


pip install -r requirements.txt

4️⃣ Run the Flask app

python app.py

5️⃣ Open the web app

Go to http://127.0.0.1:5000/ in your browser.

🎯 Usage

Enter passenger details (Age, Gender, Class, Seat Type, Fare Paid, etc.).
Click Predict to get survival probability.
The app will display whether the passenger survived or not.


🚀 Future Improvements

Improve model accuracy with advanced feature engineering
Deploy the app online using Heroku or Render
Enhance UI/UX with a better web interface
Made with ❤️ by SaifudheenTK
