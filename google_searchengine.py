'''this program is helpful for web scraping and easy way to extract the detail of the 
any site without copy the url of a site'''
from googlesearch import search

data = input("enter your search : ")

for i in search(data,10,advanced= True):
    print(i.url)
    print(i.title)
    print(i.description)
    print()
