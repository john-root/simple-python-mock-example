import unittest
import mock
from articles.fake_article import FakeArticle
import some_other_file

class ServerTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_do_the_thing(self):

        with mock.patch('some_other_file.Article') as ArticleMockClass:
            ArticleMockClass.return_value = FakeArticle()
            result = some_other_file.do_the_thing()
            self.assertEquals(result, "The test title")
