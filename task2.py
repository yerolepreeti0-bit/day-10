import pandas as pd

# Load dataset
df = pd.read_csv("customer_orders.csv")

# Check initial data types
print("Initial Data Types:\n")
print(df.dtypes)

# Clean Price column
df["Price"] = (
    df["Price"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Verify updated types
print("\nUpdated Data Types:\n")
print(df.dtypes)



