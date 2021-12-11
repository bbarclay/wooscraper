""" 
1. get links from https://www.jordanusd.net/wp-sitemap-posts-product-1.xml 
"""
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url = 'https://www.jordanusd.net/wp-sitemap-posts-product-1.xml'

response = requests.get(url)

#parse reponse get urls put in list print list
soup = BeautifulSoup(response.text, 'html.parser')

urls = []

for link in soup.find_all('loc'):
    urls.append(link.text)

#loop through list and request each url
#use try except to catch errors that are not redirects or 200
#build a catalog of all the products and their info from woocommerce page
#find price, description, image, etc.
#price has compare at and price under price-wrapper
#description has a class of of info-content std
#image has a class of product-images
#get variants and sizes under variations
#woocommerce-review-link has a class of woocommerce-review-link get count
#get reviews and ratings

#write a function to clean html

info = []
count = 0
for url in urls:
    try:
        count += 1
        #after count = 5 exit loop
        if count == 5:
            break

        #print url with a new line
        #print('url =========== ' + url + '\n')
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        #get price
        price = soup.find('span', class_='price').text
        #get description
        # print(price)
        description = soup.find('div', class_='info-content').text
        # print('description' + description)

        description2 = soup.find('div', class_='woocommerce-Tabs-panel--description').text
        # print('description2' + description2)

        attribute = soup.find('div', class_='woocommerce-product-attributes-item__value')
        # print(attribute)

        #extract all option values from dropdowns and print
        #get all dropdowns
        dropdowns = soup.find_all('select')
        # print(dropdowns)

        #get image inside woocommerce-product-gallery__image class
        image = soup.find('img', class_='woocommerce-product-gallery__image')
        # print(image)
        #get variants
        variants = soup.find('div', class_='variations')
        # print(variants)
        #get reviews
        reviews = soup.find('div', class_='woocommerce-review-link')
        # print(reviews)
        #get ratings
        ratings = soup.find('div', class_='star-rating').text
        # print(ratings)

        #put all info into an array
        info.append([price, description, description2, image, variants, reviews, ratings, dropdowns, attribute, url])
    except:
        print('error')
        continue
#convert array as dataframe

df = pd.DataFrame(info, columns=['price', 'description', 'description2', 'image', 'variants', 'reviews', 'ratings', 'dropdowns', 'attribute', 'url'])   

#escape commas so they don't mess up csv

#/Users/brandon/woocommercescraper/woocommercescraper.tsv
#df.to_csv('/Users/brandon/woocommercescraper/woocommercescraper.tsv', sep='\t', index=False)

"""
1. attach google drive and save as tsv
"""
