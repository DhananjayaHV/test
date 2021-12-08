from typing import Optional
from fastapi import FastAPI
from pydantic import  BaseModel
import schemas
app=FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'Dhananjay'}}

@app.get('/about')
def about():
    return {"Result":"about page"}



@app.get('/about/{id}')
def show(id: int):
    return {'data':id}

@app.get('/blog')
def blog(limit=10,published: bool=True,sort:Optional[str]=None):
    
    if published:
        return {"Data" : f'{limit} published blogs from list.'}
    else:
        return {"Data" : f'{limit} blogs from list.'}


@app.get('/about/{id}/comments')
def comments(id:int):
    return {id:{"Data" : "Dhananjay"}}


class Blog(BaseModel):
    title : str
    body:str
    published:Optional[bool]

@app.post('/create_blog')
def create_blog1(request:Blog):
    return {'Data':f'Blog is created with the {request.title}'}


@app.post('/')
def create_blog(request: schemas.Blog):
    return request