from django.test import TestCase
from django.contrib.auth import get_user_model
# user model^
from django.urls import reverse
# urls^
from .models import Blog




class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = "mamad",
            password ="1234",
        )
        self.user = Blog.objects.create(
            title = "title blog",
            body = "body blog",
            author = self.user,
        )



    def test_string_model(self):
        blog = Blog(title ="blog a test")
        self.assertEqual(str(blog),blog.title)


    def post_model_object(self):
        self.assertEqual(f'{self.blog.title}',"blog title")
        self.assertEqual(f'{self.blog.body}',"blog body")
        self.assertEqual(f'{self.blog.author}',"mamad")
    


    def test_list_post(self):
        response = self.client.get(reverse("blog:blog_list"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"blog/blog_list.html")

    def test_post_detail(self):
        resp = self.client.get('/blog/1/')
        no_reso = self.client.get('/bloge/3/')
        self.assertEqual(resp.status_code,200)
        self.assertEqual(no_reso.status_code,404)
        self.assertTemplateUsed(resp,"blog/detail.html")

    # def test_get_absolute_url(self):
    #     self.assertEqual(self.Blog.get_absolute_url() ,'/blog/1/')
 


    def test_creat_post(self):
        response = self.client.post(reverse("blog:new"),{
            "title":"new post",
            "body":"body post",
            "author":self.user.id
        })
        self.assertEqual(response.status_code,302)
        self.assertEqual(Blog.objects.last().title,"new post")
        self.assertEqual(Blog.objects.last().body,"body post")


    def test_update_post(self):
        response = self.client.post(reverse('blog:edit',args="1"),{
        "title":"update title",
        "body":"update body"
        })
        self.assertEqual(response.status_code,302)

    def test_delete_post(self):
        response = self.client.post(reverse("blog:delete",args="1"))
        self.assertEqual(response.status_code,302)








    
    
