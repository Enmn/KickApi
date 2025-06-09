# kickapi/clip_data.py
class ClipCreator:
    def __init__(self, data):
        self.id = data.get("id")
        self.username = data.get("username")
        self.slug = data.get("slug")

    def __repr__(self):
        return f"<ClipCreator id='{self.id}' username='{self.username}'>"
    
class ClipCategory:
    def __init__(self, data):
        self.id = data.get("id")
        self.name = data.get("name")
        self.slug = data.get("slug")

    def __repr__(self):
        return f"<ClipCategory category='{self.slug}'>"

class ClipData:
    def __init__(self, data):
        self.id = data.get("id")
        self.title = data.get("title")
        self.thumbnail = data.get("thumbnail_url")
        self.stream = data.get("clip_url")
        self.duration = data.get("duration")
        self.views = data.get("views")
        self.created_at = data.get("created_at")
        self.creator = ClipCreator(data.get("creator", {}))  # Use the nested class
        self.category = ClipCategory(data.get("category", {}))  # Use the nested class

    def __repr__(self):
        return f"<ClipData id='{self.id}' title='{self.title}'>"
