import csv
import pkg_resources

def domain_builder(search, section, filters, cities): 
    """
    Return 0: Array of domains
    Return 1: Array of cities
    
    Builds the Craigslist URL's for each city in 'city.csv'

    Some options for sorting your craigslist are found below,
    more options can be found in readme.txt and the rest can
    be found simply by going on craigslist.

    Section: 'sss' = all
             'cta' = cars all
             'cto' = cars owner
             'syp' = computer parts
             'sya' = computers
             'ela' = electronics
             'zip' = free stuff
    """

    domains = []
    cities_list = []

    domain_section = section
    domain_search = '?query={}'.format(search)

#    DATA_PATH = pkg_resources.resource_filename('craigslistscraper', 'city_data/cities_compile.csv')

#    with open(DATA_PATH) as csv_file:
#        cities = csv.reader(csv_file)

    for city in cities:
        domains.append('https://' + str(city) + '.craigslist.org/search/' + domain_section + domain_search + ''.join(filters))

        cities_list.append(city)
       
    print(domains, cities_list)
    return domains, cities_list






