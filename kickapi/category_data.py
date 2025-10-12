# kickapi/category_data.py
class BannerData:
    def __init__(self, data: dict):
        self.responsive = data.get("responsive")
        self.url = data.get("url")

class CategoryInfo:
    def __init__(self, data: dict):
        self.id = data.get("id")
        self.name = data.get("name")
        self.slug = data.get("slug")
        self.icon = data.get("icon")

class SubCategoryData:
    def __init__(self, data: dict):
        self.id = data.get("id")
        self.category_id = data.get("category_id")
        self.name = data.get("name")
        self.slug = data.get("slug")
        self.tags = data.get("tags", [])
        self.description = data.get("description")
        self.is_mature = data.get("is_mature", False)
        self.is_promoted = data.get("is_promoted", False)
        self.viewers = data.get("viewers", 0)
        self.is_fallback = data.get("is_fallback", False)

        # nested objects
        self.banner = BannerData(data.get("banner", {})) if data.get("banner") else None
        self.category = CategoryInfo(data.get("category", {})) if data.get("category") else None

class CategoryResponse:
    def __init__(self, data: dict):
        # pagination info
        self.current_page = data.get("current_page")
        self.first_page_url = data.get("first_page_url")
        self.last_page = data.get("last_page")
        self.last_page_url = data.get("last_page_url")
        self.next_page_url = data.get("next_page_url")
        self.prev_page_url = data.get("prev_page_url")
        self.per_page = data.get("per_page")
        self.total = data.get("total")

        # subcategories
        self.data = [SubCategoryData(item) for item in data.get("data", [])]

        # pagination links
        self.links = data.get("links", [])