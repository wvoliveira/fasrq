# fasrq

Example API with framework FastAPI and database Rqlite with authentication

## Tested

- Python 3.7.3
- Pip 18.1
- Docker 19.03

## Developing

### Local dependencies

Before run application, we need run the rqlite database with auth.

```bash
make run_database
```

Create virtualenv, install dependencies and run:

```bash
make
```

Or just run with: `make run_api`

### With docker

```bash
# run database
make run_database

# in another terminal build and run API
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
