#!/bin/sh

curl -sI "$1" | grep -i "Location" | cut -d ' ' -f 2
