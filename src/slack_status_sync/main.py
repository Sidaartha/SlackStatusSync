import os
import logging
import datetime
from typing import Optional
from dotenv import load_dotenv
from .calendar import CalendarService
from .slack import SlackService

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='logs/stdout.log',
    filemode='a'  # Append to the existing file instead of creating a new one
)
logger = logging.getLogger(__name__)

class SlackStatusSync:
    def __init__(self, slack_token: str):
        """Initialize the SlackStatusSync with required services."""
        self.calendar_service = CalendarService()
        self.slack_service = SlackService(slack_token)

    def sync_status(self) -> None:
        """Main function to sync the Slack status with the current calendar event."""
        event = self.calendar_service.get_current_event()
        
        if event:
            summary = event.get('summary', 'Busy')
            logger.info(f"Found current event: {summary}")
            
            # Get end time for status expiration
            end_time = datetime.datetime.fromisoformat(event['end']['dateTime'].replace('Z', '+00:00'))
            expiration_timestamp = int(end_time.timestamp())
            
            # Parse emoji and text from summary
            parts = summary.split(' ', 1)
            if len(parts) > 1 and parts[0].strip():
                emoji = parts[0].strip()
                status_text = parts[1].strip()
                self.slack_service.update_status(status_text, emoji=emoji, expiration=expiration_timestamp)
            else:
                # If no emoji found, use default emoji
                self.slack_service.update_status("In a meeting", expiration=expiration_timestamp)

def main():
    """Main entry point for the application."""
    logger.info("Script started")
    
    # Load configuration from .env file
    load_dotenv()
    slack_token = os.getenv('SLACK_TOKEN')
    if not slack_token:
        logger.error("SLACK_TOKEN not found in .env file")
        return

    try:
        logger.info("Initializing SlackStatusSync")
        status_sync = SlackStatusSync(slack_token)
        logger.info("Running sync_status")
        status_sync.sync_status()
        logger.info("Script completed successfully")
    except Exception as e:
        logger.error(f"Error in main execution: {e}", exc_info=True)

if __name__ == '__main__':
    main() 