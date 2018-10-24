'''

@Author: Parth Kandpal
Title: "Popular Tech News Downloader"
Description:

A Web Scraping Application to Download all popular Tech news from Gadgets.NDTV.com and save them to a CSV file News.CSV
It can be scheduled on daily basis, hourly or as you wish.(By default it is 10:00 o'clock every day

'''
import requests
from bs4 import BeautifulSoup
import schedule,time
import csv



def get_news():
    res=requests.get("https://gadgets.ndtv.com/")               #Creating a request
    soup=BeautifulSoup(res.text,'lxml')                          #Beautiful Soup
    csv_file= open("News.csv",'w')                              #Creating CSV file to Store Headlines with Articles
    csv_writer=csv.writer(csv_file)                              #Creating writer for CSV file

    csv_writer.writerow(['Headline','Article'])                 #First Row Created for Headline and Article



    division=soup.find('div',class_='nlist bigimglist')         #Popular Articles
    # print(division)

    URLList=[]
    for a in division.find_all('a',href=True):                  #fetched all the links
        # print(a['href'])
        url=a['href']
        URLList.append(url)                                     #All URLs Stored in a List

    # print(URLList)
    Headlines=[]
    Articles=[]

    for url in URLList:                                       #Parse through all the URL to get Article
        request=requests.get(url)
        soup=BeautifulSoup(request.text,'lxml')
        h1=soup.find('span', id='ContentPlaceHolder1_FullstoryCtrl_Stitle')               #will fetch h1 tag for heading
        Headline=h1.text
        Headlines.append(h1.text)                                                            #will store Headline

        Article_data=soup.find('div', class_='content_text row description')                #will fetch article  for heading
        Article=Article_data.text
        Articles.append(Article_data.text)                                                   #will store Article

        csv_writer.writerow([Headline,Article])                                             #Storing all articles in CSV File



    print("--------------Here are the Headlines for you.-----------------------\n")
    for Headline in Headlines:
        print("------Headline-----\t",Headline,"\t")


    print("\n")

    print("----------------And now Articles Here--------------------\n")
    for Article in Articles:

            print("----Article------\t", Article, "\n")


    print("\n")

    csv_file.close()


schedule.every().day.at("10:00").do(get_news)                #Scheduling the job for every day at 10:00

while True:
    schedule.run_pending()
    time.sleep(1)







