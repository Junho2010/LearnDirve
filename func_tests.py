from selenium import webdriver
br = webdriver.Firefox()
br.get('http://127.0.0.1:8000')
assert 'Django' in br.title


