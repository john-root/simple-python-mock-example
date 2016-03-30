# The "real" article entry point
# Maybe this has external (AWS) dependencies)


class Article:

    def __init__(self):
        pass

    def get_article(self, idx):
        return {
            "id": idx,
            "title": "The real title"
        }