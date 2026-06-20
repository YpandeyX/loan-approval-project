import pandas as pd

df = pd.read_csv(r"C:\Users\YOGESH PANDIT\OneDrive\Desktop\loan_approval\Loan_approval.csv")


df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
df["Married"] = df["Married"].fillna(df["Married"].mode()[0])
df["Dependents"] = df["Dependents"].fillna(df["Dependents"].mode()[0])
df["Self_Employed"] = df["Self_Employed"].fillna(df["Self_Employed"].mode()[0])
df["Property_Area"] = df["Property_Area"].fillna(df["Property_Area"].mode()[0])
df["Credit_History"] = df["Credit_History"].fillna(df["Credit_History"].mode()[0])
df["Loan_Amount_Term"] = df["Loan_Amount_Term"].fillna(df["Loan_Amount_Term"].median())


df["Gender"] = df["Gender"].map({"Male": 1, "Female": 0})

df["Married"] = df["Married"].map({"Yes": 1, "No": 0})

df["Education"] = df["Education"].replace({
    "Graduate": 1,
    "Not Graduate": 0,
    "Grad": 1
})

df["Self_Employed"] = df["Self_Employed"].map({
    "Yes": 1,
    "No": 0
})

df["Loan_Status"] = df["Loan_Status"].map({
    "Y": 1,
    "N": 0
})

df["Dependents"] = df["Dependents"].replace({
    "0": 0,
    "1": 1,
    "2": 2,
    "3+": 3,
    "four": 4
})

df["Property_Area"] = df["Property_Area"].replace({
    "Rural": 0,
    "rural": 0,
    "Semiurban": 1,
    "semiurban": 1,
    "semi-urban": 1,
    "Urban": 2,
    "urban": 2,
    "Metro": 3,
    "metro": 3
})


df = df.drop("Loan_ID", axis=1)

# Convert remaining columns to numeric
df["Dependents"] = pd.to_numeric(df["Dependents"], errors="coerce")
df["Education"] = pd.to_numeric(df["Education"], errors="coerce")
df["Property_Area"] = pd.to_numeric(df["Property_Area"], errors="coerce")

print(df.dtypes)
print(df.isnull().sum())

# Train Test Split
from sklearn.model_selection import train_test_split

X = df.drop("Loan_Status", axis=1)
y = df["Loan_Status"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print(X_train.shape)
print(X_test.shape)


from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=42)

model.fit(X_train, y_train)

print("Model Training Complete")

from sklearn.metrics import accuracy_score

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
import pickle

pickle.dump(model, open("loan_model.pkl", "wb"))

print("Model Saved Successfully")
sample = X_test.iloc[[0]]

prediction = model.predict(sample)

print(prediction)