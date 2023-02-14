import pandas as pd
from sqlite3 import connect
import streamlit as st

conn = connect("stocks.db")
data = pd.read_csv("https://raw.githubusercontent.com/JaniceLibbyThomas/dummy1/main/Secrets.csv")
data.to_sql("meta",conn)
df = pd.read_sql("SELECT * FROM meta",conn)
st.dataframe(df)
