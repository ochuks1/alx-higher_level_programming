#!/bin/bash
# Script to send a JSON POST request and display the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
