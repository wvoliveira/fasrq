# Use make to build, run, push and so on

.PHONY: all build run tag push database_run clean install run_local lint

NAME = fasrq
VERSION ?= 0.0.1
DB_HOST ?= $(shell hostname -I | cut -d' ' -f1):4001
TAG ?= wvoliveira

default: install run_api

build:
	docker build -t ${NAME}:${VERSION} .

run: build
	docker run --rm -p 8000:80 -e DB_HOST="${DB_HOST}" ${NAME}:${VERSION}

tag: build
	docker tag ${NAME}:${VERSION} ${TAG}/${NAME}:${VERSION}

push: build tag
	docker push ${TAG}/${NAME}:${VERSION}

run_database:
	mkdir -p /tmp/rqlite
	docker run --rm -v ${PWD}/conf:/rqlite/conf -v /tmp/rqlite/data:/rqlite/file/data -p 4001:4001 rqlite/rqlite:4.5.0 -auth /rqlite/conf/rqlite.json

clean:
	rm -rfv __pycharm__
	rm -rfv /tmp/rqlite/data

install:
	python3 -m venv venv && \
	. venv/bin/activate && \
	pip3 install dep/pyrqlite && \
	pip3 install dep/sqlalchemy-rqlite && \
	pip3 install -r requirements.txt

run_api:
	python3 -m venv venv && \
	. venv/bin/activate && \
	uvicorn main:app --reload

lint:
	python3 -m venv venv && \
	. venv/bin/activate && \
	autopep8 -i main.py; pylint main.py; flake8 main.py
