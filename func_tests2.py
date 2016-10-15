from selenium import webdriver
import unittest

class NewVisionTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_cat_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('To_Do',self.browser.title)
        self.fail('Finish the Test!')

if __name__=='__main__':
    unittest.main(warnings='ignore')
'''
br = webdriver.Firefox()
br.get('http://127.0.0.1:8000')
assert 'Django' in br.title
'''

