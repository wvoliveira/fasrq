# Use make to build, run, push and so on

NAME = fasrq
VERSION?=0.0.1
DB_HOST?=localhost:4001
TAG?=wvoliveira

build:
	docker build -t ${NAME}:${VERSION} .

run: build
	docker run --rm -p 8000:80 -e DB_HOST="${DB_HOST}" ${NAME}:${VERSION}

tag: build
	docker tag ${NAME}:${VERSION} ${TAG}/${NAME}:${VERSION}

push: build tag
	docker push ${TAG}/${NAME}:${VERSION}
