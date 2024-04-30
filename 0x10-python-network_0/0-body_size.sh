#!/bin/bash
#curling some requests
curl -s "$1" | wc -c
