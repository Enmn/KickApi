# kickapi/chat_data.py
class ChatMessage:
    def __init__(self, data):
        # Initialize chat message attributes
        self.text = data.get("content", "")
        self.sender = ChatSender(data.get("sender", {}))
        self.date = data.get("created_at", "")

class ChatSender:
    def __init__(self, data):
        # Initialize chat sender attributes
        self.username = data.get("username", "")
        self.user_id = data.get("id", "")

class ChatData:
    def __init__(self, data):
        # Initialize chat data attributes
        self.messages = [ChatMessage(message) for message in data.get("data", {}).get("messages", [])]