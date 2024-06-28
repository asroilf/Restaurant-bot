#!/bin/sh

# Start the Rasa server in the background
rasa run -m models --enable-api --cors '*' &

# Start the Rasa action server
rasa run actions

