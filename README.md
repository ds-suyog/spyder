# Intelligent Spyder #   

#### Author: Suyog Kumar Sethia ####                      
Currently version 2 upgrades are parked.  
You may refer LICENSE.md for info regarding usage.    

## What Spyder does? ##
1. Picks job from queue, crawls webpages for stocks, parses crawled webpages, and generates 'tabular' report.   
2. App scraps top 5 gainers, top 5 loosers, and trending stocks from Bombay Stock Exchange(BSE)    
3. App processes database collection's keys statistics, and generates tabular report.        
4. [In pipelinea] db optimization
5. [In pipeline] dashboarding and reporting
6. [In pipeline] stock analytics
7. [In pipeline] model and autoML

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


## Set-up ##
Just calling script create_venv.sh creates python virtual environment at parent location of spyder, by using requirements.txt provided in config.
```
$bash create_venv.sh
```

## Trigger or schedule workflow  ##
Automation: Workflow is triggered by calling auto_webscrap.sh or it can be scheduled via crontab or other means. Script will automatically activate venv, run workflow, and then deactivate venv. Script can automatically trigger virtual network also and shut it down in the end too.
```
$bash auto_webscrap.sh
```

Manual Trigger: Create venv from requirements.txt provided in config, and call script trigger_webscrap.sh.  
```
$bash trigger_webscrap.sh
```

Workflow modes: There are multiple workflow modes, which can be set in trigger_webscrap.sh.



