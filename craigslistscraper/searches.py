from craigslistscraper import domain, scraper, json_build


class Searches:
    """
    Class purpose is for reusability of code.
    """

    def __init__(self, search, cities, section='sss', filters=['&postedToday=1']):
        self.search = search
        self.section = section
        self.domains, self.cities = domain.domain_builder(search, section, filters, cities)
    
    def compile_search(self):
        """
        Runs JsonProcessor 
        """
        
        SEARCH = json_build.JsonProcessor(self.domains, self.cities, self.search)
    
        SEARCH.json_multiprocessor()











