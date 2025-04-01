
import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")

    db = client['Riot']

    collist = db.list_collection_names()

    if "Streets" in collist:
        print("Collection already exists")
    
    else:
        col = db['Streets']
        dictionary = {'Name' : 'Mahi', 'Marks' : '45'}
        col.insert_one(dictionary)
        print("Collection created successfully")
        print(db.list_collection_names())

