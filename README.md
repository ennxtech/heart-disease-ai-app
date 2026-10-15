# Group 14 – Heart Disease Prevention Using Artificial Intelligence

## Project Name: SereneHeart AI

### Project Overview

SereneHeart AI is our Group 14 machine learning project. We developed a website that uses patient information to classify whether heart disease is present or absent based on patterns learned from a heart disease dataset.

The aim of our project is to explore how artificial intelligence can be used to support heart health awareness.

### Dataset

We used the Cleveland Heart Disease dataset from the UCI Machine Learning Repository.

The dataset contains 303 patient records and 13 input features, including age, sex, chest pain type, blood pressure, cholesterol, maximum heart rate, and other clinical measurements.

We changed the original target into two classes:

- 0 – No heart disease recorded
- 1 – Heart disease recorded

### Machine Learning Models

We trained and compared four machine learning algorithms:

1. Logistic Regression
2. Random Forest
3. Gradient Boosting
4. Neural Network

We used cross-validation and hyperparameter tuning to compare their performance.

After evaluation, we selected **Logistic Regression** as our final model.

### Final Model Performance

Our selected Logistic Regression model achieved the following results on the test dataset:

| Metric | Result |
|---|---|
| Recall | 92.86% |
| F2 Score | 90.28% |
| MCC | 0.7451 |

The model correctly identified 26 out of 28 test records where heart disease was recorded.

### Our Website

We developed the application using Streamlit. The website includes a homepage, a heart disease assessment form, a model performance dashboard, and information about the project.

### How to Run the Application

```bash
git clone https://github.com/ennxtech/heart-disease-ai-app.git
cd heart-disease-ai-app
pip install -r requirements.txt
streamlit run app.py
```

### Project Files

- `app.py` – Streamlit website code
- `heart_disease_model.joblib` – Saved machine learning model
- `requirements.txt` – Required Python libraries
- `README.md` – Project information

### Project Limitations

Our dataset contains only 303 records, which limits how much the model can learn.

Although our project focuses on heart disease prevention, the current model classifies recorded heart disease. It does not predict whether a patient will develop heart disease in the future.

During Neural Network training, we also received a convergence warning because the model reached 1,000 iterations without fully converging.

Our selected Logistic Regression model also made some incorrect predictions, and we have not tested it using an independent hospital dataset.

### Conclusion

We successfully trained and compared different machine learning models and developed a Streamlit application using our selected Logistic Regression model.

Our project helped us understand data analysis, preprocessing, machine learning, model evaluation, and deployment.

SereneHeart AI is an educational project and should not be used as a medical diagnosis tool.# heart-disease-ai-app
