
import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    db = client['Riot']
    
    col = db['Streets']

    prev = {'Name' : 'Asees'}
    next = {'$set' : {'Location' : 'Chandigarh'}}
    col.update_one(prev, next)
    print("Updated successfully")

