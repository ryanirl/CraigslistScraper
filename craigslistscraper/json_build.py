# todo: work on documenting and variable names

#import craigslistscraper.domain as domain
#import craigslistscraper.scraper as scraper

from craigslistscraper import domain, scraper

import multiprocessing
import concurrent.futures
import os
from time import strftime
import json

class JsonProcessor:
    """
    JsonProcessor takes in 3 arguments, the domains that are being 
    searche along with the cities, and a string of whats being searched.
    
    The idea is to build a json file with the following structure:
    
    {search_dictionary: {
        city_dictionary: {
            name_dictionary: {

            [ad information]

            }
        }
    }    

    For all searches defined in main, and all cities defined in cities.csv

    The following file structure is formed
    /data/'todays date'/file_name.json

    Where the file_name is the name if the search followed by todays time 
    and date seperated by a '-'
    """

    def __init__(self, domains, cities, search):
        self.domains = domains
        self.cities = cities
        self.search = search
        self.search_dictionaries = {self.search: {}}

    def json_multiprocessor(self):
        """
        Defines time and date for the creation of data files.

        Runs json_data() on multiple processors allowing for a faster
        scraping of each ad page. Each process passes along the city_dictionary
        compiled in json_data and then wraps that dictionary into the larger
        search_dictionary and dumps the dictionary into a file for each search
        ran in main

        """

        # Used for naming json file
        current_time = strftime('%d:%b:%Y-%H:%M:%S')
        current_date = strftime('%d-%b-%Y')
        
        try:
            os.mkdir('data')
        
        except FileExistsError:
            pass

        path = 'data/{}'.format(current_date)

        try:
            os.mkdir(path)

        except FileExistsError:
            pass

        with concurrent.futures.ProcessPoolExecutor() as executor:
            city_dictionaries = executor.map(self.json_data, self.domains, self.cities)

            for city_dictionary in city_dictionaries:
                print(city_dictionary)

                self.search_dictionaries[self.search].update(city_dictionary)

                with open('data/{}/{}_{}.json'.format(current_date, self.search, current_time), 'w') as f:
                    json.dump(self.search_dictionaries, f, indent=2)


    def json_data(self, domain, city):
        """
        Defines city_dictionary and runs the scraper and compiles
        posting_titles, prices, ad_hrefs, and posting_details then
        passes them into name_dictionary.

        name_dictionaries is hen placed inside of city_dictionary for 
        each city in self.cities and returns city_dictionary.

        """

        city_dictionary = {city[0]: {}}        

        SEARCH = scraper.CraigslistSearches(domain)

        posting_titles = SEARCH.posting_title()
        prices = SEARCH.price()
        ad_hrefs = SEARCH.ad_href()
        posting_details, descriptions = SEARCH.posting_details()

        for posting_title, price, url, itter in zip(posting_titles, prices, ad_hrefs, range(len(posting_titles))):

            name_dictionaries = {posting_title: {'price': price, 'url': url}} # removed ''model': None' from the end

            for item in posting_details[itter]:
                if len(item) == 2:
                    name_dictionaries[posting_title].update({item[0]: item[1]})
                else:
                    name_dictionaries[posting_title].update({'model': item[0]})

            city_dictionary[city[0]].update(name_dictionaries)
            

        return city_dictionary










