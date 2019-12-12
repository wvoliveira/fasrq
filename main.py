#!/usr/bin/env python3

"""
Simple todo API with some methods:
GET /                       => return all items
GET /{id}                   => return just one item
PUT / payload: task         => insert one task
POST / payload: id and task => insert or update one task
DELETE /{id}                => delete item
"""

from os import getenv
from fastapi import FastAPI, HTTPException

from typing import List
from pydantic import BaseModel

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
from marshmallow_sqlalchemy import ModelSchema

DB_HOST = getenv('DB_HOST', 'localhost:4001')
DB_USERNAME = getenv('DB_USERNAME', 'bob')
DB_PASSWORD = getenv('DB_PASSWORD', 'secret1')


app = FastAPI()
Base = declarative_base()


class Item(Base):
    """Item model"""
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String)


class ItemSchema(BaseModel):
    """Item schema to dump result"""
    id: int
    task: str


auth = '{}:{}'.format(DB_USERNAME, DB_PASSWORD)
engine = create_engine('rqlite+pyrqlite://{0}@{1}/'.format(auth, DB_HOST))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

@app.head('/')
@app.get('/', response_model=List[ItemSchema])
async def get_items():
    return session.query(Item).all()


@app.get('/{id}')
async def get_item(id: int):
    return session.query(Item).filter_by(id=id).first()


@app.put('/', response_model=ItemSchema)
async def put_item(task: str):
    item = Item(task=task)
    session.add(item)
    session.commit()
    return item


@app.post('/', response_model=ItemSchema)
async def post_item(task: str, id: int = None):
    item = None

    if id is not None:
        item = session.query(Item).filter_by(id=id).first()
        item.task = task
    else:
        item = Item(task=task)

    session.add(item)
    session.commit()

    return item


@app.delete('/{id}')
async def delete_item(id: int):
    item = session.query(Item).filter_by(id=id).first()
    if item is None:
        raise HTTPException(status_code=404, detail='item not found')

    session.delete(item)
    session.commit()
    return 'OK'
