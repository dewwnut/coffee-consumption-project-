import streamlit as st
import pandas as pd
from src.data_processing import clean_data
from src.visualizations import plot_consumption

st.title("☕ Coffee Consumption Dashboard")

df = pd.read_csv("data/coffee_consumption.csv")
df_cleaned = clean_data(df)

st.write("### Data Preview", df_cleaned.head())

st.write("### Coffee Consumption by Country")
plot_consumption(df_cleaned)
