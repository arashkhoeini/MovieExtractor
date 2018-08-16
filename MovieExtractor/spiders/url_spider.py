import scrapy
import pandas as pd
import os
from urllib.parse import parse_qs

class URLSpider(scrapy.Spider):
    name ='url'

    def start_requests(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        movies_dir = os.path.join(current_dir,'..','data' , 'movies.dat')
        movies = pd.read_csv(movies_dir, sep='::', names=['id','name', 'genre'])
        movies = movies.head()
        for movie in movies.iterrows():
            url = 'https://www.imdb.com/find?q='+movie[1]['name']
            url += "&name="+movie[1]['name']
            url += "&id="+str(movie[1]['id'])
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        url = response.css('table.findList tr td.result_text a::attr(href)').extract_first()
        full_movie_url = 'https://www.imdb.com'+url
        params = parse_qs(response.url)
        yield {"id":params['id'] , "name":params['name'] , "url":full_movie_url }
