
import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    db = client['Riot']
    
    col = db['Streets']

    #documenet/rec delete
    rec = {'Name' : 'Dev'}
    col.delete_one(rec)
    print("Deleted successfully")

    #collection delete (drop)
    #col.drop()
    #print("Dropped successfully")

