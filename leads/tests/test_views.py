from django.test import TestCase
from django.shortcuts import reverse


class landingPageTest(TestCase):

    def test_get_request(self):
        response = self.client.get(reverse("landing-page"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing.html")
