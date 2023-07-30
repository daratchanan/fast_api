from fastapi import FastAPI
import pymongo 
from schemas.tag_schema import tages_serializer
from bson import ObjectId

app = FastAPI()

mocked_movies_data = [
    {"id": 1, "name": "Movie 1", "genre": "Action"},
    {"id": 2, "name": "Movie 2", "genre": "Adventure"},
]

myclient = pymongo.MongoClient("mongodb://root:qwerty@192.168.1.119:27017/")
db = myclient["chadchart"]
col_tags = db["tags"]


data = [
    { "id": 1, "title": "Book 1", "author": "Author 1" },
    { "id": 2, "title": "Book 2", "author": "Author 2" },
]

@app.get('/tags')
async def find_all():
    tags = tages_serializer(col_tags.find())
    return {"status": "Ok","data": tags}

@app.get('/tags/{id}')
async def find_one(id: str):
    tag = tages_serializer(col_tags.find({"_id": ObjectId(id)}))
    return {"status": "Ok","data": tag}


# @app.get('/')
# async def say_hi():
#     return "hello world natty"



    

