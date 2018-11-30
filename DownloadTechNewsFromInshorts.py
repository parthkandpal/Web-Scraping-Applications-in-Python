'''

Author: Parth kandpal

This is a Web Scraping Application which download all Tech ralated news from https://inshorts.com/

Inshorts is a news app that selects latest and best news from multiple national and international sources and summarises them
to present in a short and crisp 60 words or less format.

This Script downloads News in form of Headlines and Shorts and prints them.
This Script also stores Tech News in a CSV File so that it can be read later.
'''






import requests,bs4,csv

res=requests.get("https://inshorts.com/en/read/technology")
soup=bs4.BeautifulSoup(res.text)


csv_file=open("inshorts Tech for today.csv", 'w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Headlines','Shorts'])


Headlines=list()
Bodies=list()

CardStack= soup.find("div", class_="card-stack")
# print(CardStack.prettify())
for Headline in CardStack.find_all("span",itemprop="headline"):

    Headlines.append(Headline.text)
for Body in CardStack.find_all("div", itemprop="articleBody"):

    Bodies.append(Body.text)

for i in range(len(Headlines)):
    print("Headline")
    print(Headlines[i],'\n')
    print("Body")
    print(Bodies[i],'\n')

    csv_writer.writerow([Headlines[i].encode("utf-8"),Bodies[i].encode("utf-8")])

csv_file.close()


