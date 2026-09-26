import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("travel_expenses.csv")
df_eda = df.copy()

st.subheader("Travel Expenses Dataset")
st.dataframe(df_eda)

expense_category = (df_eda.groupby("Expense Category")["Amount ($)"].sum().reset_index())

fig, ax = plt.subplots()

sns.barplot(
  data=expense_category,
  x = "Expense Category",
  y = "Amount ($)",
  ax=ax
)

ax.set_title("Total Expense berdasarkan Expense Category")
ax.set_xlabel("Expense Category")
ax.set_ylabel("Total Amount ($)")

st.pyplot(fig)

destination_info = (df_eda.groupby("Destination")["Amount ($)"].sum().reset_index())
fig, ax = plt.subplots()

ax.pie(
  destination_info["Amount ($)"], 
  labels = destination_info["Destination"], 
  autopct="%1.1f%%")

ax.set_title("Total Expense berdasarkan Destination")
st.pyplot(fig)



