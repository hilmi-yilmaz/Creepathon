from pymongo import MongoClient

client = MongoClient(port=27017)
collection = client.get_database('test').get_collection('venmo')
collection.aggregate([{'$match': {"payment.target.user.first_name": 'Jason'}}, {'$out': "Jasons"}])
