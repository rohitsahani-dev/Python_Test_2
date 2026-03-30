# ===============================
# IMPORT LIBRARIES
# ===============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# ===============================
# LOAD DATA
# ===============================
df = pd.read_csv("T_17.csv")

print("=== FIRST 5 ROWS ===")
print(df.head())

print("\n=== DATA INFO ===")
print(df.info())

print("\n=== STATISTICS ===")
print(df.describe())

# ===============================
# DATA CLEANING
# ===============================
# Check missing values
print("\nMissing values:\n", df.isnull().sum())

# ===============================
# FEATURE ENGINEERING
# ===============================
# Create new column: Total Score
df["Total"] = df["Assignments_Score"] + df["Mid_Exam"] + df["Final_Exam"]

# Create performance label
df["Performance"] = np.where(df["Total"] > 240, "Good", "Average")

print("\n=== UPDATED DATA ===")
print(df.head())

# ===============================
# NUMPY OPERATIONS
# ===============================
avg_study = np.mean(df["Hours_Study"])
max_score = np.max(df["Final_Exam"])

print("\nAverage Study Hours:", avg_study)
print("Max Final Exam Score:", max_score)

# ===============================
# DATA VISUALIZATION
# ===============================

# 1. Study vs Final Exam
plt.figure()
plt.scatter(df["Hours_Study"], df["Final_Exam"])
plt.xlabel("Study Hours")
plt.ylabel("Final Exam Score")
plt.title("Study vs Performance")
plt.show()

# 2. Attendance vs Final
plt.figure()
plt.plot(df["Attendance"], df["Final_Exam"])
plt.xlabel("Attendance")
plt.ylabel("Final Score")
plt.title("Attendance Impact")
plt.show()

# 3. Histogram
plt.figure()
plt.hist(df["Final_Exam"])
plt.title("Distribution of Final Exam Scores")
plt.show()

# 4. Bar chart (Name vs Total Score)
plt.figure()
plt.bar(df["Name"], df["Total"])
plt.title("Total Score by Student")
plt.show()

# ===============================
# MACHINE LEARNING MODEL
# ===============================

# Features (input)
X = df[["Hours_Study", "Sleep_Hours", "Attendance"]]

# Target (output)
y = df["Final_Exam"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create model
model = LinearRegression()

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, predictions)

print("\nModel Error (MSE):", mse)

# ===============================
# PREDICT YOUR OWN DATA
# ===============================
my_data = np.array([[6, 7, 85]])  # study, sleep, attendance
result = model.predict(my_data)

print("\nPredicted Final Score:", result[0])