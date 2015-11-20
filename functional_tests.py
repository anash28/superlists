from selenium import webdriver
browser = webdriver.Firefox()

# Edith has heard about a cool new online to-do app. She goes to
#check out its homepage
browser.get('http://localhost:8000')

# She notices the page title and header mention to-do lists
assert 'To-Do' in browser.title

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

browser.quit()
