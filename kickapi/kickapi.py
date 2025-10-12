# kickapi/kickapi.py
import logging
import cloudscraper
from kickapi.category_data import CategoryResponse
from kickapi.channel_data import ChannelData
from kickapi.video_data import VideoData
from kickapi.chat_data import ChatData
from kickapi.clip_data import ClipData
import ua_generator

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class KickAPI:
    def __init__(self):
        # Initialize the session and set headers and cookies
        self.session = cloudscraper.CloudScraper()
        self.ua = ua_generator.generate()
        self.headers = {
            "Accept": "application/json",
            "Alt-Used": "kick.com",
            "Priority": "u=0, i",
            "Connection": "keep-alive",
            "User-Agent": self.ua.text
        }

    def categories(self, page, limit=32):
        """Fetch categories (subcategories list) with pagination."""
        url = f"https://kick.com/api/v1/subcategories?limit={limit}&page={page}"
        response = self.session.get(url)
        try:
            data = response.json()
            return CategoryResponse(data)
        except ValueError:
            logger.error("Failed to parse JSON response for categories.")
            return None

    def channel(self, username):
        url = f"https://kick.com/api/v1/channels/{username}"
        response = self.session.get(url, headers=self.headers)
        try:
            data = response.json()
            return ChannelData(data, api=self)
        except ValueError:
            logger.error("Failed to parse JSON response for channel: %s", username)
            return None
        
    def video(self, video_id):
        url = f"https://kick.com/api/v1/video/{video_id}"
        response = self.session.get(url, headers=self.headers)
        try:
            data = response.json()
            return VideoData(data)
        except ValueError:
            logger.error("Failed to parse JSON response for video: %s", video_id)
            return None
        
    def chat(self, channel_id, datetime):
        url = f"https://kick.com/api/v2/channels/{channel_id}/messages?start_time={datetime}"
        response = self.session.get(url, headers=self.headers)
        try:
            data = response.json()
            return ChatData(data)
        except ValueError:
            logger.error(
                "Failed to parse JSON response for chat: channel_id=%s, datetime=%s",
                channel_id, datetime
            )
            return None
        
    def clip(self, clip_id):
        url = f"https://kick.com/api/v2/clips/{clip_id}"
        response = self.session.get(url, headers=self.headers)
        try:
            data = response.json()['clip']
            return ClipData(data)
        except ValueError:
            logger.error("Failed to parse JSON response for clip: %s", clip_id)
            return None