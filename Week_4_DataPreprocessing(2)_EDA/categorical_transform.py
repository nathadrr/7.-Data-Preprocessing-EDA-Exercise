import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("travel_expenses.csv")

df_transform = df.copy()

#TIPE DATA
#Nominal: Department, Destination, Expense Category
#Binary: Approval Status, Payment Mode

binary_mapping = {
  "Approval Status":{"Pending":0,"Approved":1},
  "Payment Mode":{"Corporate Card":0, "Personal Reimbursement":1}
}

for col, mapping in binary_mapping.items():
  df_transform[col] = df_transform[col].map(mapping) 

nominal_mapping = ["Department", "Destination", "Expense Category"]
label_encoder = LabelEncoder()

for col in nominal_mapping:
  df_transform[col] = label_encoder.fit_transform(df_transform[col])

df_transform.to_csv("travel_expenses_transformed.csv", index=False)

