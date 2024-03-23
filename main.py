from bs4 import BeautifulSoup
import data
import requests
import csv
soup = BeautifulSoup(data.data , "html.parser")
a = soup.select('.page__main .tw-my-2 h2 a')
links = []
new_links = []
numbers = []
myitems = []
for i in range(100):
    if 'href' in a[i].attrs and a[i]['href'] is not None:
        link = 'https://www.allabolag.se' + a[i]['href']
        links.append(link)
        parts = link.split('/')
        parts[-1] = 'adresser'
        new_link = '/'.join(parts)
        new_links.append(new_link)
        number = parts[-2]
        page = requests.get(new_link)
        src = page.content
        soup = BeautifulSoup(src , "html.parser")
        name = soup.select_one('.p-name')
        postal = soup.select_one('.p-postal-code')
        locality = soup.select_one('.p-locality')
        region = soup.select_one('.p-region')
        item = []
        item.append(number)
        item.append(new_link)
        if name is not None:
             item.append(name.text.strip())
        else:
            item.append(' ')
        if postal is not None:
            item.append(postal.text.strip())
        else:
            item.append(' ')

        if locality is not None:
            item.append(locality.text.strip())
        else:
            item.append(' ')

        if region is not None:
            item.append(region.text.strip())
        else:
            item.append(' ')
        myitems.append(item)
with open('D:/Programming/web scraping/up work tesks/tesks.csv', 'w', encoding='utf-8-sig') as mydata:
    csvfille = csv.writer(mydata)
    csvfille.writerows(myitems)
print(len(links))
print(len(numbers))
print(len(new_links))
print(len(myitems))



