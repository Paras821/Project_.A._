
import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    db = client['Riot']
    
    col = db['Streets']

    query = {'Location' : 'Mumbai'}

    doc = col.find(query)

    for x in doc:
        print(x)

