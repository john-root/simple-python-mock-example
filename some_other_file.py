from articles.article import Article


def do_the_thing():
    art = Article()
    return art.get_article(1)["title"]

