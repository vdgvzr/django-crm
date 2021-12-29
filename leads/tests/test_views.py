from django.test import TestCase
from django.shortcuts import reverse
from leads.models import Lead


class SignupPageTest(TestCase):
    
    def test_get_request(self):
        response = self.client.get(reverse("signup"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")


class LandingPageTest(TestCase):

    def test_get_request(self):
        response = self.client.get(reverse("landing-page"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing.html")


class ListPageTest(TestCase):

    def test_get_request(self):
        response = self.client.get(reverse("leads:lead-list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "leads/lead_list.html")

''' class DetailPageTest(TestCase):

    def setup(self):
        Lead.objects.create(id=6)

    def test_get_request(self):
        response = self.client.get(reverse("leads:lead-detail", args=(6,)), follow=True)

        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "leads/lead_detail.html") '''

class CreatePageTest(TestCase):

    def test_get_request(self):
        response = self.client.get(reverse("leads:lead-create"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "leads/lead_create.html")

''' class UpdatePageTest(TestCase):
    
    def test_get_request(self):
        pk = 1
        response = self.client.get(reverse("leads:lead-update"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "leads/lead_update.html") '''

''' class DeletePageTest(TestCase):
    
    def test_get_request(self):
        response = self.client.get(reverse("leads:lead-delete"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "leads/lead_delete.html") '''
