#!/bin/bash
# Comment
curl -s -o /dev/null -I --w "%{http_code}" "$1"
