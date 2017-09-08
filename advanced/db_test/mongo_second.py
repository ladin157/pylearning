def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.test
    return db


def add_country(db):
    db.countries.insert({"name": "Vietnam"})


def get_country(db):
    return db.countries.find_one()


if __name__ == "__main__":
    db = get_db()
    add_country(db)
    print(get_country(db))
