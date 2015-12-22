#!/bin/bash

function usage () {
  echo "usage: $0 <version>"
}

version=$1
shift
if [ -z "$version" ]
then
  usage
  exit 1
fi

googlecode_upload.py -p python-deep \
  -s "python-deep $version" \
  -l python,deep,recursive,comparison \
  -u fergald@gmail.com \
  dist/deep-$version.tar.gz
