import pymongo

if __name__=="__main__":
    print("Welcome to pyMango")
    client =pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db =client['student']
    collection=db['sample']
    
    #location is updated
    prev={"name":"abc"}
    nextt={"$set":{"Location":"Mumbai"}}
    collection.update_one(prev, nextt)
    
    #used to update many
    collection.update_many(prev, nextt)