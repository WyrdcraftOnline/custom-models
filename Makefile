.DEFAULT_GOAL := build

.PHONY: build release

build: release

release:
	bash ./build.sh
