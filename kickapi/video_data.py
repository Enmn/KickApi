# kickapi/video_data.py
from kickapi.channel_data import ChannelData

class VideoData:
    def __init__(self, data):
        # Initialize video data attributes
        self.id = data.get("id")
        self.title = data.get("livestream", {}).get("session_title")
        self.thumbnail = data.get("livestream", {}).get("thumbnail")
        self.duration = data.get("livestream", {}).get("duration")
        self.live_stream_id = data.get("live_stream_id")
        self.createdAt = data.get("created_at")
        self.updatedAt = data.get("updated_at")
        self.uuid = data.get("uuid")
        self.views = data.get("views")
        self.language = data.get("language")
        self.strem_video = data.get("source")
        self.channel = ChannelData(data.get("livestream", {}).get("channel"))
