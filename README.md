# Intelligent SpyderBot #   

#### Author: Suyog K Sethia ####                      
I have taken up this old work again to create version 2.

## What SpyderBot does? ##
1. Picks job from queue, crawls webpages for stocks, parses crawled webpages, and generates 'tabular' report.   
2. App scraps top 5 gainers, top 5 loosers, and trending stocks from Bombay Stock Exchange(BSE)    
3. App processes database collection's keys statistics, and generates tabular report to respective clients.        

## Workflow: ##
1. app creates and auto-syncs jobs  (implemented both handmade job-queue and redis job-queue) 
2. app processes jobs in background with workers through multithreading or multiprocessing (choice provided)
3. app's job-queue dashboard: rq-dashboard
4. app stores respective logs for information and debugging purposes
5. app inserts data in mongodb respective collections. I wrote modules to automatically generate and receive data-dumps in both .json and .bson format.
6. app can store store data in Elasticsearch indexes.
7. app generates report for stocks - trending, gainers, loosers.
8. app generates collection's keys statistics too.     
9. Advanced features are in pipeline for version 2.  


## To run  ##
setup virtual environment,
```
$source venv/bin/activate
```

install dependencies,
```
$pip install -r requirements.txt
```

### Note: webscrapper is for experiment purpose         ###



