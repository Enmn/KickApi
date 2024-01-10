# kickapi/channel_data.py
class ChannelData:
    def __init__(self, data):
        # Initialize channel data attributes
        self.id = data.get("id")
        self.user_id = data.get("user_id")
        self.username = data.get("slug")
        self.bio = data.get("user", {}).get("bio")
        self.avatar = data.get("user", {}).get("profile_pic")
        self.followers = data.get("followersCount")
        self.playback = data.get("playback_url")