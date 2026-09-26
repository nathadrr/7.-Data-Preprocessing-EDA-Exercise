import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df_normalisation = pd.read_csv("travel_expenses_transformed.csv")

df_minmax = df_normalisation.copy()
minMaxScaler = MinMaxScaler()
df_minmax["Amount ($)"] = minMaxScaler.fit_transform(df_normalisation[["Amount ($)"]])

df_zscore = df_normalisation.copy()
zScore = StandardScaler()
df_zscore["Amount ($)"] = zScore.fit_transform(df_normalisation[["Amount ($)"]])

df_minmax.to_csv("min_max_scaler_result.csv", index=False)
df_zscore.to_csv("zscore_scaler_result.csv", index=False)