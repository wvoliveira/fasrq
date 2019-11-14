# Use make to build, run, push and so on

NAME = fasrq
VERSION ?= 0.0.1
DB_HOST ?= $(shell hostname -I | cut -d' ' -f1):4001
TAG ?= wvoliveira

all:
	build tag push

build:
	docker build -t ${NAME}:${VERSION} .

run:
	docker run --rm -p 8000:80 -e DB_HOST="${DB_HOST}" ${NAME}:${VERSION}

tag: build
	docker tag ${NAME}:${VERSION} ${TAG}/${NAME}:${VERSION}

push: build tag
	docker push ${TAG}/${NAME}:${VERSION}

rqlite_run:
	mkdir -p /tmp/rqlite
	docker run --rm -v ${PWD}/conf:/rqlite/conf -v /tmp/rqlite/data:/rqlite/file/data -p 4001:4001 rqlite/rqlite:4.5.0 -auth /rqlite/conf/rqlite.json

clean:
	rm -rfv __pycharm__
	rm -rfv /tmp/rqlite/data
