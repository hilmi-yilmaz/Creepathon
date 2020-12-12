from pymongo import MongoClient

client = MongoClient(port=27017)
db = client.get_database('test')
coll = db.list_collection_names()
collection = db.get_collection("newcoll")
# print(collection)
for i, line in enumerate(collection.find()):
#	print(line)
#	if i > 1000:
	#	break
	print(i)
