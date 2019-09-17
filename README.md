# fasrq

Example api with Fast API + Rqlite with authentication

## tested

- python 3.7.3

## how

Create virtualenv and active:

```
python3 -m venv venv
. venv/bin/active
```

Install dependencies (pip install directly doesnt work):

```bash
cd dep/pyrqlite
pip3 install -e .

cd ../sqlalchemy-rqlite
pip3 install -e .

cd ../..

pip3 install -r requirements.txt
```

Now you need run rqlite database with auth:

```bash
curl -L https://github.com/rqlite/rqlite/releases/download/v4.5.0/rqlite-v4.5.0-linux-amd64.tar.gz -o rqlite-v4.5.0-linux-amd64.tar.gz
tar xvfz rqlite-v4.5.0-linux-amd64.tar.gz
mv rqlite-v4.5.0-linux-amd64/rqlite .

# create config with credentials
cat << EOF > config.json
[
  {
    "username": "bob",
    "password": "secret1",
    "perms": ["all"]
  },
  {
    "username": "mary",
    "password": "$2a$10$fKRHxrEuyDTP6tXIiDycr.nyC8Q7UMIfc31YMyXHDLgRDyhLK3VFS",
    "perms": ["query", "status"]
  }
]
EOF

# run rqlite
./rqlited -auth config.json ~/node.1
```

In another terminal just run uvicorn:

```bash
uvicorn main:app --reload
```

Access to <localhost:8000/docs> and be happy
