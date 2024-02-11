from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse


class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='user1')
        cls.post1=Post.objects.create(
            title='post1',
            text='this is the description of post1',
            status=Post.STATUS_CHOICES[0][0],
            author=cls.user
        )
        cls.post2=Post.objects.create(
            title='post2',
            text='this is the description of post2',
            status=Post.STATUS_CHOICES[1][0],
            author=cls.user
        )

    def test_post_list_url_by_name(self):
        response=self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_url(self):
        response=self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_blog_list_post(self):
        response=self.client.get(reverse('post_list'))
        self.assertContains(response,self.post1.title)

    def test_post_detail_on_blog_detail_post(self):
        response=self.client.get('/blog/1/')
        self.assertContains(response,self.post1.text)

    def test_post_detail_url_by_name(self):
        response=self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_draft_post_not_show_in_post_list(self):
        response=self.client.get(reverse('post_list'))
        self.assertContains(response,self.post1.title)
        self.assertNotContains(response,self.post2.title)

    def test_post_model_str(self):
        self.assertEqual(str(self.post1),self.post1.title)

    def test_post_create_view(self):
        response=self.client.post(reverse('post_create'),{
            'title': 'some title',
            'text': 'some text',
            'status': 'pub',
            'author': self.user,
        })
        # self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'some title')
    #
    # def test_post_update_view(self):
    #     response=self.client.post(reverse('post_update', args=[self.post1.id]), {
    #         'title': 'some title1 updated',
    #         'text': 'some text updated',
    #     })
    #     self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response=self.client.post(reverse('post_delete', args=[self.post1.id]))
        self.assertEqual(response.status_code, 302)