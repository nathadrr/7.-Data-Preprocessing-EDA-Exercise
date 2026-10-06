import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt

st.set_page_config(page_title="EXPLORATORY DATA ANALYSIS", layout="wide")

df = pd.read_csv("travel_expenses.csv")
df_eda = df.copy()

st.title("Exploratory Data Analysis")
st.markdown("**Dataset loaded from `travel_expenses.csv`**")

st.subheader("Dataset Metadata")
col_met1, col_met2 = st.columns(2)
col_met1.metric("Total Records (row)", df.shape[0])
col_met2.metric("Total Attributes (column) ", df.shape[1])

st.divider()

st.subheader("Data Preview")
st.dataframe(df_eda)

st.divider()

st.subheader("Summary Statistics")
col1, col2 = st.columns(2)
with col1:
  st.subheader("Numerical")
  st.dataframe(df.describe())
with col2:
  st.subheader("Categorical")
  st.dataframe(df.describe(include=['object']).drop(['Expense ID', 'Employee Name'],axis=1, errors='ignore') )


st.subheader("Statistics Boxplots")
col11,col22 = st.columns(2)
with col11:
  fig = px.box(df_eda, y="Amount ($)")
  fig.update_traces(boxpoints='all', jitter=0.3)
  fig.update_xaxes(showticklabels=False, title_text="Amount ($)")
  fig.update_yaxes(showticklabels=True, title_text="")
  st.plotly_chart(fig)

st.divider()

st.subheader("Data Distribution")
col1,col2,col3 = st.columns(3)

with col1:
  st.markdown("##### 1. Distribution of Departments")
  hist_department = df['Department'].value_counts().sort_index()
  st.bar_chart(hist_department, x_label="Department", y_label="Jumlah")

with col2:
  st.markdown("##### 2. Distribution of Destination")
  hist_dest = df['Destination'].value_counts().sort_index()
  st.bar_chart(hist_dest, x_label="Destination", y_label="Jumlah")

with col3:
  st.markdown("##### 3. Distribution of Expense Category")
  hist_exp = df['Expense Category'].value_counts().sort_index()
  st.bar_chart(hist_exp, x_label="Expense Category", y_label="Jumlah")

  with col1:
    st.markdown("##### 4. Distribution of Payment Mode")
    hist_pay = df['Payment Mode'].value_counts().sort_index()
    st.bar_chart(hist_pay, x_label="Payment mode", y_label="Jumlah")

  with col2:
    st.markdown("##### 5. Distribution of Approval Status")
    hist_app = df['Approval Status'].value_counts().sort_index()
    st.bar_chart(hist_app, x_label="Approval Status", y_label="Jumlah")

  with col3:
    st.markdown("##### 6. Histogram of Amount")
    bins_p = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    labels_p = ["0-100", "100-200", "200-300", "300-400", "400-500", "500-600", "600-700", "700-800", "800-900", "900-1000"]
    hist_a = pd.cut(df['Amount ($)'], bins=bins_p, labels=labels_p)

    fig = px.histogram(hist_a, x="Amount ($)", height=350)

    fig.update_xaxes(
      title_text = "Amount ($)",
      categoryorder = "array",
      categoryarray = labels_p
    )
    fig.update_layout(bargap=0)
    fig.update_yaxes(title_text="Jumlah Karyawan")
    st.plotly_chart(fig)

st.divider()

st.subheader("Data Visualisation")


col1, col2 = st.columns(2)

# 1. Expense Category vs Amount
with col1:
    expense_category = (
        df_eda.groupby("Expense Category")["Amount ($)"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        expense_category,
        x="Expense Category",
        y="Amount ($)",
        title="Total Expense berdasarkan Expense Category"
    )

    fig.update_layout(
        xaxis_title="Expense Category",
        yaxis_title="Total Amount ($)"
    )

    st.plotly_chart(fig, use_container_width=True)


# 2. Department vs Amount
with col2:
    department_amount = (
        df_eda.groupby("Department")["Amount ($)"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        department_amount,
        x="Department",
        y="Amount ($)",
        title="Total Expense berdasarkan Department"
    )

    fig.update_layout(
        xaxis_title="Department",
        yaxis_title="Total Amount ($)"
    )

    st.plotly_chart(fig, use_container_width=True)


col1, col2 = st.columns(2)

# 3. Approval Status vs Amount
with col1:
    fig = px.box(
        df_eda,
        x="Approval Status",
        y="Amount ($)",
        points="all",
        title="Amount berdasarkan Approval Status"
    )

    fig.update_layout(
        xaxis_title="Approval Status",
        yaxis_title="Amount ($)"
    )

    st.plotly_chart(fig, use_container_width=True)


# 4. Payment Mode vs Amount
with col2:
    payment_amount = (
        df_eda.groupby("Payment Mode")["Amount ($)"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        payment_amount,
        x="Payment Mode",
        y="Amount ($)",
        title="Total Expense berdasarkan Payment Mode"
    )

    fig.update_layout(
        xaxis_title="Payment Mode",
        yaxis_title="Total Amount ($)"
    )

    st.plotly_chart(fig, use_container_width=True)


col1, col2 = st.columns(2)

# 1. Department + Expense Category + Amount
with col1:
    department_category = (
        df_eda.groupby(
            ["Department", "Expense Category"]
        )["Amount ($)"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        department_category,
        x="Department",
        y="Amount ($)",
        color="Expense Category",
        barmode="group",
        title="Expense berdasarkan Department dan Expense Category"
    )

    fig.update_layout(
        xaxis_title="Department",
        yaxis_title="Total Amount ($)"
    )

    st.plotly_chart(fig, use_container_width=True)


# 2. Destination + Expense Category + Amount
with col2:
    destination_category = (
        df_eda.groupby(
            ["Destination", "Expense Category"]
        )["Amount ($)"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        destination_category,
        x="Destination",
        y="Amount ($)",
        color="Expense Category",
        barmode="stack",
        title="Expense berdasarkan Destination dan Expense Category"
    )

    fig.update_layout(
        xaxis_title="Destination",
        yaxis_title="Total Amount ($)"
    )

    st.plotly_chart(fig, use_container_width=True)


col1, col2 = st.columns(2)

# 3. Department + Approval Status + Amount
with col1:
    department_approval = (
        df_eda.groupby(
            ["Department", "Approval Status"]
        )["Amount ($)"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        department_approval,
        x="Department",
        y="Amount ($)",
        color="Approval Status",
        barmode="group",
        title="Expense berdasarkan Department dan Approval Status"
    )

    fig.update_layout(
        xaxis_title="Department",
        yaxis_title="Total Amount ($)"
    )

    st.plotly_chart(fig, use_container_width=True)


# 4. Destination + Payment Mode + Amount
with col2:
    destination_payment = (
        df_eda.groupby(
            ["Destination", "Payment Mode"]
        )["Amount ($)"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        destination_payment,
        x="Destination",
        y="Amount ($)",
        color="Payment Mode",
        barmode="group",
        title="Expense berdasarkan Destination dan Payment Mode"
    )

    fig.update_layout(
        xaxis_title="Destination",
        yaxis_title="Total Amount ($)"
    )

    st.plotly_chart(fig, use_container_width=True)



