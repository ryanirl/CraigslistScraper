import time
import domain
import scraper
import json_build
from searches import Searches
import searches


def main():
    """
    Define searches here, a few examples are given below.

    search_name = searches.Searches('your search', 'section')

    default section is 'sss' which is all of craigslist.
    """

    # some examples of what can be done
    bmw_search = searches.Searches('bmw', 'cto')
    audi_search = searches.Searches('audi', 'cto')
    iphone_search = searches.Searches('iphone', 'ela')

    bmw_search.compile_search()
    audi_search.compile_search()
    iphone_search.compile_search()



if __name__ == '__main__':
    main()
    print(time.perf_counter())




