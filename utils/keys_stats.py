import sys; sys.path.append('./')    # call from parent location
#sys.path.append('../')              # call from inside dir utils
from config import *
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

    def get_coll_keys_stats(self, dbname):          
        myclient, mydb = self.getmongoclient(dbname)    
        colls = mydb.list_collection_names()
        for collname in colls:
            self.get_keys_stats(dbname, collname)

    def get_keys_stats(self, dbname, collname):
        myclient, mydb = self.getmongoclient(dbname) 
        mycoll = mydb[collname]
        all_keys = set()
        all_keystypes = set()
        all_keysstats = set()
        table_data= list()

        cursor = mycoll.find()
        for doc in cursor:
            try:
                keys = set(doc.keys())
                all_keys = all_keys.union(keys)                
                keystypes = [{(str(k), str(type(v).__name__))} for k,v in doc.items()]
                for val in keystypes:
                    all_keystypes = all_keystypes.union(set(val))
            except Exception as e:
                pass
     
        all_keystypes = sorted(all_keystypes)
        for ky,typ in all_keystypes:
            cursor = mycoll.find()
            freq = sum([1 for doc in cursor if ky in doc])
            sample = None
            itercount = 0
            cursor = mycoll.find()
            for doc in cursor:
                itercount+=1
                if ky in doc:
                    sample = doc
                    all_keysstats.add((ky, typ, freq, str(sample)))
                    break
            table_data.append([ky, typ, freq, sample])            

        table_headrs = ["fieldname", "type", "frequency", "sample"]
        # import pdb; pdb.set_trace()
        with open(REPORT_KEYS_FPATH, 'a') as f:
            f.write("COLLECTION: {}".format(collname))
            f.write("\ntotal documents: {}".format(mycoll.count_documents({})))           
            f.write('\nkey stats: ')
            table = tabulate(table_data, headers=table_headrs, tablefmt='orgtbl')
            f.write("\n{}\n\n\n".format(table))  

  
def main():
    db = 'bse'
    gn = Generate()  
    with open(REPORT_KEYS_FPATH, 'w') as f:
        f.write("REPORT: database {} keys statistics".format(db))
        f.write("\n[time stamp] {}\n\n".format(datetime.now().strftime("%B %d, %Y  %H:%M:%S")))
    gn.get_coll_keys_stats(db)                    

if __name__ == '__main__':
    main()



