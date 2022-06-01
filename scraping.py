import requests
from bs4 import BeautifulSoup
import pandas as pd

#insert the wesite url that will be scraped
req = requests.get("https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&sort=recency_desc&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkxhdGVzdCBTYW1zdW5nIG1vYmlsZXMgIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=1.productCard.PMU_V2_1")

soup = BeautifulSoup(req.content, "html.parser")

products = [] #list to store name of the product
prices = [] #list to store price of the product
ratings = [] #list to store rating of the product

#find the data and append data in respective list
name = soup.find_all("div", attrs={'class': '_4rR01T'})
for row in name:
    x = row.text
    products.append(x)
price = soup.find_all("div", attrs={'class': '_30jeq3 _1_WHN1'})
for row in price:
    y = row.text
    prices.append(y)
rating = soup.find_all("div", attrs={'class': '_3LWZlK'})
for row in rating:
    z = row.text
    ratings.append(z)
ratings.insert(0,'N/A')#ratings not available for the first itme

#output the data form of a csv file
df = pd.DataFrame({'Product Name':products,'price':prices,'Rating':ratings})
df.to_csv('Products.csv', index=False, encoding='utf-8')

print(df)


