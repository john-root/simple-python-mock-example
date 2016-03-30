import unittest
import mock
from articles.test_article import Article
import some_other_file

class ServerTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_do_the_thing(self):

        with mock.patch('some_other_file.Article') as ArticleMockClass:
            ArticleMockClass.return_value = Article()
            result = some_other_file.do_the_thing()
            self.assertEquals(result, "The test title")
