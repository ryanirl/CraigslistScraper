
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='craigslistscraper',  
    version='1.0.0',  
    description='Webscraper for Craigslist',  
    long_description=long_description,  
    long_description_content_type='text/markdown', 
    url='https://github.com/ryanirl/CraigslistScraper',  
    download_url='https://github.com/ryanirl/CraigslistScraper/archive/v1.0.0-beta.tar.gz',
    author='Ryan Peters',
    author_email='ryanirl@icloud.com',  

    classifiers=[  
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='web scraper, python, data, development',  
    packages=find_packages(),  
    python_requires='>=3.5, <4',

    install_requires=['beautifulsoup4', 'requests', 'pandas'],  
    
    include_package_data=True,
#    package_data={  'cities_compile.csv': ['city_data/cities_compile.csv'],
#        'craigslist_cities_list.csv': ['city_data/craigslist_cities_list.csv']
#    },

#    data_files=[('city_data/cities_compile.csv', ['craigslistscraper/city_data/cities_compile.csv'])],

    project_urls={'Source': 'https://github.com/ryanirl/CraigslistScraper'},
)
