import json
import csv

def key_constructor(json_file):
    '''
    Builds a list of keys in a JSON dictionary generated from CraigslistScraper
    '''
    
    keys = ['price', 'url']
    
    with open(json_file) as json_data:
        data = json.load(json_data)

    # Iterates over JSON dictionaries to ad_data
    for search in data:
        for city in data[search]:
            for ad in data[search][city]:
                for ad_data in data[search][city][ad]:
                    if ad_data not in keys:
                        keys.append(ad_data) # Adds all dictionary keys to keys variable

    return keys


def csv_from_json(keys, json_file):
    '''
    Creates a csv file taking in a list of possible keys which can be 
    constructed using key_constructor()

    The reason it needs the list of keys is so it can match up values 
    with keys and fill in empty spaces.
    '''

#    # Used for naming JSON file
#    current_time = strftime('%d:%b:%Y-%H:%M:%S')
#    current_date = strftime('%d-%b-%Y')
#    
#    try: # Checks to see if 'data' file has been created yet.
#        os.mkdir('data')
#    except FileExistsError:
#        pass
#
#    path = 'data/{}'.format(current_date)
#
#    try: # Checks if the file for 'current_date' has been created or not.
#        os.mkdir(path)
#    except FileExistsError:
#        pass

    with open(json_file) as json_data:
        data = json.load(json_data)

    csv_file = open('csvfile.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(keys)

    for search in data:
        for city in data[search]:
            for ad in data[search][city]:
                build_line = [] 

                for key, itter in zip(keys, range(len(keys))):
                    try:
                        build_line.append(data[search][city][ad][key])

                    except KeyError:
                        build_line.append('')
                        continue

                csv_writer.writerow(build_line)

    csv_file.close()

    

csv_from_json(key_constructor('evenbiggerdata.json'), 'evenbiggerdata.json')

