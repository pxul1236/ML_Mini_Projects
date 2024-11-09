# Ad Click Prediction
This project uses a logistic regression model to predict whether a user will click on an advertisement based on various features. The dataset contains information on user demographics, ad interaction history, and other relevant details. Logistic regression was chosen as the initial model to explore the relationship between the input features and the likelihood of clicking an ad.

## Overview
This project aims to predict ad clicks based on user features, allowing businesses to target potential customers more effectively. The logistic regression algorithm is utilized due to its simplicity, interpretability, and efficiency for binary classification tasks like this one.

## Dataset
The dataset contains features related to user demographics and online behavior, including:

- Age: Age of the user
- Daily Time Spent on Site: Average time spent on the website per day (in minutes)
- Area Income: Average income of the user’s area of residence
- Daily Internet Usage: Average daily time spent on the internet (in minutes)
- Ad Topic Line: Text content related to the ad
- City and Country: Location information of the user
- Timestamp: Date and time of the ad click
- Clicked on Ad: Binary target variable indicating whether the ad was clicked (1 if clicked, 0 if not)
### Model Used
Logistic Regression: Logistic regression is a linear model used for binary classification. It models the probability of the target variable (ad click) based on the linear combination of the input features. It’s a suitable starting point due to its interpretability and quick training process.
### Results
The logistic regression model demonstrated moderate accuracy in predicting ad clicks. Given its simplicity, it serves as a benchmark for potential future models that might incorporate more complex algorithms.