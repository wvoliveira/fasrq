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

Just run theses commands:

```bash
mkdir data # for database
docker run --rm -v ${PWD}/conf:/rqlite/conf -v ${PWD}/data:/rqlite/file/data -p 4001:4001 rqlite/rqlite:4.5.0 -auth /rqlite/conf/rqlite.json
```

In another terminal just run application:

```bash
# with python venv
uvicorn main:app --reload

# or with docker
docker run --rm -p 8000:80 -e DB_HOST="<your address>:4001" wvoliveira/fasrq:0.0.1
```

Or run with make (using docker)

```bash
# build API
make build

# run database
make rqlite_run

# in another shell, run API
make run
```

Access to <localhost:8000/docs> and be happy.

Make GET/PUT/POST/DELETE methods in /docs endpoint.

To clean database and cache, execute: `make clean`

## Routes

- GET <localhost:8000/>: Get all items.
- GET <localhost:8000/[id]>: Get single item.
- PUT <localhost:8000/>: Insert task.
- POST <localhost:8000/>: Insert/update task.
- DELETE <localhost:8000/[id]>: Delete single item.
