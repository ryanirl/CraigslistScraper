import craigslistscraper as cs
import json


# Define the search. Everything is done lazily, and so the html is not fetched
# at this step.
search = cs.Search(
    query = "honda",
    city = "minneapolis",
    category = "cto"
)

# Define the filters
filters = {
    "postedToday": 1,
    "bundleDuplicates": 1,
    "max_price": 5000
}

# This is the step that will fetch the html from the server. Notice that the
# filters are passed in through the requests.get(params = ...) argument.
search.fetch(params = filters)

for ad in search.ads:
    # We fetch additional information about each ad.
    ad.fetch()

    # There is a to_dict() method for convenience. 
    data = ad.to_dict()

    # json.dumps is merely for pretty printing. 
    print(json.dumps(data, indent = 4))


