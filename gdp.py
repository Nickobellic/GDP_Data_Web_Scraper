import requests
import pandas as pd
import country_converter as coco
# PCAP -> GDP per Capita

country = input("Enter the Name of the Country: ").title()
alpha = coco.convert(names = country, to ='ISO3')

access_to_gdp = requests.get(f'http://api.worldbank.org/v2/country/{alpha}/indicator/NY.GDP.MKTP.CD?format=json')
access_to_per_cap = requests.get(f'http://api.worldbank.org/v2/country/{alpha}/indicator/NY.GDP.PCAP.CD?format=json')
access_to_gdp_ppp = requests.get(f'http://api.worldbank.org/v2/country/{alpha}/indicator/NY.GDP.MKTP.PP.CD?format=json')
 # divide by 12 zeros with 1

GDP = []
year = []
per_cap = []
ppp = []

for i in range(49):
    year.append(access_to_gdp.json()[1][i]['date'])
    GDP.append(access_to_gdp.json()[1][i]['value']/(10**12))
    per_cap.append(access_to_per_cap.json()[1][i]['value'])
    if access_to_gdp_ppp.json()[1][i]['value'] == None:
        ppp.append(0)
    else:
        ppp.append(access_to_gdp_ppp.json()[1][i]['value']/(10**12))

df = pd.DataFrame({'Year':year[::-1], 'GDP(Nominal) in Trillions ':GDP[::-1], 'GDP(PPP)':ppp[::-1], 'Per_Capita(Nominal)':per_cap[::-1]})
df.to_csv(f'{country}_GDP_stats.csv')

