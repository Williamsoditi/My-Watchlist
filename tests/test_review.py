import unittest
from app.models import Review

class ReviewTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Review class
    '''

    def setUp(self):
        '''
        Setup method that will run before every Test
        '''
        self.new_review = Review(1234,'Python Must Be Crazy','www.google.com','Great movie you gat here')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))

if __name__ == '__main__':
    unittest.main()