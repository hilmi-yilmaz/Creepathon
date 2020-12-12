from pymongo import MongoClient

client = MongoClient(port=27017)
db = client.get_database('test')
collection = db.get_collection("venmo")
print(collection)
for i in enumerate(db[collection].find()):
	# if i % 10000 == 0:
	print(i)