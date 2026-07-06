import pandas as pd

print("\n==================== SERIES ====================\n")

# Create a Pandas Series
Marks = pd.Series([85, 90, 78, 92, 88])
print(Marks)

print("\n==================== DATAFRAME ====================\n")

# Create a DataFrame using a dictionary
student = {
    "ID": [101, 102, 103, 104, 105],
    "Name": ["Raju", "Asha", "Kiran", "Priya", "Arun"],
    "Age": [21, 20, 22, 21, 23],
    "Department": ["CSE", "IT", "ECE", "CSE", "AIDS"],
    "Marks": [85, 90, 78, 95, 88]
}

df = pd.DataFrame(student)
print(df)

print("\n==================== ROWS & COLUMNS ====================\n")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n==================== HEAD() ====================\n")

print(df.head())

print("\n----- head(2) -----\n")
print(df.head(2))

print("\n==================== TAIL() ====================\n")

print(df.tail())

print("\n----- tail(3) -----\n")
print(df.tail(3))

print("\n==================== SHAPE ====================\n")

print(df.shape)

print("\n==================== COLUMNS ====================\n")

print(df.columns)

print("\n==================== SINGLE COLUMN SELECTION ====================\n")

print(df["Department"])

print("\n==================== INFO() ====================\n")

print(df.info())

print("\n==================== DESCRIBE() ====================\n")

print(df.describe())

print("\n==================== SINGLE COLUMN ====================\n")

print(df["Name"])

print("\n==================== MULTIPLE COLUMNS ====================\n")

print(df[["Name", "Marks"]])

print("\n==================== ROW SELECTION (loc) ====================\n")

print(df.loc[2])

print("\n==================== ROW SELECTION (iloc) ====================\n")

print(df.iloc[2])

print("\n==================== MULTIPLE ROWS ====================\n")

print(df.loc[1:3])

print("\n==================== READ CSV ====================\n")

df = pd.read_csv("students.csv")
print(df)

print("\n==================== WRITE CSV ====================\n")

df.to_csv("output.csv", index=False)
print("CSV file saved successfully.")

print("\n==================== DATA CLEANING ====================\n")

data = {
    "Name": ["Raju", "Asha", "Raju", " Kiran ", None],
    "Age": [21, None, 21, 22, 23],
    "Department": ["CSE", "IT", "CSE", "ECE", "AIDS"],
    "Marks": [85, 90, 85, None, 88]
}

df = pd.DataFrame(data)

print("\n----- Original DataFrame -----\n")
print(df)

print("\n==================== MISSING VALUES ====================\n")

print("\n----- isnull() -----\n")
print(df.isnull())

print("\n----- notnull() -----\n")
print(df.notnull())

print("\n----- dropna() -----\n")
print(df.dropna())

print("\n----- fillna(0) -----\n")
print(df.fillna(0))

print("\n----- fillna(mean) -----\n")
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)

print("\n==================== DUPLICATE VALUES ====================\n")

print("\n----- duplicated() -----\n")
print(df.duplicated())

print("\n----- drop_duplicates() -----\n")
print(df.drop_duplicates())

print("\n==================== RENAME COLUMNS ====================\n")

df = df.rename(columns={
    "Name": "Student_Name",
    "Marks": "Score"
})

print(df)

print("\n==================== CHANGE DATA TYPE ====================\n")

df["Age"] = df["Age"].astype(float)
print(df.dtypes)

print("\n==================== REPLACE VALUES ====================\n")

df["Department"] = df["Department"].replace("IT", "Information Technology")
print(df)

print("\n==================== STRING CLEANING ====================\n")

print("\n----- lower() -----\n")
df["Department"] = df["Department"].str.lower()
print(df)

print("\n----- upper() -----\n")
df["Department"] = df["Department"].str.upper()
print(df)

print("\n==================== SORT VALUES ====================\n")

print("\n----- Ascending Order -----\n")
print(df.sort_values(by="Score"))

print("\n----- Descending Order -----\n")
print(df.sort_values(by="Score", ascending=False))