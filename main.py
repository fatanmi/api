from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


myPosts = [
    {"title": "Referencing", "content": "A book about plagiarism", "id": 1},
    {"title": "Referencing", "content": "A book about plagiarism", "id": 2}
]


def getPostID(id):
    for post in myPosts:
        if (post["id"]==id):
            return post

@app.get("/")
async def root():
    return {"message": "Welcome to my API"}


@app.get("/posts")
async def get_post():
    return {"message": myPosts}

@app.get("/posts/{id}")
async def getPostById(id):
    post=getPostID(int(id))
    return{"mydetails": post}


@app.post("/posts")
def create_post(post: Post):
    postDict=post.dict()
    postDict["id"]=randrange(0,100000000)
    myPosts.append(postDict)
    return {"data": myPosts}
