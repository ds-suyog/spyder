import sys; sys.path.append('./')    # call from parent location
#sys.path.append('../')              # call from inside dir utils
from config.config import *
import sys; sys.path.append(BASEDIR)
from pymongo import MongoClient
from datetime import datetime
from tabulate import tabulate

class Generate:
    def getmongoclient(self, dbname):
        try: 
            myclient = MongoClient(MONGODB_HOST, MONGODB_PORT, unicode_decode_error_handler='ignore') 
        except:   
            pass
        mydb = myclient[dbname]
        return myclient, mydb

    def all_coll_report(self, dbname):
        myclient, mydb = self.getmongoclient(dbname)    
        colls = mydb.list_collection_names()     
        for collname in colls:
            self.single_coll_report(dbname, collname)

    def single_coll_report(self, dbname, collname):
        myclient, mydb = self.getmongoclient(dbname) 
        mycol = mydb[collname]
        cursor = mycol.find()
        if collname == 'gainers':
            tab_headers = list(('id','Rank', 'Name', 'LTP (₹)', 'Change', '% Change'))        
            table_data = []
            for i,doc in enumerate(cursor):
                # import pdb; pdb.set_trace()
                table_data.append([doc['_id'], i+1, doc['Security'], doc['LTP (₹)'], doc['Change'], doc['% Ch.']])
            table = tabulate(table_data, headers=tab_headers, tablefmt='orgtbl')
            with open(REPORT_BSE_FPATH, 'a') as f:
                f.write("COLLECTION: {}\n{}\n\n".format(collname, table))
        elif collname == 'loosers':
            tab_headers = list(('id','Rank', 'Name', 'LTP (₹)', 'Change', '% Change'))          
            table_data = []
            for i,doc in enumerate(cursor): 
                # import pdb; pdb.set_trace()
                table_data.append([doc['_id'], i+1, doc['Security'], doc['LTP (₹)'], doc['Change'], doc['% Change']])
            table = tabulate(table_data, headers=tab_headers, tablefmt='orgtbl')
            with open(REPORT_BSE_FPATH, 'a') as f:
                f.write("COLLECTION: {}\n{}\n\n".format(collname, table))
        elif collname == 'trending':
            tab_headers = list(('id', 'Name'))          
            table_data = []
            for i, doc in enumerate(cursor): 
                table_data.append([doc['_id'], doc['name']])
            table = tabulate(table_data, headers=tab_headers, tablefmt='orgtbl')
            with open(REPORT_BSE_FPATH, 'a') as f:
                f.write("COLLECTION: {}\n{}\n\n".format(collname, table))

def main():
    gn = Generate()  
    with open(REPORT_BSE_FPATH, 'w') as f:
        f.write("REPORT: BSE Trending, top 5 Gainers, top 5 Loosers")
        f.write("\n[time stamp] {}\n\n".format(datetime.now().strftime("%B %d, %Y  %H:%M:%S")))        

    gn.all_coll_report(BSE_DB)    

if __name__ == '__main__':
    main()



