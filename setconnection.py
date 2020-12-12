from pymongo import MongoClient
import pandas as pd
import sys


# In order to display all the columns in the same line, rather than splitting them under each other, we set options on pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('max_columns', None)
pd.set_option("max_colwidth", 0)
pd.set_option("max_seq_item", None)


def _connect_mongo(host, port, username, password, db):
	""" A util for making a connection to mongo"""

	# For us, we don't need a username and password, but if you did, here's how
	if username and password:
		mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
		conn = MongoClient(mongo_uri)
	else:
		conn = MongoClient(host, port)

	return conn[db]


def aggregate_collection(arg, db='test', collection='venmo', host='localhost', port=27017, username=None, password=None, no_id=True):
	""" Unsorted data is so messy, that's why we can aggregate it into more useful smaller parts"""

	db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)

	collection = db.get_collection(collection)

	# We set up a few default aggregations
	collection.aggregate([{'$match': {"payment.target.user.first_name": 'Jason'}}, {'$out': "Jasons"}])


def read_mongo(db='test', collection='venmo', query={}, host='localhost', port=27017, username=None, password=None, no_id=True):
	""" Read from Mongo and Store into DataFrame"""

	# Let's set up a connection to the mongoDB server we host on our own machine.
	db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)

	# Make a query to the specific Database and collection
	# For testing purposes, we limit the response to 10000
	cursor = db[collection].find(query).limit(10000)

	# Expand the cursor and construct the DataFrame
	df = pd.DataFrame(list(cursor))

	# Delete the _id
	if no_id:
		del df['_id']

	return df


print(sys.argv[0])
print(len(sys.argv))
if len(sys.argv) > 2 and sys.argv[1] == 'aggregate':
	# Right now we don't want to print the dataset, but we want to aggregate (i.e. split) it
	aggregate_collection(sys.argv[2])

else:
	if len(sys.argv) > 2:
		dataframe = read_mongo(sys.argv[1], sys.argv[2])
	else:
		dataframe = read_mongo()

	# To get a feel for what the data looks like, we take a sneak peek at the first (10) results
	print(dataframe.head(10))

