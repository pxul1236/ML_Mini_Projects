---
# Black Friday Sales Prediction

This project aims to predict customer purchase amounts during the Black Friday sales event using historical sales data. We implemented multiple regression algorithms and explored their performance to select the best model for this task.

## 🎯 Problem Statement
Black Friday is one of the largest retail events, where millions of consumers make purchases. This project focuses on predicting the amount a customer is likely to spend based on various features such as demographics, product details, and past purchase history.

## 🔧 Tools and Libraries 
-Pandas: For data manipulation and analysis.
-NumPy: For numerical computations.
-Matplotlib & Seaborn: For data visualization.
-Scikit-learn: For machine learning algorithms and model evaluation.

## 📝 Approach
1. Exploratory Data Analysis (EDA)
We began by conducting a thorough EDA using Pandas, Matplotlib, and Seaborn to uncover patterns, outliers, and relationships between features. This step helped identify significant variables and gain insights into the dataset.

2. Data Preprocessing
Data preprocessing involved:     
                            -Handling missing values.
                            -Encoding categorical variables.
                            -Feature scaling to prepare the data for machine learning models.
                            -Splitting the dataset into features (X) and target (y).
3. Model Selection
Various regression algorithms were implemented, including:
 -Linear Regression: A simple, yet not highly effective approach on this complex dataset.
 -Decision Tree Regressor: Showed improvement but tended to overfit.
 -ExtraTrees Regressor: A stronger model based on decision trees, which showed notable improvement.
 -RandomForest Regressor: Provided the best results, handling the large dataset and complex feature interactions effectively.

4. Model Training and Optimization
The large dataset required a significant amount of computational power. To optimize training time, RandomForest was trained using n_jobs=-1, allowing the model to utilize all available CPU cores for parallel processing.

## 🚀 Conclusion
The RandomForest Regressor was the most effective model, outperforming others in terms of accuracy and error metrics. By utilizing n_jobs=-1, we were able to optimize training for the large dataset. This project highlights the importance of choosing the right model and computational resources when working with large datasets.

---

