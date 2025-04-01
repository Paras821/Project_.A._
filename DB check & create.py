
import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")

    dblist = client.list_database_names()

    if "Riot" in dblist:
        print("DB already exists")
    
    else:
        db = client['Riot']
        print("Database created successfully")
        print(client.list_database_names())

