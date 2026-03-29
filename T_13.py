# Import pandas library for handling datasets (CSV, tables, etc.)
import pandas

# Import linear regression model from sklearn (machine learning library)
from sklearn import linear_model

# Read the CSV file into a DataFrame (like a table in memory)
df = pandas.read_csv("T_13.csv")

# Select input features (independent variables)
# These are the columns the model will use to make predictions
X = df[['Weight', 'Volume']]

# Select target variable (dependent variable)
# This is what we are trying to predict
y = df['CO2']

# Create a Linear Regression model object
regr = linear_model.LinearRegression()

# Train the model using the data
# The model learns the relationship between X (inputs) and y (output)
regr.fit(X, y)

#--Make a prediction using new input data
#--Example: Weight = 3300, Volume = 1300
#--The model predicts the CO2 emission for this input
predictedCO2 = regr.predict([[3300, 1300]])

# Print the predicted value
print(predictedCO2)