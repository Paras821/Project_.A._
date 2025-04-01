
import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")

    db = client['Riot']
    
    col = db['Streets']

    print("Collections: \n ", db.list_collection_names())

