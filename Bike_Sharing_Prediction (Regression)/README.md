# Bike Share Demand Regression Project

## Project Overview
This project aims to predict bike share demand using regression models based on various features, including weather conditions, time, and user demographics. The dataset contains historical bike share data, and the goal is to forecast the number of bike rentals.

## Dataset
The dataset used in this project is sourced from UCI Machine Learning Repository. It includes the following features:
- **Datetime**: Timestamp of the bike rental
- **Season**: Season of the year (spring, summer, autumn, winter)
- **Year**: Year of the rental
- **Month**: Month of the rental
- **Weekday**: Day of the week
- **Holiday**: Whether the day is a holiday
- **Working Day**: Whether the day is a working day
- **Weather**: Weather conditions (clear, cloudy, rainy, etc.)
- **Temp**: Normalized temperature in Celsius
- **Humidity**: Normalized humidity
- **Wind Speed**: Normalized wind speed
- **Casual**: Count of casual riders
- **Registered**: Count of registered riders
- **Count**: Total count of bike rentals (target variable)

## 🔧 Tools and Libraries 
-Pandas: For data manipulation and analysis.
-NumPy: For numerical computations.
-Matplotlib & Seaborn: For data visualization.
-Scikit-learn: For machine learning algorithms and model evaluation.


## Models Implemented
The following regression models were implemented to predict bike share demand:
1. **Linear Regression**
2. **Lasso Regression**
3. **Ridge Regression**
4. **Elastic Net Regression**
5. **Huber Regressor**
6. **Decision Tree Regressor**
7. **Random Forest Regressor**
8. **Extra Trees Regressor**
9. **Gradient Boosting Regressor**

### Model Performance
The models were evaluated using cross-validation and mean squared error (MSE) as the performance metrics. After removing the 'casual' feature due to its high correlation with the target variable, the following results were obtained:

| Model                      | CV Score         | MSE                |
|---------------------------|------------------|--------------------|
| Linear Regression          | 1168.16          | 1181.14            |
| Lasso Regression           | 1228.51          | 1231.07            |
| Ridge Regression           | 1168.17          | 1180.97            |
| Elastic Net Regression     | 1795.03          | 1796.22            |
| Huber Regressor           | 1467.20          | 1475.20            |
| Decision Tree Regressor    | 581.35           | 571.47             |
| Random Forest Regressor    | 305.94           | 313.98             |
| Extra Trees Regressor      | 297.82           | 297.27             |
| Gradient Boosting Regressor | 365.17           | 382.35             |

## Future Work
-Hyperparameter Tuning: Further optimize model performance by tuning hyperparameters using techniques such as Grid Search or Random Search.
-Feature Engineering: Explore additional features that could improve model accuracy, such as time-based features (hour of the day) or geographical data.