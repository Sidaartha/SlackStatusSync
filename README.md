# Slack Status Sync

A Python application that automatically syncs your Slack status with your Google Calendar events. It runs as a background service on macOS and updates your Slack status every 5 minutes based on your current calendar event.

## Features

- Automatically updates Slack status based on current Google Calendar event
- Supports custom emojis in event titles
- Sets status expiration based on event end time
- Runs as a background service on macOS
- Detailed logging for troubleshooting
- Secure credential management
- Automatic token refresh for Google Calendar API

## Prerequisites

- Python 3.7+
- macOS
- Google Calendar API credentials
- Slack API token

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/slack-status-sync.git
cd slack-status-sync
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up Google Calendar API:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable the Google Calendar API
   - Create OAuth 2.0 credentials
   - Download the credentials and save as `credentials.json` in the project root
   - The credentials file should contain client_id and client_secret

5. Set up Slack API:
   - Go to [Slack API](https://api.slack.com/apps)
   - Create a new app
   - Add `users.profile:write` scope
   - Install the app to your workspace
   - Copy the OAuth token (starts with 'xoxp-')

6. Create a `.env` file in the project root:
```bash
SLACK_TOKEN=your_slack_token_here
```

7. Run the initial setup:
```bash
python src/slack_status_sync/setup.py
```
   - This will create a `token.json` file for Google Calendar authentication
   - Follow the OAuth flow in your browser when prompted

8. Install the service:
```bash
./scripts/manage_service.sh install
```

## Security Considerations

- Keep your API tokens secure and never commit them to version control
- The `.env` file is automatically added to `.gitignore`
- Regularly rotate your Slack API token
- Store credentials in a secure location
- Use environment variables for sensitive data in production

## Usage

The service will automatically run every 5 minutes. You can manage it using the provided script:

```bash
# Check service status
./scripts/manage_service.sh status

# View logs
./scripts/manage_service.sh logs

# Restart service
./scripts/manage_service.sh restart

# Stop service
./scripts/manage_service.sh stop

# Start service
./scripts/manage_service.sh start
```

## Calendar Event Format

To set a custom emoji for your status, include it at the start of your calendar event title:

```
🔥 Team Meeting
🎯 Project Review
💻 Coding Session
```

The emoji will be used as your Slack status emoji, and the rest of the title will be your status text.

## Project Structure

```
slack-status-sync/
├── src/
│   └── slack_status_sync/
│       ├── __init__.py
│       ├── main.py
│       ├── calendar.py
│       └── slack.py
├── scripts/
│   ├── com.slackstatussync.plist
│   ├── manage_service.sh
│   └── install_service.sh
├── logs/
│   ├── stdout.log
│   └── stderr.log
├── requirements.txt
├── setup.py
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 