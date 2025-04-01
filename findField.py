
import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    db = client['Riot']
    
    col = db['Streets']
    
    docs = col.find({'Name' : 'Asees'}, {'Name' : 1, '_id' : 0})   #.limit(1)
    #print(docs.count())
    
    for item in docs:
        print(item)

