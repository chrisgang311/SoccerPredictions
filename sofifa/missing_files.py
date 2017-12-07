import glob, os
import requests
from bs4 import BeautifulSoup

def getAllVersionLinks():
    return_dict = {}
    page = requests.get("https://sofifa.com/")
    soup = BeautifulSoup(page.content, "lxml")
    filter_body = soup.find('div', attrs={'class': 'filter-body'})
    card_headers = filter_body.find_all('div', attrs={'class' : 'card-header'})
    card_bodies = filter_body.find_all('div', attrs={'class':'card-body'})
    for card_header, card_body in zip(card_headers, card_bodies):
        links = card_body.find_all('a')
        for link in links:
            month_year = card_header.text.split('  ')
            month = month_year[0]
            year = month_year[1]
            name = "FIFA%s_%s_%s_%s" % (card_body.parent.parent['data-tag'][-2:], year, month, link.text)
            return_dict[name] = link['href']
    return return_dict



os.chdir('/Users/steeve/Documents/ETH/Austauschsemester/Data Science Laboratory/Final Project/sofifa')
files = glob.glob("FIFA*.csv")
filename_array = []
linkdict = getAllVersionLinks()
for filename, link in linkdict.items():
    full_name = "%s.csv" % str(filename)
    if full_name in files:
        continue
    filename_array.append(full_name)

print "The following %d files missing: \n" % len(filename_array)
#print filename_array

