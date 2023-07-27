from django.test import TestCase , SimpleTestCase

# Create your tests here.
 
class SimpleTest(SimpleTestCase):
    def test_home_page_status_code(self):
        respons = self.client.get('/')
        self.assertEqual(respons.status_code,200)

    def test_about_status_code(self):
        respons = self.client.get('/about/')
        self.assertEqual(respons.status_code,200)
        
    # def TestPosts(self):
    #     respons = self.client.get('/posts/')
    #     self.assertEqual(respons.status_code,200)