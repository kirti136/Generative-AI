import json
import unittest
from app import app

class SocialMediaAppTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True

    def test_create_and_view_post(self):
        # Create a new post
        new_post = {'username': 'Alice', 'caption': 'A great day at the beach'}
        response = self.app.post('/create_post', data=json.dumps(new_post), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        # View all posts and verify that the new post is in the list
        response = self.app.get('/view_posts')
        self.assertEqual(response.status_code, 200)
        posts = json.loads(response.data)
        self.assertTrue(any(post['username'] == 'Alice' and post['caption'] == 'A great day at the beach' for post in posts))

    def test_delete_post(self):
        # Create a new post for testing deletion
        test_post = {'username': 'Bob', 'caption': 'Testing delete functionality'}
        self.app.post('/create_post', data=json.dumps(test_post), content_type='application/json')

        # Delete the test post
        response = self.app.delete('/delete_post/1')  # Assuming the test post has ID 1
        self.assertEqual(response.status_code, 200)

        # Verify that the test post is deleted
        response = self.app.get('/view_posts')
        self.assertEqual(response.status_code, 200)
        posts = json.loads(response.data)
        self.assertFalse(any(post['username'] == 'Bob' for post in posts))

    def test_like_post(self):
        # Create a new post for testing liking
        test_post = {'username': 'Charlie', 'caption': 'Testing like functionality'}
        self.app.post('/create_post', data=json.dumps(test_post), content_type='application/json')

        # Like the test post
        response = self.app.put('/like_post/1')  # Assuming the test post has ID 1
        self.assertEqual(response.status_code, 200)

        # Verify that the post's likes count is incremented
        response = self.app.get('/view_posts')
        self.assertEqual(response.status_code, 200)
        posts = json.loads(response.data)
        liked_post = next(post for post in posts if post['username'] == 'Charlie')
        self.assertEqual(liked_post['likes'], 1)

if __name__ == '__main__':
    unittest.main()
