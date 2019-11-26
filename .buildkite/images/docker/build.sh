#! /bin/bash
ROOT=$(git rev-parse --show-toplevel)
pushd $ROOT/.buildkite/images/docker/

# Version of the buildkite image. Update this when you make significant changes to the image.
IMAGE_VERSION="v6"


function cleanup {
    rm -rf scala_modules
    set +ux
}

# # ensure cleanup happens on error or normal exit
trap cleanup INT TERM EXIT ERR

if [ "$#" -ne 2 ]; then
    echo "Error: Must specify a Python version and image type.\n" 1>&2
    echo "Usage: ./build.sh 3.7.4 integration" 1>&2
    return 0
fi

set -ux

# e.g. 3.7.4
PYTHON_VERSION=$1
# e.g. 3
PYTHON_MAJOR_VERSION="${PYTHON_VERSION:0:1}"
# e.g. 37
PYTHON_MAJMIN=`echo "${PYTHON_VERSION:0:3}" | sed 's/\.//'`

if (( $PYTHON_MAJMIN > 37 )); then

    DEBIAN_BASE='buster'

else
    DEBIAN_BASE='stretch'

fi

IMAGE_TYPE=$2

rsync -av --exclude='*target*' --exclude='*.idea*' --exclude='*.class' $ROOT/scala_modules . && \
\
if [ $IMAGE_TYPE == "integration" ]; then
    # Build the integration image
    docker build . \
        --no-cache \
        --build-arg PYTHON_VERSION=$PYTHON_VERSION \
        --build-arg PYTHON_MAJOR_VERSION=$PYTHON_MAJOR_VERSION \
        --build-arg DEBIAN_BASE=$DEBIAN_BASE \
        --target dagster-integration-image \
        -t "dagster/buildkite-integration:py${PYTHON_VERSION}-${IMAGE_VERSION}"
else
    # Build the public image
    docker build . \
        --no-cache \
        --build-arg PYTHON_VERSION=$PYTHON_VERSION \
        --target dagster-public-image \
        -t "dagster/dagster-py${PYTHON_MAJMIN}"
fi
rm -rf scala_modules
set +ux
