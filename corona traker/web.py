from bs4 import BeautifulSoup
import requests

result= requests.get('https://www.worldometers.info/coronavirus/country/sri-lanka/')
scr= result.content
soup= BeautifulSoup(scr, 'html.parser')
number_of_patians=soup.find(class_='maincounter-number').get_text()
count= soup.find_all('span')
number_of_deaths=str(count[5])
number_of_recovered=str(count[6])
number_of_recovered= number_of_recovered.replace('<span>','')
number_of_recovered= number_of_recovered.replace('</span>','')
number_of_deaths= number_of_deaths.replace('<span>','')
number_of_deaths= number_of_deaths.replace('</span>','')
lates_news= soup.find(class_='news_li').get_text()
lates_news= lates_news.replace('[source]', '')
day= str(soup.find(class_='news_date').get_text())
lates_news= str(lates_news)+' on the '+day
# print(lates_news)
# print(day)