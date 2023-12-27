# Multiprocessing example with multiple cities for a single search.
from concurrent.futures import ThreadPoolExecutor
import craigslistscraper as cs
import time

query = "bmw e46"
cities = [
    "minneapolis",
    "sfbay",
    "portland"
]

delay = 1.0 # Time to delay between each request (in seconds)
max_workers = 2 # Max threads

# Define the list of searches (lazily!)
searches = []
for city in cities: 
    searches.append(
        cs.Search(
            query = "bmw e46",
            city = city,
            category = "cto"
        )
    )


def worker_thread(search: cs.Search) -> None:
    """The function that will do work (including fetching) for each search."""
    status = search.fetch() # Fetch the html data.
    if status != 200:
        print(f"Unable to fetch search at city {city} with status <{status}>.")
        return

    print(f"Number of ads found at {search.city}: {len(search.ads)}")


with ThreadPoolExecutor(max_workers = max_workers) as executor:
    for search in searches:
        executor.submit(worker_thread, search = search)

        if delay > 0:
            time.sleep(delay)

