#!/bin/bash
# read json file then post content
curl --silent --request POST "$1" -T "$2" -H "Content-Type: application/json"
