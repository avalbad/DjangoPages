from django.test import TestCase
from posts.models import post
from django.urls import reverse


# add post
class PostModelTest(TestCase):

    def setUp(self):
        post.objects.create(text="just a test")

    def test_text_content(self):
        ost = post.objects.get(id=1)
        expected_object_name = f'{ost.text}'
        self.assertEqual(expected_object_name, "just a test")



# http://127.0.0.1:8000/post/
class HomePageViews(TestCase):
    def setUp(self):
        post.objects.create(text = 'This is another test')

    
    def test_views_url_locationa(self):
        resp = self.client.get('/posts/')
        self.assertEqual(resp.status_code,200)

# urls post_list
    def test_views_url_name(self):
        resp = self.client.get(reverse("posts:post_list"))
        self.assertEqual(resp.status_code,200)



# test template_html
    def test_views_template(self):
        resp = self.client.get(reverse("posts:post_list"))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,'posts/list.html')