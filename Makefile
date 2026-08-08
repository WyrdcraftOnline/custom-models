.DEFAULT_GOAL := build

.PHONY: build release painting

build: release

release:
	bash ./build.sh

painting:
	python3 ./scripts/create_painting_asset.py
