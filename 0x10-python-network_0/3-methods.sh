#!/bin/bash
# getting the allowed methods of a web page
curl -sI "$1" | grep -i "Allow" | awk -F ': ' '{print $2}'
