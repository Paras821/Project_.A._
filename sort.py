
import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")

    db = client['Riot']
    
    col = db['Streets']

    mydoc = col.find().sort('Name')     # a=1, d=-1

    for x in mydoc:
        print(x)

