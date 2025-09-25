# kickapi/kickapi.py
import cloudscraper
from kickapi.channel_data import ChannelData
from kickapi.video_data import VideoData
from kickapi.chat_data import ChatData
from kickapi.clip_data import ClipData
import ua_generator

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

    def channel(self, username):
        url = f"https://kick.com/api/v1/channels/{username}"
        response = self.session.get(url, headers=self.headers)
        try:
            data = response.json()
            return ChannelData(data, api=self)  # Pass self as api
        except ValueError:
            print("Failed to parse JSON response.")
            return None
        
    def video(self, video_id):
        # Get video data by video ID
        url = f"https://kick.com/api/v1/video/{video_id}"
        response = self.session.get(url, headers=self.headers)
        try:
            data = response.json()
            return VideoData(data)
        except ValueError:
            print("Failed to parse JSON response.")
            return None
        
    def chat(self, channel_id, datetime):
        # Get chat data by channel id
        url = f"https://kick.com/api/v2/channels/{channel_id}/messages?start_time={datetime}"
        response = self.session.get(url, headers=self.headers)
        try:
            data = response.json()
            return ChatData(data)
        except ValueError:
            print("Failed to parse JSON response.")
            return None
        
    def clip(self, clip_id):
        # Get chat data by channel id
        url = f"https://kick.com/api/v2/clips/{clip_id}"
        response = self.session.get(url, headers=self.headers)
        try:
            data = response.json()['clip']
            return ClipData(data)
        except ValueError:
            print("Failed to parse JSON response.")
            return None      
    main
