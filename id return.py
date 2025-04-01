
import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    db = client['Riot']
    
    col = db['Streets']
    
    insertThese = [
        {'_id' : 1, 'Name' : 'Mahi', 'Location' : 'Mumbai', 'Marks' : '44'},
        {'_id' : 2, 'Name' : 'Dev', 'Location' : 'Surat', 'Marks' : '40'},
        {'_id' : 3, 'Name' : 'Ali', 'Location' : 'Delhi', 'Marks' : '48'},
        {'_id' : 4, 'Name' : 'Asees', 'Location' : 'Banglore', 'Marks' : '46'}
    ]
    
    #col.insert_one(insertThese)
    col.insert_many(insertThese)
    print("Inserted Successfully")

