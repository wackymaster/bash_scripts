#!/bin/sh
cp /usr/local/bin/* src/
git add --all # -u if I have a gitignore
DATE=$(date +'%m/%d/%Y')
git commit -m "[Refresh] ${DATE}"
git push
