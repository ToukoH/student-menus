#!/bin/bash

SCRIPT_NAME="main.py"
SOURCE_SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

SOURCE_SCRIPT="$SOURCE_SCRIPT_DIR/$SCRIPT_NAME"

SYMLINK_NAME="/usr/local/bin/safkat"

if [ ! -f "$SOURCE_SCRIPT" ]; then
    echo "Script not found in the current directory: $SCRIPT_NAME"
    exit 1
fi

ln -sf "$SOURCE_SCRIPT" "$SYMLINK_NAME"

chmod +x "$SOURCE_SCRIPT"

echo "Symbolic link created for $SOURCE_SCRIPT as $SYMLINK_NAME"

