
import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print("Databases: \n ", client.list_database_names())

