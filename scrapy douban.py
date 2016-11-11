import requests
from bs4 import BeautifulSoup
import urllib.request
import re
import pandas as pd
name_vector=[]
rating_num_vector=[]
pop_vector={}
values=[]
for k in range(0,250,25):
   url="https://movie.douban.com/top250?start="+str(k)+"&filter="
   req=requests.get(url)
   req.encoding="utf-8"
   soup=BeautifulSoup(req.text,"lxml")
   name=soup.find_all("span",{"class":"title"})
   rating_num=soup.find_all("div",{"class":"star"})
   pop=soup.select(" span")

   for i in name:
       if "\xa0/\xa0" not in i.text:
           name_vector.append(i.text)
   for j in rating_num:
       rating_num_vector.append(j.text.replace("\n"," "))
   for i,j in zip(name_vector,rating_num_vector):
       pop_vector[i]=j
items=pop_vector.values()
for i in items:
    values.append(i)
values.sort(reverse=True)
#print(values)
movie=pd.DataFrame()
movie['name']=pop_vector.keys()
movie['rating_num']=pop_vector.values()
movie=movie.sort_values(by='rating_num',ascending=False)

print(movie)
movie.to_csv("D:/douban250.csv")
"""
def fetch_movie(url):
url="https://movie.douban.com/top250?start="+str(i)+"&filter="
for i in range(0,250,25):

"""
