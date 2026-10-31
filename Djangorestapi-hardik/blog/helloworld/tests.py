from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from .models import BlogPost


class BlogPostAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.other_user = User.objects.create_user(
            username='otheruser',
            password='testpassword'
        )

        self.client.login(
            username='testuser',
            password='testpassword'
        )

    def test_create_post(self):
        response = self.client.post(
            '/api/posts/',
            {
                'title': 'Test Post',
                'content': 'Test Content'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            BlogPost.objects.count(),
            1
        )

    def test_list_posts(self):
        BlogPost.objects.create(
            author=self.user,
            title='Test Post',
            content='Test Content'
        )

        response = self.client.get('/api/posts/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_only_sees_own_posts(self):
        BlogPost.objects.create(
            author=self.user,
            title='My Post',
            content='My Content'
        )

        BlogPost.objects.create(
            author=self.other_user,
            title='Other Post',
            content='Other Content'
        )

        response = self.client.get('/api/posts/')

        self.assertEqual(
            response.data['count'],
            1
        )