import os
import datetime
import logging
from typing import Optional, Dict, Any
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

logger = logging.getLogger(__name__)

class CalendarService:
    def __init__(self):
        """Initialize the Google Calendar service."""
        self.service = self._initialize_service()

    def _initialize_service(self) -> Any:
        """Initialize and return the Google Calendar service."""
        SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
        creds = None
        
        if os.path.exists('token.json'):
            try:
                creds = Credentials.from_authorized_user_file('token.json', SCOPES)
            except Exception as e:
                logger.error(f"Error loading credentials: {e}")
                raise

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                try:
                    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                    creds = flow.run_local_server(port=0)
                except Exception as e:
                    logger.error(f"Error during OAuth flow: {e}")
                    raise

            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        return build('calendar', 'v3', credentials=creds)

    def get_current_event(self) -> Optional[Dict[str, Any]]:
        """Get the current event that is happening right now."""
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        now_dt = datetime.datetime.now(datetime.timezone.utc)
        
        try:
            events_result = self.service.events().list(
                calendarId='primary',
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy='startTime'
            ).execute()
            
            events = events_result.get('items', [])
            
            # Filter out all-day events and find events that are currently happening
            for event in events:
                # Skip all-day events
                if 'date' in event['start']:
                    continue
                    
                # Convert event times to datetime objects
                start_time = datetime.datetime.fromisoformat(event['start']['dateTime'].replace('Z', '+00:00'))
                end_time = datetime.datetime.fromisoformat(event['end']['dateTime'].replace('Z', '+00:00'))
                
                # Check if the event is happening right now
                if start_time <= now_dt <= end_time:
                    return event
                    
            return None
            
        except Exception as e:
            logger.error(f"Error fetching calendar events: {e}")
            return None 