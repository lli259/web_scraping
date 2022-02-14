import requests
from bs4 import BeautifulSoup
import json
import time






def getlebron():

    url='http://nba.hupu.com/games/boxscore/162109'
    page = requests.get(url)  
    print('status_code',page.status_code)
    print('SUCC:200. ERROR:4 or a 5-----------------------\n')


    soup=BeautifulSoup(page.content,'html.parser')
    alltables = soup.find_all("table", id="J_away_content")
    allplayers = alltables[0].find_all("tr")
    allvalues=allplayers[3].find_all("td")
    print(allvalues[-2].get_text())


for i in range(10):
    print(i)
    getlebron()
    time.sleep(1)

exit()

url='http://nba.hupu.com/games/boxscore/162109'


#1 get content
page = requests.get(url)  
print('status_code',page.status_code)
print('SUCC:200. ERROR:4 or a 5-----------------------\n')

soup=BeautifulSoup(page.content,'html.parser')
#soup.prettify()


#2 find p tag step by step
#soup has children, get tags
print([type(item) for item in list(soup.children)])
#[bs4.element.Doctype, bs4.element.NavigableString, bs4.element.Tag]
'''
The first is a Doctype object, which contains information about the type of the document.
The second is a NavigableString, which represents text found in the HTML document.
The final item is a Tag object, which contains other nested tags.
'''
html = list(soup.children)[2]


# tag has children, get body
tagchildren=list(html.children)
print(tagchildren)
body = list(html.children)[3]

#body has children, get p tag
print(list(body.children))
#['n', <p>Here is some simple content for this page.</p>, 'n']
p = list(body.children)[1]

#get txt
p.get_text()
#get url
p.get('href')
re.findall('\d+',p.get('href'))
#get img
img = body.find("img")
desc = img['title']



#3 find all tags
soup.find_all('p')
soup.find_all('p')[0].get_text()
#find once
soup.find('p')


#search by class
soup.find_all('p', class_='outer-text')
soup.find_all(class_="outer-text")

#search by id
soup.find_all(id="first")

#search by css
'''
p a — tags tags
body p a — body tag tag.
html body — html body.
p.outer-text — tag with class=outer-text.
p#first — tag with id=first.
body p.outer-text — boy tag with tag class=outer-text.
'''
data = soup.select("div p")
print(data)

