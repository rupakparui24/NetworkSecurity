import os
import sys
import json
import numpy as np
import pandas as pd
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URI = os.getenv('MONGO_DB_URI')
print(MONGO_DB_URI)

import certifi
ca = certifi.where()

class NetworkDataExctract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_convertor(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, database, collection, records):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URI)
            self.database = self.mongo_client[self.database]
            self.collection= self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
if __name__ == '__main__':
    database = "RupakParuiML"
    file_path = "Network_Data\phisingData.csv"
    collection = "network_data"

    network_obj = NetworkDataExctract()
    records = network_obj.csv_to_json_convertor(file_path=file_path)
    print(len(records))
    number_of_records = network_obj.insert_data_mongodb(database, collection, records)
    print(number_of_records)
