import pymongo


class MongoDB_Helper():

    def __init__(self, server: str, username: str, password: str, db_name="default_db", collection_name="default_collection"):
        '''Intializes connection and creates default database and collection'''
        self.db_name = db_name
        self.collection_name = collection_name

        self.client = pymongo.MongoClient(f"mongodb://{server}/", username=username, password=password) # init connection
        self._create_database(db_name)
        self._create_collection(db_name, collection_name)


    def _create_database(self, db_name: str):
        '''Create database if does not exist'''
        dblist = self.client.list_database_names()
        if db_name in dblist:
            print(f"Database {db_name} already exists")
        else:
            print(f"Creating database {db_name}") # db init is not complete until content is added
            mydb = self.client[db_name]


    def list_databases(self):
        '''List all databases'''
        dblist = self.client.list_database_names()
        print(dblist)


    def _create_collection(self, db_name: str, collection_name: str):
        '''Create collection if does not exist'''
        db = self.client[db_name]

        collist = db.list_collection_names()
        if collection_name in collist:
            print(f"Collection {collection_name} already exists")
        else:
            print(f"Creating collection {collection_name}") # collection init is not complete until content is added
            collection = db[collection_name]


    def list_collections(self):
        '''List all collections'''
        db = self.client[self.db_name]
        col_list = db.list_collection_names()
        print(col_list)


    def insert_document(self, document: dict):
        '''Insert single document into collection'''
        print(f"Inserting document into {self.collection_name}")

        if type(document) is not dict:
            raise TypeError

        db = self.client[self.db_name]
        collection = db[self.collection_name]

        x = collection.insert_one(document)
        print(x.inserted_id)


    def insert_multiple_documents(self, documents: list):
        '''Insert multiple documents into collection'''
        print(f"Inserting multiple documents into {self.collection_name}")

        if type(documents) is not list:
            raise TypeError

        db = self.client[self.db_name]
        collection = db[self.collection_name]

        x = collection.insert_many(documents)


    def find_field(self):
        '''Find specific field in default collection'''
        print(f"Finding field in {self.collection_name}")

        db = self.client[self.db_name]
        collection = db[self.collection_name]

        for x in collection.find({},{ "_id": 0, "name": 1, "address": 1 }): # need to parameterize
            print(x)


    def query_field(self, query: dict):
        '''Query default collection for specific field'''
        print(f"Querying {self.collection_name} for field")

        if type(query) is not dict:
            raise TypeError

        db = self.client[self.db_name]
        collection = db[self.collection_name]

        mydoc = collection.find(query)

        for x in mydoc:
            print(x)


mydict = { "name": "John", "address": "Highway 38" }

mylist = [
    { "name": "Amy", "address": "Apple st 652"},
    { "name": "Hannah", "address": "Mountain 21"},
    { "name": "Michael", "address": "Valley 345"},
    { "name": "Sandy", "address": "Ocean blvd 2"},
    { "name": "Betty", "address": "Green Grass 1"},
    { "name": "Richard", "address": "Sky st 331"},
    { "name": "Susan", "address": "One way 98"},
    { "name": "Vicky", "address": "Yellow Garden 2"},
    { "name": "Ben", "address": "Park Lane 38"},
    { "name": "William", "address": "Central st 954"},
    { "name": "Chuck", "address": "Main Road 989"},
    { "name": "Viola", "address": "Sideway 1633"}
    ]

myquery = { "address": "Park Lane 38" }

# create instance of class
x = MongoDB_Helper(server="localhost:27017", username="mongodbuser", password="your_mongodb_root_password")

x.list_databases()
x.list_collections()

# x.insert_document(mydict)
# x.insert_multiple_documents(mylist)

x.query_field(myquery)
x.find_field()
