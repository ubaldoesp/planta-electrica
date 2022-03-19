.PHONY: run
run:
	@docker-compose up

.PHONY: down
down:
	@docker-compose down

.PHONY: build
build:
	@docker-compose build

.PHONY: rebuild
rebuild:
	@docker-compose build --no-cache
