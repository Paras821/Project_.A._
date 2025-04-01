
import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    db = client['Riot']
    
    col = db['Streets']

    prev = {'Name' : 'Asees'}
    next = {'$set' : {'Location' : 'Chandigarh'}}
    col.update_many(prev, next)
    #print(.modified_count())
    print("Updated successfully")

