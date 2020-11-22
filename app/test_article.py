import unittest
from models import article

Article = article.Article

class TestArticle(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Method that run before each test case
        '''
        self.new_article = Article("abc", "covid", "blablablaa", "http", "http", "2020")

    def test_init(self):
        '''
        Test case that test if an article is initialized
        '''

        self.assertEqual("abc", self.new_article.source_name)
        self.assertEqual("covid", self.new_article.article_title)

if __name__=='__main__':
    unittest.main()