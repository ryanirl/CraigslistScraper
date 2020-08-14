#import craigslistscraper.searches as searches # new
#import craigslistscraper.Search
from craigslistscraper import Searches
import time


def main():
    """
    Define searches here, a few examples are given below.

    search_name = searches.Searches('your search', 'section')

    default section is 'sss' which is all of craigslist.
    """

    # some examples of what can be done
    bmw_search = Searches('bmw', 'cto')
    audi_search = Searches('audi', 'cto')
    iphone_search = Searches('iphone', 'ela')

    bmw_search.compile_search()
    audi_search.compile_search()
    iphone_search.compile_search()



if __name__ == '__main__':
    main()
    print(time.perf_counter())




