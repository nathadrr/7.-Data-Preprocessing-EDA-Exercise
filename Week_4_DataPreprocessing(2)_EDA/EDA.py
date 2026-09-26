import streamlit as st
import pandas as pd
import seaborn as sns

df = pd.read_csv("Week_4_DataPreprocessing(2)_EDA/travel_expenses.csv")
df_eda = df.copy()

sns.heatmap()
