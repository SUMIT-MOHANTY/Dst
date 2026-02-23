all: build

build:
	@echo "Building project..."
	@./build.sh

optimize:
	@python optimize.py

clean:
	rm -rf www/*
