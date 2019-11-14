# fasrq

Example api with Fast API + Rqlite with authentication

## Tested

- Python 3.7.3
- Docker 19.03

## Developing

Create virtualenv and active:

```bash
python3 -m venv venv
. venv/bin/active
```

Install dependencies (pip install directly doesnt work):

```bash
pip3 install dep/pyrqlite
pip3 install dep/sqlalchemy-rqlite
pip3 install -r requirements.txt
```

Now you need run rqlite database with auth.

First, get it:

```bash
curl -L https://github.com/rqlite/rqlite/releases/download/v4.5.0/rqlite-v4.5.0-linux-amd64.tar.gz -o rqlite-v4.5.0-linux-amd64.tar.gz
tar xvfz rqlite-v4.5.0-linux-amd64.tar.gz
mv rqlite-v4.5.0-linux-amd64/rqlite .

# run rqlite
./rqlited -auth conf/rqlite.json ~/node.1
```

In another terminal just run uvicorn:

### Run local

```bash
uvicorn main:app --reload
```

### Run with docker

```bash
docker run --rm -p 8000:80 -e DB_HOST="<your address>:4001" wvoliveira/fasrq:0.0.1
```

Access to <localhost:8000/docs> and be happy.

Make GET/PUT/POST methods in /docs endpoint.

## Routes

- GET <localhost:8000/>: Get all items.
- GET <localhost:8000/[id]>: Get single item.
- PUT <localhost:8000/>: Insert task.
- POST <localhost:8000/>: Insert/update task.
