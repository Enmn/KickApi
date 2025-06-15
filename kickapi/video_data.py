# kickapi/video_data.py
class VideoData:
    def __init__(self, data):
        livestream = data.get("livestream", {})

        def get_value(key):
            return livestream.get(key) if livestream.get(key) is not None else data.get(key)

        self.id = data.get("id")
        self.title = get_value("session_title")
        self.thumbnail = get_value("thumbnail")
        self.duration = get_value("duration")
        self.live_stream_id = data.get("live_stream_id")
        self.start_time = get_value("created_at")
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")
        self.uuid = data.get("uuid", data.get("video", {}).get("uuid"))
        self.views = data.get("views")
        self.language = get_value("language")
        self.stream = data.get("source")

        # handle channel safely
        channel_data = livestream.get("channel") or data.get("channel")
        self.channel = ChannelData(channel_data) if channel_data else None

        # handle categories safely
        categories_data = livestream.get("categories") or data.get("categories") or []
        self.categories = [CategoryData(category) for category in categories_data]

class ChannelData:
    def __init__(self, data=None):  
        if data:
            self.id = data.get("id")
            self.username = data.get("slug")
        else:
            self.id = None
            self.username = None
            self.category = None

class CategoryData:
    def __init__(self, data=None):
        if data:
            self.id = data.get("id")
            self.category_id = data.get("category_id")  
            self.name = data.get("name") 
            self.slug = data.get("slug") 
        else:
            self.id = None
            self.category_id = None
            self.name = None
            self.slug = None
