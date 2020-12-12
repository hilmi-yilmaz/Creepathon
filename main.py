from pymongo import MongoClient
import pandas as pd
from bson import json_util

def _connect_mongo(host, port, username, password, db):
	""" A util for making a connection to mongo"""

	if username and password:
		mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
		conn = MongoClient(mongo_uri)
	else:
		conn = MongoClient(host, port)

	return conn[db]


def read_mongo(db, collection, query={}, host='localhost', port=27017, username=None, password=None, no_id=True):
	""" Read from Mongo and Store into DataFrame"""

	db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)

	# Make a query to the specific Database and collection
	cursor = db[collection].find(query).limit(10000)
	print("after cursor")
	# Expand the cursor and construct the DataFrame
	df = pd.DataFrame(list(cursor))
	print("after pd.dataframe")

	# Delete the _id
	if no_id:
		del df['_id']

	return df


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('max_columns', None)
dataframe = read_mongo('test', 'Jasons')
print(dataframe.columns)

print(dataframe.head(10))

# print(dataframe)
