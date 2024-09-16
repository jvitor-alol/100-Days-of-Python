#!/bin/bash

if [ -f "requirements.txt" ]; then
    pip3 install --user -r requirements.txt
fi
