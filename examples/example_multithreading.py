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

# Time to delay before requests (in seconds)
delay = 1.0

# Max threads
max_workers = 2

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
    search.fetch() # Fetch the html data.
    print(f"Number of ads found at {search.city}: {len(search.ads)}")


with ThreadPoolExecutor(max_workers = max_workers) as executor:
    for search in searches:
        executor.submit(worker_thread, search = search)

        if delay > 0:
            time.sleep(delay)

