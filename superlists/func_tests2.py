#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisionTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #打开网站，标题中显示了To-Do标识待办事项。并且有一个标题提示新建
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("To-Do",header_text)

        #网页提示可以新建一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        #在输入框中输入“Buy peacock feather”
        inputbox.send_keys("Buy peacock feather")

        #按下Enter键，页面更新，在待办实现中显示“1.Buy peacock feather”
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text== '1.Buy peacock feather' for row in rows))

        self.fail('Finish the Test!')

if __name__=='__main__':
    unittest.main(warnings='ignore')
'''
br = webdriver.Firefox()
br.get('http://127.0.0.1:8000')
assert 'Django' in br.title
'''


