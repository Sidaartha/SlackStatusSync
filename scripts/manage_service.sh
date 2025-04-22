#!/bin/bash

SERVICE_NAME="com.slackstatussync"
PLIST_PATH="$HOME/Library/LaunchAgents/$SERVICE_NAME.plist"
LOG_FILE="logs/stdout.log"

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${BLUE}Status:${NC}"
    if launchctl list | grep -q "$SERVICE_NAME"; then
        echo -e "${GREEN}Service is loaded${NC}"
        launchctl list | grep "$SERVICE_NAME"
    else
        echo -e "${RED}Service is not loaded${NC}"
    fi
}

case "$1" in
    "install")
        echo "Installing service..."
        cp "$SERVICE_NAME.plist" "$PLIST_PATH"
        launchctl load "$PLIST_PATH"
        print_status
        ;;
        
    "update")
        echo "Updating service..."
        launchctl unload "$PLIST_PATH"
        cp "$SERVICE_NAME.plist" "$PLIST_PATH"
        launchctl load "$PLIST_PATH"
        print_status
        ;;
        
    "restart")
        echo "Restarting service..."
        launchctl unload "$PLIST_PATH"
        launchctl load "$PLIST_PATH"
        print_status
        ;;
        
    "stop")
        echo "Stopping service..."
        launchctl unload "$PLIST_PATH"
        print_status
        ;;
        
    "start")
        echo "Starting service..."
        launchctl load "$PLIST_PATH"
        print_status
        ;;
        
    "status")
        print_status
        ;;
        
    "logs")
        if [ -f "$LOG_FILE" ]; then
            echo "Last 20 lines of logs:"
            tail -n 20 "$LOG_FILE"
        else
            echo -e "${RED}No log file found${NC}"
        fi
        ;;
        
    "test")
        echo "Running script directly for testing..."
        python3 -m src.slack_status_sync.main
        echo "Check logs for details:"
        tail -n 10 "$LOG_FILE"
        ;;
        
    *)
        echo "Usage: $0 {install|update|restart|stop|start|status|logs|test}"
        echo
        echo "Commands:"
        echo "  install - Install and start the service"
        echo "  update  - Update the service with new configuration"
        echo "  restart - Restart the service"
        echo "  stop    - Stop the service"
        echo "  start   - Start the service"
        echo "  status  - Check service status"
        echo "  logs    - Show recent logs"
        echo "  test    - Run the script directly for testing"
        exit 1
        ;;
esac 