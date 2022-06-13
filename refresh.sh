#!/bin/sh
cp /usr/local/bin/* src/
git add --all # -u if I have a gitignore
DATE=$(date +'%m/%d/%Y %H:%M:%S')
git commit -m "[Auto-Refresh] ${DATE}"
git push
