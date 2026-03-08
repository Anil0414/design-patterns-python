class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating Database Connection")
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance


db1 = Database()
db2 = Database()

print(db1 is db2)