#!/bin/bash
# Script to display the size of the body of the response
curl -s "$1" | wc -c