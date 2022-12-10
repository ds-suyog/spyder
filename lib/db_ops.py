
from config.config import *
import lib.utils as utils
import os
import sys; sys.path.append(BASEDIR)
import json
from pymongo import MongoClient
from elasticsearch import helpers, Elasticsearch


class MongoOps:
    def getmongoclient(self, collname):
        try:
            myclient = MongoClient(MONGODB_HOST, MONGODB_PORT)
        except:
            pass
        mydb = myclient[BSE_DB]
        mycol = mydb[collname]
        return myclient, mydb, mycol

    def insert_one(self, data, colname):
        myclient, mydb, mycol = self.getmongoclient(colname)
        # import pdb; pdb.set_trace()
        if colname in mydb.list_collection_names(): mydb[colname].remove()
        for doc in data:
            try:
                result = mydb[colname].insert_one(doc)
            except Exception as e:
                pass

    def insert_many(self, data, colname):
        myclient, mydb, mycol = self.getmongoclient(colname)
        if colname in mydb.list_collection_names(): mydb[colname].remove()
        mycol.insert(data)

    def mongodumpjson(self, colname, filepath):
        myclient, mydb, mycol = self.getmongoclient(colname)
        cursor = mycol.find()
        with open (filepath, 'w', encoding="utf8") as f:
            docs = [doc for doc in cursor]
            json.dump(docs ,f)

    def mongoimportjson(self, colname, filepath):
        myclient, mydb, mycol = self.getmongoclient(colname)
        with open(filepath, 'r', encoding="utf8") as f:
            docs = json.load(f)
            for doc in docs:
                try:
                    result = mycol.insert_one(doc)
                except Exception as e:
                    pass

    def mongoimportbson(self, colname, filepath):
        myCmd = 'bsondump {} > {}'.format(filepath, filepath.replace('bson' ,'json'))
        os.system(myCmd)
        os.system('ls {}}/tmp/bse'.format(BASEDIR))
        self.mongoimportjson(colname, filepath.replace('bson' ,'json'))

class ElasticSearchOps:
    def bulk_insert(self, data, indexname, doctype):
        from elasticsearch import helpers, Elasticsearch
        es = Elasticsearch(['http://localhost:9200/'])
        temp = {'_index': indexname ,'_type': doctype}
        trending_bulk = list()
        for doc in data:
            del doc['_id']
            doc.update(temp)
            trending_bulk.append(doc)
        helpers.bulk(es, trending_bulk, chunk_size=1000, request_timeout=200)