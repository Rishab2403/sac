import pymongo

if __name__=="__main__":
    print("Welcome to pyMango")
    client =pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db =client['student']
    collection=db['sample']
    
    #insert one
    #dictionary={'name':'Sharan','marks':599}
    #collection.insert_one(dictionary)
    
    #dictionary1={'name':'Rishab','marks':600}
    #collection.insert_one(dictionary1)
    
    #dictionary2={'name':'Shreyas','marks':588}
    #collection.insert_one(dictionary2)
    
    #insert many
    insertThese=[
        {'name':'xyz','Location':'Delhi','Marks':100},
        {'name':'abc','Location':'Belagavi','Marks':90},
        {'name':'mno','Location':'Hubli','Marks':89},
        {'name':'efg','Location':'Bengaluru','Marks':85}
        ]
    
    collection.insert_many(insertThese)