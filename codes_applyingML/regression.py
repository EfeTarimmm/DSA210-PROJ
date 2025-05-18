import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("second_Student_Depression_Dataset.csv")

# Transform 'Sleep Duration' into an ordinal numeric feature
sleep_map = {
    "Less than 5 hours": 1,
    "5-6 hours": 2,
    "7-8 hours": 3,
    "More than 8 hours": 4
}
df['Sleep_Ordinal'] = df['Sleep Duration'].map(sleep_map)

# Select numerical features to be used as predictors
features = ['Academic Pressure', 'Work Pressure', 'CGPA',
            'Study Satisfaction', 'Job Satisfaction',
            'Work/Study Hours', 'Financial Stress',
            'Sleep_Ordinal']  # newly transformed feature
target = 'Depression'

# Remove rows with missing values in the selected columns
df_model = df[features + [target]].dropna()

# Define independent variables (X) and dependent variable (y)
X = df_model[features]
y = df_model[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate model performance
print("Mean Squared Error (MSE):", mean_squared_error(y_test, y_pred))
print("R-squared (R²):", r2_score(y_test, y_pred))

# Visualize model coefficients
coefficients = pd.Series(model.coef_, index=features)
plt.figure(figsize=(10,6))
sns.barplot(x=coefficients.values, y=coefficients.index)
plt.title("Linear Regression Coefficients")
plt.xlabel("Coefficient Value")
plt.ylabel("Feature")
plt.tight_layout()
plt.show()