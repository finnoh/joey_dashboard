# Add a chart
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import streamlit as st  # 🎈 data web app development
import yaml

s_secret_path = "secrets/sheet.yaml"

with open(s_secret_path, 'r') as file:
    yaml_data = yaml.safe_load(file)

s_link = f"https://docs.google.com/spreadsheets/d/{yaml_data['sheet_id']}/gviz/tq?tqx=out:csv&sheet={yaml_data['sheet_name']}"

# data 
df = pd.read_csv(s_link)


# Set the page title
st.set_page_config(page_title="Joey's Dashboard")

# set a title
st.title("Joey's Dashboard")

# Display the data frame
st.write("Data:")
st.write(df)

# Create a selectbox to choose the y-axis column
cols = df.columns
selected_column = st.selectbox("Select a column for the y-axis:", cols[1:])

# Create a line chart based on the selected column
st.line_chart(df.set_index("date")[selected_column])

# create a scatterplot
selected_column_a = st.selectbox("Select a column for the x-axis:", cols[1:], key="selectbox_a")
selected_column_b = st.selectbox("Select a column for the y-axis:", cols[1:], key="selectbox_b")
st.scatter_chart(data=df, x=selected_column_a, y=selected_column_b)