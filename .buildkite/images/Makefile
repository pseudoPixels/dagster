py27 = 2.7.16
py35 = 3.5.7
py36 = 3.6.9
py37 = 3.7.4
py38 = 3.8.0

####################################################################################################
# Update snapshots
####################################################################################################
snap:
	./docker/snapshot-update.sh

####################################################################################################
# Buildkite integration images
####################################################################################################
build-integration-38:
	./docker/build.sh $(py38) integration $(VERSION)

push-integration-38:
	./docker/push.sh $(py38) integration $(VERSION)

build-integration-37:
	./docker/build.sh $(py37) integration $(VERSION)

push-integration-37:
	./docker/push.sh $(py37) integration $(VERSION)

build-integration-36:
	./docker/build.sh $(py36) integration $(VERSION)

push-integration-36:
	./docker/push.sh $(py36) integration $(VERSION)

build-integration-35:
	./docker/build.sh $(py35) integration $(VERSION)

push-integration-35:
	./docker/push.sh $(py35) integration $(VERSION)

build-integration-27:
	./docker/build.sh $(py27) integration $(VERSION)

push-integration-27:
	./docker/push.sh $(py27) integration $(VERSION)

build-integration: build-integration-37 build-integration-36 build-integration-35 build-integration-27
push-integration: push-integration-37 push-integration-36 push-integration-35 push-integration-27

####################################################################################################
# Public images
####################################################################################################
build-public-37:
	./docker/build.sh $(py37) public $(VERSION)

push-public-37:
	./docker/push.sh $(py37) public $(VERSION)

build-public-36:
	./docker/build.sh $(py36) public $(VERSION)

push-public-36:
	./docker/push.sh $(py36) public $(VERSION)

build-public-35:
	./docker/build.sh $(py35) public $(VERSION)

push-public-35:
	./docker/push.sh $(py35) public $(VERSION)

build-public-27:
	./docker/build.sh $(py27) public $(VERSION)

push-public-27:
	./docker/push.sh $(py27) public $(VERSION)

build-public: build-public-37 build-public-36 build-public-35 build-public-27
push-public: push-public-37 push-public-36 push-public-35 push-public-27
