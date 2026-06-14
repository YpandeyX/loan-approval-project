import pandas as pd

df = pd.read_csv(r"C:\Users\YOGESH PANDIT\OneDrive\Desktop\loan_approval\Loan_approval.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())