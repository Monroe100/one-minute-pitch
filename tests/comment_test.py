from app.models import Comments,User
from app import db
import unittest

class CommentTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''
    def setUp(self):
        self.user_James = User(username = 'kajuju',password = 'kajuju', email = 'kajuju@ms.com')
        self.new_comment = Comment(pitch_id=12345,pitch_title='Review for movies',user = self.user_kajuju) 

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()


    def test_save_comment(self): 
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)
