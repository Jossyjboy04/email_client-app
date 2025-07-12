#!/bin/bash

# Navigate to the project folder
cd \home\joseph\email_client

# Run the processor and log output
/usr/bin/python3 main.py >> email_log.txt 2>&1
