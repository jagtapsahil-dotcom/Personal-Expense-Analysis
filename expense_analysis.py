import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Load dataset (CSV, not .py)
# -------------------------------
df = pd.read_csv(r"C:\Users\Rajdeep\Documents\Personal_Expense_Analysis\data\expenses.csv")

# -------------------------------
# Clean column names
# -------------------------------
df.columns = df.columns.str.strip()

# -------------------------------
# Data cleaning & preparation
# -------------------------------
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

print("First 5 rows:")
print(df.head())

# -------------------------------
# Total spending
# -------------------------------
total_spent = df['Amount'].sum()
print("Total Amount Spent:", total_spent)

# -------------------------------
# Spending by category
# -------------------------------
category_spending = df.groupby('Category')['Amount'].sum()
print("\nCategory-wise Spending:")
print(category_spending)

# -------------------------------
# Visualization – Category-wise Spending
# -------------------------------
plt.figure(figsize=(8, 5))
sns.barplot(x=category_spending.index, y=category_spending.values)
plt.title("Spending by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.show()

# -------------------------------
# Monthly spending trend
# -------------------------------
monthly_spending = df.groupby('Month')['Amount'].sum()

plt.figure(figsize=(8, 5))
sns.lineplot(x=monthly_spending.index, y=monthly_spending.values, marker='o')
plt.title("Monthly Expense Trend")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.show()

# -------------------------------
# Data understanding
# -------------------------------
print("\nData Info:")
print(df.info())

print("\nData Description:")
print(df.describe())

# -------------------------------
# Missing value handling
# -------------------------------
print("\nMissing values:")
print(df.isnull().sum())

df = df.dropna()

# -------------------------------
# Budget vs Actual
# -------------------------------
budget_vs_actual = df.groupby('Category')[['Amount', 'Budget']].sum()
budget_vs_actual['Over_Spend'] = budget_vs_actual['Amount'] - budget_vs_actual['Budget']

print("\nBudget vs Actual:")
print(budget_vs_actual)

