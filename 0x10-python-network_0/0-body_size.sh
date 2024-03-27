#!/bin/bash
# Get byte size of the HTTP response header for a URL
curl -s "$1" | wc -c
