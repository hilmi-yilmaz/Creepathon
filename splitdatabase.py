from pymongo import MongoClient

client = MongoClient(port=27017)
db = client.get_database('test')
collection = db.get_collection('venmo')
collection.aggregate([{'$match': {"payment.target.user.first_name": 'Jason'}}, {'$out': "Jasons"}])
# collection.aggregate([{'$match': {"comments": 'Jason'}}, {'$out': "Jasons"}])
# collection.aggregate(
# 		{$group: {
# 				_id: {
# 				month: {$month: "$entryTime"},
# 				year: {$year:  "$entryTime"}
# 			}},
# 				total: {$sum: "$expenseAmount"}
# 			}})
