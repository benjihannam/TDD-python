from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page
from lists.models import Item

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        new_list_item = 'A new list item'
        response = self.client.post('/', data={'item_text': new_list_item})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, new_list_item)

    def test_redirects_after_POST(self):
        new_list_item = 'A new list item'
        response = self.client.post('/', data={'item_text': new_list_item})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], "/lists/the-only-list-in-the-world/")

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, first_item.text)
        self.assertEqual(second_saved_item.text, second_item.text)


class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_items(self):
        # Given two saved objects
        first_item = 'item 1'
        second_item = 'item 2'
        Item.objects.create(text=first_item)
        Item.objects.create(text=second_item)

        # When we get the page
        response = self.client.get("/lists/the-only-list-in-the-world/")

        # Then: it contains the items
        self.assertContains(response, first_item)
        self.assertContains(response, second_item)