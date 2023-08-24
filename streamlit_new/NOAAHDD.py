################################################## 

"""
st.subheader(':green[NOAA CDD/HDD]')
st.write("Data Source: https://ftp.cpc.ncep.noaa.gov/htdocs/products/analysis_monitoring/cdus/degree_days/archives/")

noaa_datasets = glob.glob('noaa/*.csv')
noaa_week = [i.split(".")[0].split("/")[1] for i in noaa_datasets]
noaa_date = max(noaa_week)

st.write("Last NOAA: {} ".format(noaa_date))
st.write("https://www.eia.gov/dnav/ng/ng_stor_wkly_s1_w.htm")

if st.button("Update NOAA"):
    noaa_ = pd.read_csv("noaa/{}.csv".format(noaa_date))

    today = date.today()
    st.write("NOAA on {}".format(str(today)))
else:
    noaa_ = pd.read_csv("noaa/{}.csv".format(noaa_date))


st.session_state["noaa_df"] =  noaa_


latest_date = max(noaa_['Period'])
st.write("Latest Data Available: {} ".format(latest_date))



tmp_download_link = download_link(noaa_, 'NOAA.csv', 'Click here to download your data!')
st.markdown(tmp_download_link, unsafe_allow_html=True)

"""


################################################## 
    