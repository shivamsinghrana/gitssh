from bs4 import BeautifulSoup
import requests
import pandas as pd
#i get error as i dont seprate every year by evey column

years = ["1930", "1934", "1938", "1950", "1954", "1958", "1962", "1966", "1970", "1974", "1978", "1982", "1986", "1990", "1994", "1998", "2002", "2006", "2010", "2014", "2018"]
def get_matches(year):
    #in website link we need to replce 2014 by year to all year data show
    web=f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    response=requests.get(web)
    #print(response.text)#these show all html css website 
    content=response.text
    soup=BeautifulSoup(content,'lxml')#soup is use to extract data from website
#here we install pip intall xml
#here we made data frame column name 
    matches = soup.find_all('div', class_='footballbox')#class name as footvballbox get this info from inpect of website which contain detail of all data
    home =[]
    score =[]
    away=[]
    for match in matches:
    #first we use here print to show  all detail score byt reove and 
        home.append(match.find('th', class_='fhome').get_text())
        score.append(match.find('th', class_='fscore').get_text())
        away.append(match.find('th', class_='faway').get_text())
    dict_football={'home': home,'score' :score,'away': away}
    df_football=pd.DataFrame(dict_football) 
    df_football['year']=year
    #here we return data frame df_football
    return df_football #thts how extract data from wikipedia websiyte here only for 2014 world cup
#print(get_matches('1930'))
#for year 1982 there is not simlar way of data fram as all years so we need to handle this
#how to inpect this website properly
#put all data in table so we use pandas
#either use find or find all we use finnda all bcoz multiple matches
fifa=[get_matches(year) for year in years]#list comprenshion
#for year in years:
# get_matches(years)
df_fifa = pd.concat(fifa,ignore_index=True)#to add all th tabales and dataframe
df_fifa.to_csv('fifa_worldcup_historical_data.csv', index=False)   
#index= false not show index which show early
df_fixture=get_matches(2022)
df_fixture.to_csv('fifa_worldcup_fixture.csv',index=False)

#data cleaning

#df_historical_data = pd.read_csv('fifa_worldcup_matches.csv')
df_fixture = pd.read_csv('fifa_worldcup_fixture.csv')
df_missing_data = pd.read_csv('fifa_worldcup_missing_data.csv')


df_fixture['home']=df_fixture['home'].str.strip()
df_fixture['away'] = df_fixture['away'].str.strip()
df_missing_data.dropna(inplace=True)
df_historical_data = pd.concat([df_historical_data, df_missing_data], ignore_index=True)
df_historical_data.drop_duplicates(inplace=True)
df_historical_data.sort_values('year', inplace=True)
df_historical_data