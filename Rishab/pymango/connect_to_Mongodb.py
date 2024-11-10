import pymongo

if __name__=="__main__":
    print("Welcome to pyMango")
    client =pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db =client['student']
    collection=db['sample']