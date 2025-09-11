# CarValuatorAI 🚗 - Predict car resale prices accurately

---


## 📌 Project Goal  
CarValuatorAI is a machine learning-powered web application that predicts the resale value of cars based on their features. The aim is to provide car buyers and sellers with a reliable estimate of resale prices, enabling fair and informed decisions in the automobile market.  

---

## 📖 Project Overview  
This project delivers an end-to-end machine learning pipeline for car price prediction:  
- Data preprocessing and cleaning for model-ready inputs.  
- Exploratory Data Analysis (EDA) to understand feature impact.  
- Building and tuning a CatBoost Regressor for high-accuracy predictions.  
- Deploying the trained model into a Streamlit application for interactive usage.

---

## 🔄 Project Workflow  

### 1. Data Preprocessing  
- Removed missing and irrelevant values.  
- Converted categorical variables (Fuel Type, Transmission, Seller Type) into dummy variables.  
- Derived car age (`no_year`) from year of manufacture.  
- Selected key features: `Present_Price`, `Kms_Driven`, `Owner`, `no_year`, `Fuel_Type`, `Seller_Type`, and `Transmission`.  

### 2. Model Building  
- Used **CatBoost Regressor** as the core model.  
- Applied **hyperparameter tuning** (iterations, depth, learning rate, etc.) to optimize performance.  
- Final trained model saved as `model.pkl` for deployment.  

### 3. Evaluation Metrics  
- **CatBoost Regressor Performance:**  
  - R² Score: **0.94**  
  - Mean Absolute Error (MAE): **0.44**  
  - Root Mean Squared Error (RMSE): **0.65**  
- The tuned CatBoost model provided excellent accuracy and generalization.  

### 4. Deployment  
- The trained CatBoost model was serialized using `pickle`.  
- A **Streamlit web app** (`app.py`) was built for user interaction.  
- The app allows users to enter details like car price, kilometers driven, ownership, fuel type, transmission, etc. and get instant resale price predictions.  
- Can be deployed on **Streamlit Cloud, Heroku, AWS, or other cloud platforms** for real-time usage.  

---

## 🛠 Tech Stack  
**Programming Language:**  
- Python  

**Libraries for Data Analysis & Visualization:**  
- Numpy  
- Pandas  
- Matplotlib  
- Seaborn  

**Machine Learning:**  
- CatBoost  
- Scikit-learn (for preprocessing and evaluation metrics)  

**Deployment & Utilities:**  
- Streamlit  
- Pickle  

---

## 📂 Project Structure  

CarValuatorAI/
├── dataset/
│   └── car_data.csv                        # Raw dataset used for training
├── .gitignore                              # Files/directories to exclude from Git tracking
├── Car_Price_Prediction.ipynb              # Notebook with EDA and model training
├── LICENSE                                 # Allows reuse, with attribution, no warranty
├── README.md                               # Project documentation
│-- app.py                                  # Streamlit app
│-- model.pkl                               # Trained CatBoost model
│-- requirements.txt                        # Required dependencies


---

## ✨ Features  
- Predict the **resale value of a car** using ML.  
- Simple and interactive **Streamlit UI** with sliders and dropdowns.  
- Powered by a **tuned CatBoost model** for high accuracy.  
- Provides results based on real-world dataset features.  

---

## 🚀 Future Enhancements  
- Add more features like **car brand, model, mileage, location**.  
- Deploy a **REST API** for integration with external systems.  
- Add **visual explanations (SHAP, feature importance plots)** for model transparency.  
- Deploy at scale on **AWS/GCP/Azure** with CI/CD pipelines.  

---

## 📌 How to Run Locally  

```
git clone https://github.com/AradhyaRay05/CarValuatorAI.git
cd CarValuatorAI
pip install -r requirements.txt
streamlit run app.py
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

<p>
  <a href="mailto:aradhyaray99@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="www.linkedin.com/in/rayaradhya"><img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="https://github.com/AradhyaRay05"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
</p>

---

Thanks for visiting ! Feel free to explore my other repositories and connect with me. 🚀
