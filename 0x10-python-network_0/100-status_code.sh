#!/bin/bash
#iam here
curl -sw '%{response_code}' -o /dev/null "$1"
