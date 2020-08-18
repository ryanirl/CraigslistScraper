from craigslistscraper import domain

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

 
class CraigslistSearches:
    """
    Object that pulls all relevent ad information and returns them
    in arrays to be parsed to a JSON file.
    """

    def __init__(self, domain_get):
        self.page = requests.get(domain_get)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

    def posting_title(self):  
        """
        Retuns the Posting Title of the ad in the form of a string.
        """

        posting_title_raw = self.soup.find_all(class_='result-title hdrlnk')

        posting_title = [item.get_text() for item in posting_title_raw]

        return posting_title 

    def price(self):  
        """
        Returns Price of ad in form $'price' with the dollar sign included.
        """

        prices_raw = self.soup.find_all(class_='result-meta')

        price = [item.find(class_='result-price').get_text() for item in prices_raw]

        return price

    def ad_href(self):  
        """
        Returns a sting of the link to an ad.
        """

        raw = self.soup.find_all(class_='result-row')

        ad_link_raw = [item.find('a') for item in raw]

        ad_link = [items.get('href') for items in ad_link_raw]

        return ad_link

    def posting_details(self): 
        """
        Retuns an array of all the Posting Details and Description in an array.
        """

        posting_details = []
        description = []

        for url in self.ad_href():
            ad_page = requests.get(url)
            soup = BeautifulSoup(ad_page.content, 'html.parser')

            ad_info = soup.select('span')
            data = []
            unorganized_data_info = []

            for info in ad_info:  # only keep elements that don't have a 'class' or 'id' attribute
                if not (info.has_attr('class') or info.has_attr('id')):
                    data.append(info)

            for d in data:
                unorganized_data_info.append(d.text.split(': '))
            
            description_raw = soup.find_all(id='postingbody')

            for item in description_raw:
                unfiltered = item.get_text(strip=True)
                description.append(unfiltered.strip('QR Code Link to This Post'))
            
            posting_details.append(unorganized_data_info)

        return posting_details, description
    
    def display(self):  
        """
        Displays data pulled from search in terminal, and 
        puts data into 'search_info.csv'.
        """

        data = pd.DataFrame( # Displays data
            {
                'Name:': self.name(),
                'Price:': self.price(),
                'HREF:': self.ad_href()
            })

        # Parses data into 'search_info.csv'
        data.to_csv('data/search_info.csv', index=False, mode='a')

        if data.empty is True:
            print('No Results')
        else:
            print(data)





