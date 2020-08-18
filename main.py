from craigslistscraper import Searches
import time


def main():
    """
    Define searches here, a few examples are given below.

    search_name = searches.Searches('your search', 'section')

    default section is 'sss' which is all of craigslist.
    """
    
    cities = ['minneapolis', 'austin']
    filters = ['&postedToday=1']

    # some examples of what can be done
    bmw_search = Searches('bmw', cities, 'cto', filters)
#    audi_search = Searches('audi', 'cto', filters)
#    iphone_search = Searches('iphone', 'ela', filters)

    bmw_search.compile_search()
#    audi_search.compile_search()
#    iphone_search.compile_search()



if __name__ == '__main__':
    main()
    print(time.perf_counter())




