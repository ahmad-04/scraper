from bs4 import BeautifulSoup
import requests

# URL to scrape
url = 'https://www.gsmarena.com/apple-phones-48.php'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
elements = soup.find('div', class_='makers').find_all('li')

# Loop through the list of phones
for element in elements:
    name = element.find('strong').text
    route = element.find('a')['href']
    link = "https://www.gsmarena.com/"+ route
    link_text = requests.get(link).text
    link_ = BeautifulSoup(link_text, 'lxml')
    memory  = link_.find('td', {"data-spec": 'internalmemory'})
    print(memory)
    # print(name +", "+ link)