import pandas as pd

# 1. Load CSV file
df = pd.read_csv("students.csv")

print("Original Dataset:\n")
print(df)

# -------------------------------
# 2. Detect missing values
# -------------------------------
missing_before = df.isnull().sum()

# -------------------------------
# 3. Replace missing scores with subject-wise mean
# -------------------------------
score_columns = ["Math_Score", "Science_Score", "English_Score"]

for col in score_columns:
    df[col] = df[col].fillna(df[col].mean())

# -------------------------------
# 4. Replace missing attendance with mean
# -------------------------------
df["Attendance_Percentage"] = df["Attendance_Percentage"].fillna(
    df["Attendance_Percentage"].mean()
)

# -------------------------------
# 5. Standardize student names
# -------------------------------
df["Name"] = df["Name"].fillna("Unknown")
df["Name"] = df["Name"].str.strip()
df["Name"] = df["Name"].str.capitalize()

# -------------------------------
# 6. Remove duplicate records
# -------------------------------
duplicates_removed = df.duplicated().sum()
df = df.drop_duplicates()

# -------------------------------
# 7. Detect missing values after cleaning
# -------------------------------
missing_after = df.isnull().sum()

# -------------------------------
# 8. Save cleaned dataset
# -------------------------------
df.to_csv("cleaned_students.csv", index=False)

# -------------------------------
# 9. Print results
# -------------------------------
print("\nCleaned Dataset:\n")
print(df)

print("\nSummary of Missing Values Handled:\n")
print("Missing values before cleaning:\n", missing_before)

print("\nMissing values after cleaning:\n", missing_after)

print("\nDuplicate records removed:", duplicates_removed)

print("\nCleaned file saved as 'cleaned_students.csv'")
