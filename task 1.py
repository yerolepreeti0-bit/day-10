import pandas as pd

# Load dataset
df = pd.read_csv("customer_orders.csv")

# Shape before cleaning
print("Shape BEFORE cleaning:", df.shape)

# Missing values report
print("\nMissing Values Report:")
print(df.isna().sum())

# Fill missing numeric values with median
numeric_cols = df.select_dtypes(include="number").columns
for col in numeric_cols:
   df[col] = df[col].fillna(df[col].median())


# Remove duplicate rows
df_cleaned = df.drop_duplicates()

# Shape after cleaning
print("\nShape AFTER cleaning:", df_cleaned.shape)
