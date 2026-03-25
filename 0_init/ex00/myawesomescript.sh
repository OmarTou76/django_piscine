#!/bin/sh

curl -sI "$1" | grep -i "LoCation" | cut -d ' ' -f 2
