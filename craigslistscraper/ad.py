from bs4 import BeautifulSoup
import requests
import re

from typing import Optional
from typing import Union
from typing import List
from typing import Dict

from .utils import format_price


class Ad:
    def __init__(
        self, 
        url: str, 
        price: Optional[float] = None, 
        title: Optional[str] = None, 
        d_pid: Optional[int] = None,
        description: Optional[str] = None,
        attributes: Optional[Dict] = None,
        image_urls: Optional[List[str]] = None
    ) -> None:
        """An abstraction for a Craigslist 'Ad'. At the bare minimum you need a
        `url` to define an ad. Although, at search-time, information such as the
        price, title, and d_pid can additionallly be computed. If not provided,
        these are computed lazily if the user fetches the ad information with 
        `ad.fetch()`.

        """
        self.url = url
        self.price = price
        self.title = title
        self.d_pid = d_pid
        self.description = description
        self.attributes = attributes
        self.image_urls = image_urls

    def __repr__(self) -> str:
        if (self.title is None) or (self.price is None):
            return f"< {self.url} >"

        return f"< {self.title} (${self.price}): {self.url} >"

    def fetch(self, **kwargs) -> int:
        """Fetch additional data from the url of the ad."""
        self.request = requests.get(self.url, **kwargs)
        if self.request.status_code == 200:
            parser = AdParser(self.request.content)
            self.price = parser.price
            self.title = parser.title
            self.d_pid = parser.d_pid
            self.description = parser.description
            self.attributes = parser.attributes
            self.image_urls = parser.image_urls
            self.metadata = parser.metadata

        return self.request.status_code

    def to_dict(self) -> Dict:
        return {
            "url": self.url,
            "price": self.price,
            "title": self.title,
            "d_pid": self.d_pid,
            "description": self.description,
            "image_urls": self.image_urls,
            "attributes": self.attributes,
        }


def fetch_ad(url: str, **kwargs) -> Ad:
    """Functional way to fetch the ad information given a url."""
    ad = Ad(url = url)
    ad.fetch(**kwargs)
    return ad


class AdParser:
    def __init__(self, content: Union[str, bytes], **kwargs) -> None:
        self.soup = BeautifulSoup(content, "html.parser", **kwargs)

        # Remove QR text. This is important when parsing the description. 
        for qr in self.soup.find_all("p", class_ = "print-qrcode-label"):
            qr.decompose()

    @property
    def url(self) -> str:
        return self.soup.find("meta", property = "og:url")["content"] 

    @property
    def price(self) -> float:
        return format_price(self.soup.find("span", class_ = "price").text)

    @property
    def title(self) -> str:
        return self.soup.find("span", id = "titletextonly").text

    @property
    def d_pid(self) -> int:
        return int(re.search(r"/(\d+)\.html", self.url).group(1))

    @property
    def description(self) -> str:
        return self.soup.find("section", id = "postingbody").text

    @property
    def attributes(self) -> Dict:
        attrs = {}
        for attr_group in self.soup.find_all("p", class_ = "attrgroup"):
            for attr in attr_group.find_all("span"):
                kv = attr.text.split(": ") 

                # Add the attribute if and only if it's a key value attribute.
                if len(kv) == 2: attrs[kv[0]] = kv[1]

        return attrs

    @property
    def image_urls(self) -> List[str]:
        return [a.get("href") for a in self.soup.find_all("a", class_ = "thumb")]

    @property
    def metadata(self) -> List[BeautifulSoup]:
        return self.soup.find_all("meta")


