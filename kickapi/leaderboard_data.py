# kickapi/leaderboard_data.py
class LeaderboardData:
    def __init__(self, data):
        self.gifts = [GiftsUser(user) for user in data.get("gifts", [])]
        self.gifts_week = [GiftsUser(user) for user in data.get("gifts_week", [])]
        self.gifts_month = [GiftsUser(user) for user in data.get("gifts_month", [])]

class GiftsUser:
    def __init__(self, data):
        self.user_id = data.get("user_id")
        self.username = data.get("username")
        self.quantity = data.get("quantity", 0)