# add documentation and refactor

#import craigslistscraper.domain as domain
#import craigslistscraper.scraper as scraper 
#import craigslistscraper.json_build as json_build

from craigslistscraper import domain, scraper, json_build


class Searches:
    """
    Class purpose is for reusability of searches.
    """

    def __init__(self, search, section='sss', filters=['postedToday=1']):
        self.search = search
        self.section = section
        self.domains, self.cities = domain.domain_builder(search, section, filters)
    
    def compile_search(self):
        """
        Compiles JsonProcessor for search.
        """
        
        SEARCH = json_build.JsonProcessor(self.domains, self.cities, self.search)
    
        SEARCH.json_multiprocessor()











