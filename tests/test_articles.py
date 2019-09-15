import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = Articles('Jennings Brown','Man Claims He Invented Bitcoin','A man who has insisted he is the man behind the pseudonymous identity of Satoshi Nakamoto','https://i.kinja-img.com/gawker-media/image/upload/s--H8pqYMUW--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/ug34lxszlekl8efydtj3.png','https://i.kinja-img.com/gawker-media/image/upload/s--H8pqYMUW--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/ug34lxszlekl8efydtj3.png','2019-08-28T16:50:00Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,Articles))


if __name__ == '__main__':
    unittest.main()