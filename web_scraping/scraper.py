import requests
from bs4 import BeautifulSoup
import pprint 

res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res.text, 'html.parser')

links = (soup.select('.titleline > a'))
subtext = soup.select('.subtext')
links2 = (soup2.select('.titleline >a'))
subtext2 = soup2.select('.subtext')

all_links = links + links2
all_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):                                  #This is a common sorting algortithm 
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)   #The lambda is a bit confusing and encouraged to investigate more on our own time

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()                  
        href = item.get('href', None)          
        votes = subtext[idx].select('.score')   
        if len(votes):                                                    
            points = int(votes[0].getText().replace(' points', '')) 
            if points > 99:
                hn.append({'title' : title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)                                #remember to change this to first call on the sorting function
    

pprint.pprint(create_custom_hn(all_links, all_subtext))