import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = Source('abc-news','ABC News','Your trusted source for breaking news','"https://abcnews.go.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,Source))


if __name__ == '__main__':
    unittest.main()