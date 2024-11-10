import pymongo

if __name__=="__main__":
    print("Welcome to pyMango")
    client =pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db =client['student']
    collection=db['sample']
    
    #For delete one
    #rec={"name":"Sharan"}
    #collection.delete_one(rec)
    
    #For delete many
    up={"name":"Sharan"}
    collection.delete_many(up)
    print(up.delete_count)