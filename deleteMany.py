
import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    db = client['Riot']
    
    col = db['Streets']

    rec = {'Name' : 'Dev'}
    col.delete_many(rec)
    #print(.delete_count())
    print("Deleted successfully")

