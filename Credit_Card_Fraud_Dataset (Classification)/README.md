# Credit Card Fraud Detection
This project focuses on classifying fraudulent credit card transactions using machine learning techniques.

# Dataset
The dataset for this project is available on Kaggle: Credit Card Fraud Detection Dataset :
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

# Project Overview

Objective: Detect fraudulent transactions from highly imbalanced data.

## Steps and Methodology
- **Data Exploration**: Analyzed feature distributions and target class imbalance.
- **Data Preprocessing**: Verified no missing values; scaled features for model training.
- **Model Training**: Developed a custom training function for Logistic Regression, Random Forest, and XGBoost Classifier.
- **Imbalance Handling**: Did not use SMOTE (Synthetic Minority Over-sampling Technique), though it could address class imbalance.
## Models Used
- **Logistic Regression**
- **Random Forest**
- **XGBoost Classifier**
### Results
Model performance was evaluated primarily using the F1 Score due to the imbalanced nature of the dataset.

### Technologies
- Python
- scikit-learn
- XGBoost
- pandas 
- matplotlib / seaborn
