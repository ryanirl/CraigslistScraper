# add documentation and refactor

import domain
import scraper
import json_build



class Searches:
    """
    Class purpose is for reusability of searches.
    """

    def __init__(self, search, section='sss'):
        self.search = search
        self.section = section
        self.domains, self.cities = domain.domain_builder(search, section)
    
    def compile_search(self):
        """
        Compiles JsonProcessor for search.
        """
        
        SEARCH = json_build.JsonProcessor(self.domains, self.cities, self.search)
    
        SEARCH.json_multiprocessor()











