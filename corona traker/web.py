from bs4 import BeautifulSoup
import requests

result= requests.get('https://www.worldometers.info/coronavirus/country/sri-lanka/')
scr= result.content
soup= BeautifulSoup(scr, 'html.parser')
number_of_patians=soup.find(class_='maincounter-number').get_text()
lates_news= soup.find(class_='news_date').get_text()
count= soup.find_all('span')
number_of_deaths=str(count[5])
number_of_deaths= number_of_deaths[6:8]
number_of_recovered=str(count[6])
number_of_recovered= number_of_recovered[6:11]

# print(lates_news)