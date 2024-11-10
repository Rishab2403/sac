import pymongo

if __name__=="__main__":
    print("Welcome to pyMango")
    client =pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db =client['student']
    collection=db['sample']
    
    #one =collection.find_one()
    #print(one) #it retrives random file from db
    
    parti_one=collection.find_one({'name':'xyz'})#for particular document
    print(parti_one)
    
    #the value which has only 1 -will be displayed and 0- will not be displayed
    allDocs=collection.find({'name':'Sharan'},{'name':0,'_id':0})
    
    for item in allDocs:
        print(item)
        
        