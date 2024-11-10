import pymongo

if __name__=="__main__":
    print("Welcome to pyMango")
    client =pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db =client['student']
    collection=db['sample']
    
    alldbs=client.list_database_names() #shaows all the list of data in databases  
    print(alldbs)
    
    collectns=client['student']
    print(collectns.list_collection_names())
    