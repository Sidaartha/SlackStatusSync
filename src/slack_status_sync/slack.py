import logging
from typing import Optional
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logger = logging.getLogger(__name__)

class SlackService:
    def __init__(self, token: str):
        """Initialize the Slack service with the given token."""
        self.client = WebClient(token=token)

    def update_status(self, text: str, emoji: str = "📅", expiration: Optional[int] = None) -> bool:
        """Update the Slack status with the given text and emoji.
        
        Args:
            text: The status text
            emoji: The status emoji
            expiration: Unix timestamp when the status should expire (optional)
        """
        try:
            profile = {
                "status_text": text,
                "status_emoji": emoji,
            }
            if expiration:
                profile["status_expiration"] = expiration
            else:
                profile["status_expiration"] = 0
                
            self.client.users_profile_set(profile=profile)
            logger.info(f"Successfully updated Slack status to: {text}")
            return True
        except SlackApiError as e:
            logger.error(f"Slack API Error: {e.response['error']}")
            return False 