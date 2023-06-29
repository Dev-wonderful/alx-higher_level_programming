#!/bin/bash
# getting the content length of a web page
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
