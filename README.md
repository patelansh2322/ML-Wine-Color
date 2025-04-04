# ML-Wine-Color
Predicting wine color and flask deployment

This project classifies wines as either red or white based on their chemical properties. Using a combination of data preprocessing, machine learning models, and web deployment, the goal is to predict the color of wine based on various features.



Project Overview:

In this project, the dataset was preprocessed, feature selection and scaling were applied, and a Support Vector Classifier (SVC) was trained to predict wine color. The model was optimized and evaluated using multiple performance metrics. Finally, a Flask web application was deployed on AWS (Elastic Beanstalk) to make real-time predictions based on user input.



Features:

Preprocessing: Merged red and white wine datasets from UCI’s Wine Quality repository.

Data Imbalance Handling: Balanced the dataset using SMOTE (Synthetic Minority Over-sampling Technique).

Feature Correlation: Visualized feature correlations using a heatmap and removed highly negatively correlated features to improve model performance.

Scaling & Splitting: Scaled the features using StandardScaler and split the data into training and testing sets.

Model Training: Trained a Support Vector Classifier (SVC) with both Linear and Radial Basis Function (RBF) kernels.

Hyperparameter Tuning: Used GridSearchCV with cross-validation to optimize the model's hyperparameters (C, gamma, kernel).

Model Evaluation: Evaluated model performance using confusion matrix and classification report (precision, recall, and F1-score).

Deployment: Developed a Flask web application for real-time wine color prediction.



Technologies Used

Python for data processing and machine learning.

Pandas for data manipulation and preprocessing.

Seaborn and Matplotlib for data visualization.

Scikit-learn for machine learning (SVC, SMOTE, GridSearchCV, StandardScaler, etc.).

Flask for web application development.

Pickle for model and scaler serialization.


