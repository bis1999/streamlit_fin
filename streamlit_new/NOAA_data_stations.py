import requests
import pandas as pd 
import numpy as np 

from stqdm import stqdm





url ="https://ncei.noaa.gov/access/services/data/v1?dataset=daily-summaries&stations={}&startDate=2016-01-01&endDate=2023-08-23&includeAttributes=true&format=json"
chic_url = url.format('USW00094846')
iowa_burlington = url.format("USW00014931")
mins_st = url.format('USW00014922')
indianapolis_int = url.format('USW00093819')
ohio_john_Glenn = url.format('USW00014821')



bombay = url.format('IN012070800')
lucknow = url.format('IN023351400')
banglore = url.format('IN009010100')
chennai = url.format('IN020040900')
bihar_gatya = url.format('IN004051800')

# Add it to the streamlit 

soyabean_stations = {'USW00094846':"Chicago","USW00014931":"Iowa",'USW00014922':"Minnesota",'USW00093819':'Indiana','USW00014821':'Ohio','IN012070800':"bombay","IN023351400":"lucknow",'IN009010100':"chennai",'IN020040900':'Indiana','IN004051800':'bihar_gatya'}

#soyabean = [chic_url,iowa_burlington,mins_st,indianapolis_int,ohio_john_Glenn]



def celsius_to_fahrenheit(celsius):
    celsius = celsius/10
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit



def station_update():
	data_list = []


	for i in stqdm(list(soyabean_stations.keys())):

	    url_ = url.format(i)
	    
	    
	    r = requests.get(url_)
	    dfs=pd.DataFrame(r.json())
	    #cols = ['DATE', 'STATION','TMAX', 'TAVG', 'TMIN']

	    dfs[['TMAX', 'TAVG', 'TMIN','PRCP']] = dfs[['TMAX', 'TAVG', 'TMIN','PRCP']].astype("float64")
	    dfs[['TMAX', 'TAVG', 'TMIN','PRCP']] = dfs[['TMAX', 'TAVG', 'TMIN','PRCP']].interpolate()
	    dfs["TAVG"]=dfs["TAVG"].map(celsius_to_fahrenheit)
	    dfs["Region"] = soyabean_stations[i]
	    dfs["DATE"] =  pd.to_datetime(dfs["DATE"])
	    
	    dfs["Week_number"] = dfs["DATE"].dt.isocalendar().week
	    dfs["Year"] = dfs["DATE"].dt.year
	    dfs["Month"] = dfs["DATE"].dt.month
	   
	    
	    data_list.append(dfs)

	    data = pd.concat(data_list)

	return data
    
    