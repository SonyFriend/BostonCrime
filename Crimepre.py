import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import figure, show
from matplotlib.ticker import MaxNLocator
import time

data=pd.read_csv("C:/Users/user/Downloads/pythonCode/crime/crime.csv",encoding="gbk")
data=data.loc[(data['Lat']>35)&(data['Long']< -60)] #remove NA from 'Lat' and 'Long'
data=data.dropna(subset=["STREET"])
columns=['OFFENSE_CODE_GROUP']
#for j in columns:
#	print(j,data[j].unique())
print(data.isnull().sum())
type={label: idx for idx, label in enumerate(np.unique(data['OFFENSE_CODE_GROUP']))}
data['type']=data['OFFENSE_CODE_GROUP'].map(type) #change crime type to number
#print(type)
index=pd.Index(data['type'])
#print(index.value_counts().sort_values())

#############################################################################視覺化
#plt.bar(index.value_counts().index,index.value_counts())
#plt.xlabel("Crime type")
#plt.ylabel("Count")
#plt.title("Counting for Crime type")
#plt.show()
#########################################################################
Crime_year=pd.Index(data['YEAR'])
#plt.bar(Crime_year.value_counts().index,Crime_year.value_counts())
#ax =figure().gca()
#ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#ax.bar(Crime_year.value_counts().index,Crime_year.value_counts())
#plt.xlabel("Year")
#plt.ylabel("Count")
#plt.title("Counting the number for Crime (Year)")
#plt.show(ax)
#print(Crime_year.value_counts().index)
###############################################################################
data['OCCURRED_ON_DATE']=pd.to_datetime(data['OCCURRED_ON_DATE'])
data['YearMonth'] = data['OCCURRED_ON_DATE'].map(lambda x: x.strftime("%Y-%m"))
Crime_YearMonth=pd.Index(data['YearMonth'])

#plt.plot(Crime_YearMonth.value_counts().sort_index(),color='red')
#plt.xlabel("Time")
#plt.ylabel("Count")
#plt.title("Counting the number for Crime (month)")
#my_x_ticks=np.arange(0,39,6)
#plt.xticks(my_x_ticks)
#plt.show()
###################################################################################
import geopandas as gpd
import folium


incidents=folium.map.FeatureGroup()

#for lat,lon, in zip(data.Lat,data.Long):
#	incidents.add_child(folium.CircleMarker([lat,lon],radius=7,color='yellow',fill=True,fill_color='red',fill_opacity=0.4))

Lat=42.3
Lon=-71.1
#boston_map=folium.Map([Lat,Lon],zoom_start=12)
#boston_map.add_child(incidents)
#boston_map.save("mymap.html")

from folium import plugins
for j in range(4):
	data1=data[data['YEAR']==j+2015]
	filename="Crime"+str(j+2015)
	boston_map=folium.Map([Lat,Lon],zoom_start=12)
	incidents2=plugins.MarkerCluster().add_to(boston_map)
	for lat,lon,label in zip(data1.Lat,data1.Long,data1.OFFENSE_CODE_GROUP):
		folium.Marker(location=[lat,lon],icon=None,popup=label).add_to(incidents2)
	boston_map.add_child(incidents2)
	boston_map.save(filename+".html")

