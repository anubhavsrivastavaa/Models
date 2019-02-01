import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import sklearn.linear_model

#Load the data
oecd_bli=pd.read_csv("..\\Data\\BLI_2017.csv", thousands=',', encoding='utf-8-sig') 	# utf-8 encoding has BOM issues leading me to use utf-8-sig
gdp_per_capita=pd.read_csv("..\\Data\\IMF_Data.xls", thousands=',', delimiter='\t', encoding='latin1', na_values='n/a')


#Prepare the data for analysis, merging the data from two sources that is IMF and OECD
def prepare_country_stats(oecd_bli,gdp_per_capita):
	
	#print(oecd_bli)
	is_lifesatifaction= oecd_bli['Indicator'] == 'Life satisfaction'
	is_total= oecd_bli['Inequality'] == 'Total'
	country_satisfacton_value=oecd_bli[is_lifesatifaction & is_total][['Country','Value']]
	print(country_satisfacton_value)

	coutry_gdp_values=gdp_per_capita[['Country','GDP']]
	print(coutry_gdp_values)

	#joining the data of two tables
	consolidated_data=pd.merge(country_satisfacton_value,coutry_gdp_values, on='Country')
	consolidated_data.columns=['Country','Life Satisfaction','GDP per Capita']
	print(consolidated_data)
	return consolidated_data

consolidated_data=prepare_country_stats(oecd_bli,gdp_per_capita)

X=np.c_[consolidated_data["GDP per Capita"]]
Y=np.c_[consolidated_data["Life Satisfaction"]]

#Visualize the Data
consolidated_data.plot(kind='scatter', x='GDP per Capita', y='Life Satisfaction')
plt.show()

#Linear Model
linear_model= sklearn.linear_model.LinearRegression()

#Training the Model
linear_model.fit(X,Y)

#Make a prediction for Cyprus
X_new=[[22587]]
print(linear_model.predict(X_new))