#!/bin/bash
# Sends JSON POST request to a URL with a given JSON
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
