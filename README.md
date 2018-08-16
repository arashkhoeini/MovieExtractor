# MovieExtractor
Simple tool to extract IMDB URL of MoveLens dataset movies

This is a Scrapy project to fetch IMDB URL of MovieLens 1m dataset movies. 

After installing requirements, you can run the project by running: 

scrapy crawl url -o urls.json

This command will save a json array in urls.json which contains Movielens id, movie name, and IMDB URL. 
