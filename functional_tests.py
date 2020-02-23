from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # We got an open the browser
        self.browser.get('http:localhost:8000')

        # The title mentions To-DO
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # We invited to enter a to-do item straight away

        # We type "Buy peacock feathers" into a text box

        # When we hit enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item. We
        # enters "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on the list

        # We wonder whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for us -- there is some
        # explanatory text to that effect.

        # We visits that URL - the to-do list is still there.

        # Satisfied, we goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')