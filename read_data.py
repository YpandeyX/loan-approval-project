import pandas as pd

df = pd.read_csv(r"C:\Users\YOGESH PANDIT\OneDrive\Desktop\loan_approval\Loan_approval.csv")

print(df.isnull().sum())

df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
df["Married"] = df["Married"].fillna(df["Married"].mode()[0])
df["Dependents"] = df["Dependents"].fillna(df["Dependents"].mode()[0])
df["Self_Employed"] = df["Self_Employed"].fillna(df["Self_Employed"].mode()[0])
df["Property_Area"] = df["Property_Area"].fillna(df["Property_Area"].mode()[0])
df["Credit_History"] = df["Credit_History"].fillna(df["Credit_History"].mode()[0])
df["Loan_Amount_Term"] = df["Loan_Amount_Term"].fillna(df["Loan_Amount_Term"].median())

print(df.isnull().sum())

df["Gender"] = df["Gender"].map({"Male": 1, "Female": 0})
df["Married"] = df["Married"].map({"Yes": 1, "No": 0})
df["Education"] = df["Education"].replace({
    "Graduate": 1,
    "Not Graduate": 0,
    "Grad": 1
})
df["Self_Employed"] = df["Self_Employed"].map({"Yes": 1, "No": 0})
df["Loan_Status"] = df["Loan_Status"].map({"Y": 1, "N": 0})

print(df.head())
print(df.dtypes)
print(df["Education"].unique())
print(df["Education"].isnull().sum())


df["Dependents"] = df["Dependents"].replace({
    "0": 0,
    "1": 1,
    "2": 2,
    "3+": 3,
    "four": 4
})

df["Property_Area"] = df["Property_Area"].replace({
    "Rural": 0,
    "Semiurban": 1,
    "Urban": 2,
    "Metro": 3
})

df = df.drop("Loan_ID", axis=1)

print(df.dtypes)