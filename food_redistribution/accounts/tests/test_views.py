from django.test import TestCase  # , Client
from django.urls import reverse

# from django.contrib.auth.models import User
# from accounts.models import *


class PostViewTest(TestCase):
    def test_no_posts(self):
        """
        If no posts exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("posts"))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "No polls are available.")


"""
class DetailedblogViewTest(TestCase):
    def test_detailed_post(self):

        # If you click on a post, it will show up.

        c = Client()
        user = User.objects.create_user("Annika", "annika@email.com")
        c.force_login(user=user)

        onepost = Post.objects.create(
            title = f'test title',
            author = user,
            body = f'test body',
            id = 1
        )
        #response = c.post(
        #    reverse("add-post"),
        #    data=onepost,
        #)
        response2 = self.client.get(reverse('blog-details/', args=(1,)))
        # self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.status_code, 302)
        self.assertEqual(response2.status_code, 200)
        # self.assertContains(response2, desc)
        # self.assertContains(response, "No polls are available.")
"""

"""
class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_authors = 13

        for author_id in range(number_of_authors):
            Author.objects.create(
                first_name=f'Christian {author_id}',
                last_name=f'Surname {author_id}',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalog/authors/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/author_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['author_list']), 10)

    def test_lists_all_authors(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('authors')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['author_list']), 3)
"""
