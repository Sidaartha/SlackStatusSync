#!/bin/bash

# Copy the plist file to the LaunchAgents directory
cp com.slackstatussync.plist ~/Library/LaunchAgents/

# Load the service
launchctl load ~/Library/LaunchAgents/com.slackstatussync.plist

# Start the service
launchctl start com.slackstatussync

echo "Service installed and started successfully!"
echo "To check status: launchctl list | grep slackstatussync"
echo "To stop service: launchctl stop com.slackstatussync"
echo "To unload service: launchctl unload ~/Library/LaunchAgents/com.slackstatussync.plist" 