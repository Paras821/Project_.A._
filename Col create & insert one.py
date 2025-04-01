
import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    db = client['Riot']
    
    col = db['Streets']
    dictionary = {'Name' : 'Mahi', 'Marks' : '45'}
    col.insert_one(dictionary)
    print("Collection created successfully")

