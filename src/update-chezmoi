#!/bin/sh
# Update the dotfiles that are listed in the DOTFILES env variable
for FILE in $(cat "$DOTFILES") ; do
	echo "Adding ${FILE}"
	chezmoi add $FILE
done

DATE=$(date +'%m/%d/%Y')
