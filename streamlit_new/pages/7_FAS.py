import pandas as pd 
import streamlit as st 
import numpy as np

df = pd.read_csv("Data_FAS/FAS_data.csv")

st.title("Indian Sugar")

np.unique(df["calendarYear"])

year_list = list(np.unique(df["calendarYear"]))

y = st.sidebar.selectbox("Year",tuple(year_list))



req_df = df[df["calendarYear"] == y][["Attributes","marketYear","calendarYear","month","value"]]

st.dataframe(req_df,width=500)