#!/bin/bash
#extracting methods
curl -sIX OPTIONS "$1" | grep Allow | cut -d' ' -f2-
