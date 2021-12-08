from typing import Optional
from sqlalchemy import schema
from fastapi import FastAPI
from pydantic.utils import Representation
from schemas import Blog


@app.post('/')
def create_blog(request: Blog):
    return request