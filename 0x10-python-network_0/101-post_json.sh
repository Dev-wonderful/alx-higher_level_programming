#!/bin/bash
# read json file then post content
file=$(<$2)
curl --silent --request POST "$1" --data "$file" -H "Content-Type: application/json"