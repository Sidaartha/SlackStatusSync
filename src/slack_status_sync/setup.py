import os
import sys
from pathlib import Path

def setup():
    """Setup the application by checking for required files and creating necessary directories."""
    print("Setting up Slack Status Sync...")
    
    # Check for .env file
    if not os.path.exists('.env'):
        print("\n.env file not found. Please create one with your Slack token:")
        print("SLACK_TOKEN=your_slack_token_here")
        sys.exit(1)
    
    # Check for Google Calendar credentials
    if not os.path.exists('credentials.json'):
        print("\ncredentials.json not found. Please download it from Google Cloud Console:")
        print("1. Go to https://console.cloud.google.com/")
        print("2. Create a new project")
        print("3. Enable the Google Calendar API")
        print("4. Create OAuth 2.0 credentials")
        print("5. Download the credentials and save as credentials.json")
        sys.exit(1)
    
    # Create necessary directories
    Path('logs').mkdir(exist_ok=True)
    
    print("\nSetup complete! You can now run the application.")
    print("To install as a service, run: ./scripts/manage_service.sh install")

if __name__ == '__main__':
    setup() 