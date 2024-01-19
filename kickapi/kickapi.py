# kickapi/kickapi.py
import requests
from kickapi.channel_data import ChannelData
from kickapi.video_data import VideoData
from kickapi.chat_data import ChatData

class KickAPI:
    def __init__(self):
        # Initialize the session and set headers and cookies
        self.session = requests.Session()
        self.headers = {
            "Accept": "application/json",
            "Accept-Language": "ar,en-US;q=0.7,en;q=0.3",
            "Alt-Used": "kick.com",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
        }

    def channel(self, username):
        # Get channel data by username
        url = f"https://kick.com/api/v1/channels/{username}"
        response = self.session.get(url, headers=self.headers)
        try:
            data = response.json()
            return ChannelData(data)
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