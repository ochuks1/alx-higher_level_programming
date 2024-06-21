#!/bin/bash
# Script to make a request and get the response with "You got me!" message
curl -sL -X PUT -d "user_id=98" -H "Origin: School" "0.0.0.0:5000/catch_me"
