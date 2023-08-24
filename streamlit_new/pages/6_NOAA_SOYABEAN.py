import pandas as pd 



import pandas as pd 
import streamlit as st 
import pickle


import plotly.graph_objects as go
from plotly.subplots import make_subplots



df = st.session_state["NOAA_data_soyabean"] 
# pd.read_csv("NOAA_GLOBAL/NOAA_data_soyabean.csv")






stations = st.sidebar.radio('Stations',(['Soyabean','Sugar']))
period = st.sidebar.radio('Period',(['Weekly','Monthly','Season']))
attributes = st.sidebar.radio('Attributes',(["Rainfall","Temperature"]))



sta = {"Soyabean":['Chicago', 'Indiana', 'Iowa', 'Minnesota', 'Ohio'],
            "Sugar":["bombay","lucknow","chennai","bihar_gatya"]}





per = {"Weekly":"Week_number","Monthly":"Month"}
attr = {"Rainfall":"PRCP","Temperature":"TAVG"}
agf = {"PRCP":"sum","TAVG":"mean"}

st.title("NOAA Stations")




def pivot_generation(df,val,cols,idx,agf,mar):
    return df.pivot_table(columns=cols,values =val,index =idx,aggfunc=agf, margins=mar)


year_start, year_end = st.slider('Select year range', min_value=2016, max_value=2023, value=(2018, 2023))
month_start, month_end = st.slider('Select month range', min_value=1, max_value=12, value=(1, 12))
week_start, week_end = st.slider('Select week range', min_value=1, max_value=52, value=(1, 52))



filtered_df = df[(df['Year'] >= year_start) & (df['Year'] <= year_end)]
filtered_df = filtered_df[(filtered_df['Month'] >= month_start) & (filtered_df['Month'] <= month_end)]
filtered_df = filtered_df[(filtered_df['Week_number'] >= week_start) & (filtered_df['Week_number'] <= week_end)]


#st.subheader("Piviots Tables for {}".format(padd))

val= attr[attributes]
cols = "Year"
idx = per[period]


 




for i in  list(sta[stations]):
    st.subheader(i)
    


    df  = filtered_df[filtered_df["Region"] == i]
    st.dataframe(pivot_generation(df,val,cols,idx,agf[val],True).round(2),width = 700)





	
	





