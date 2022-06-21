import Database
from fastapi import FastAPI

app = FastAPI()
collection_name = Database.get_database()['Samples']


@app.get('/get_virus_family/{hash}')
def get_virus_family(hash: str):
    obj = collection_name.find_one(hash)
    return {'Family': obj['family']}


@app.get('/get_virus_hashes_by_family/{family}')
def get_virus_hashes_by_family(family: str):
    obj = collection_name.find({'family': family})
    return list(obj)


@app.post('/insert_virus/{hash}/{family}')
def insert_virus(hash: str, family: str):
    item = {
        "_id": hash,
        "family": family,
    }
    collection_name.insert_one(item)
    return {'Sample inserted successfully'}
