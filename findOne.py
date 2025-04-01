
import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    db = client['Riot']
    
    col = db['Streets']
    
    one = col.find_one({'Name' : 'Asees'})
    print(one)

