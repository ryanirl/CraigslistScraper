from bs4 import BeautifulSoup
import requests
import re

from typing import Union
from typing import List
from typing import Dict

from .ad import Ad
from .utils import format_price
from .utils import build_url


class Search:
    def __init__(self, query: str, city: str, category: str = "sss") -> None:
        """An abstraction for a Craigslist 'Search'. Similar to the 'Ad' this is
        also lazy and follows the same layout with the `fetch()` and `to_dict()`
        methods. 

        """
        self.query = query
        self.city = city
        self.category = category

        self.url = build_url(self.query, self.city, self.category)
        self.ads: List[Ad] = []

    def fetch(self, **kwargs) -> int: 
        self.request = requests.get(self.url, **kwargs)
        if self.request.status_code == 200:
            parser = SearchParser(self.request.content)
            self.ads = parser.ads

        return self.request.status_code

    def to_dict(self) -> Dict:
        return {
            "query": self.query,
            "city": self.city,
            "category": self.category,
            "url": self.url,
            "ads": [ad.to_dict() for ad in self.ads]
        }


def fetch_search(query: str, city: str, category: str = "sss", **kwargs) -> Search:
    """Functional implementation of a Craigslist search."""
    search = Search(query = query, city = city, category = category)
    search.fetch(**kwargs)
    return search


class SearchParser:
    def __init__(self, content: Union[str, bytes], **kwargs) -> None:
        self.soup = BeautifulSoup(content, "html.parser", **kwargs)

    @property
    def ads(self) -> List[Ad]:
        ads = []
        for ad_html in self.soup.find_all("li", class_ = "cl-static-search-result"):
            url = ad_html.find("a")["href"]
            title = ad_html.find(class_ = "title").text
            price = format_price(ad_html.find(class_ = "price").text)
            d_pid = int(re.search(r"/(\d+)\.html", url).group(1))

            ads.append(
                Ad(
                    url = url,
                    title = title,
                    price = price,
                    d_pid = d_pid
                )
            )

        return ads


