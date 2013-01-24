#!/bin/bash
if [ "$1" = "-D" ]; then
    find . -name '*.pyc' -delete
else
    find . -name '*.pyc'
    echo ' are able to deleting...'
    echo ' do this command if you need.'
    echo "    $ $0 -D"
fi

