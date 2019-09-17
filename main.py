from os import getenv
from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from marshmallow_sqlalchemy import ModelSchema

RQLITE_HOST = getenv('RQLITE_HOST', 'localhost:4001')
RQLITE_USERNAME = getenv('RQLITE_USERNAME', 'bob')
RQLITE_PASSWORD = getenv('RQLITE_PASSWORD', 'secret1')


app = FastAPI()
Base = declarative_base()


class Todo(Base):
    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String)

    def __repr__(self):
        return "<Todo(id='{}', task='{}')>".format(self.id, self.task)

class TodoSchema(ModelSchema):
    class Meta:
        model = Todo


auth = '{}:{}'.format(RQLITE_USERNAME, RQLITE_PASSWORD)
engine = create_engine('rqlite+pyrqlite://{0}@{1}/'.format(auth, RQLITE_HOST))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

schema = TodoSchema()


@app.get('/')
def get_items():
    items = session.query(Todo).all()
    result = schema.dump(items, many=True)
    return result

@app.get('/{id}')
def get_item(id: int):
    item = session.query(Todo).filter_by(id=id).first()
    result = schema.dump(item)
    return result

@app.put('/')
def put_item(task: str):
    item = Todo(task=task)

    session.add(item)
    session.commit()

    result = schema.dump(item)
    return result

@app.post('/')
def post_item(task: str, id: int = None):
    if id is not None:
        item = session.query(Todo).filter_by(id=id).first() 
        item.task = task
    else:
        item = Todo(task=task)

    session.add(item)
    session.commit()

    result = schema.dump(item)
    return result
