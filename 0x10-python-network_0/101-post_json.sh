#!/bin/bash
# read json file then post content
curl -s --request POST "$1" -d "@$2" -H "Content-Type: application/json"
