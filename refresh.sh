#!/bin/sh
cp /usr/local/bin/* src/
git add -u
DATE=$(date +'%m/%d/%Y')
git commit -m "[Refresh] ${DATE}"
git push
