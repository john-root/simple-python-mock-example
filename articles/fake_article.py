# The "fake" article entry point
# no dependencies etc.


class FakeArticle:

    def __init__(self):
        pass

    def get_article(self, idx):
        return {
            "id": idx,
            "title": "The test title"
        }