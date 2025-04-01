
import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    db = client['Riot']
    print("Database created successfully")

