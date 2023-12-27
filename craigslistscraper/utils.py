from urllib.parse import quote
import json
import os

from typing import List
from typing import Dict

# Get the directory of the current file agnositc of library location.
cs_dir = os.path.dirname(os.path.abspath(__file__))


def format_price(price: str) -> float:
    return float(price.replace("$", "").replace(",", ""))


def build_url(query: str, city: str, category: str = "sss") -> str:
    return f"https://{city}.craigslist.org/search/{category}?query={quote(query)}"


def get_areas() -> List[Dict]:
    with open(os.path.join(cs_dir, "data/areas.json"), "r") as file:
        areas = json.load(file)
    return areas


def get_categories() -> List[Dict]:
    with open(os.path.join(cs_dir, "data/categories.json"), "r") as file:
        categories = json.load(file)
    return categories


