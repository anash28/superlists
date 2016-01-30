from selenium import webdriver
import unittest

class NewVisitor(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
<<<<<<< HEAD
        self.browser.implicitly_wait(3)
=======
>>>>>>> 2ce0396db2c9d2ce87f0327165fc0577268e75e1
    def tearDown(self):
        self.browser = webdriver.quit()
    def tests_can_start_a_list_and_retrive_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes to
        #check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" in to a text box (Edith`s hobby
# is tying fly-fishing lures )

# When she hits enter, the page updates, and the pages lists
# "1: Buy peacock features " as an item in a to-do list

# There is a text box inviting her to add another item. She
# enters "Use peacock features to make a fly " (Edith is very methodical)

# The page updates again, and now shows both items on her list

# Edith wonders whether the site with rememeber her list. Then she sees that
# the site has generated a unique URL for her -- there is some explanatory text
# to that effect

# She visits that URL - her to-do list is still there

# Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings ='ignore')

browser.quit()
