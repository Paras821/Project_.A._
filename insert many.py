
import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    db = client['Riot']
    
    col = db['Streets']
    
    insertThese = [
        {'Name' : 'Mahi', 'Location' : 'Mumbai', 'Marks' : '44'},
        {'Name' : 'Dev', 'Location' : 'Surat', 'Marks' : '40'},
        {'Name' : 'Ali', 'Location' : 'Delhi', 'Marks' : '48'},
        {'Name' : 'Asees', 'Location' : 'Banglore', 'Marks' : '46'}
    ]

    col.insert_many(insertThese)
    print("Inserted Successfully")

