import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import requests as r

chrome = os.environ.get('chrome_webdriver')
driver = webdriver.Chrome(chrome)
msg = 'Mai Ek Boi Hu!!'

driver.get('https://web.whatsapp.com/')

input('Enter anything after scanning QR code: ')

source = driver.page_source

soup = bs(source, 'html.parser')

users = []

for dude in soup.findAll('span', {'class', '_19RFN _1ovWX'}):
    users.append(dude.string)

n = 0
dudes = []
for i in range(len(users)):
    if n % 2 == 0:
        dudes.append(users[i])
    n += 1

print(users, dudes)

# things = ['f7', 'F7', 'f6', 'F6', 'f8', 'F8', 'Jaypee', 'JP', 'jp']
things = ['interstellar', 'boiya', 'shawshank']

for dude in dudes:
    for thing in things:
        if dude != None:
            if thing != None:
                if thing in dude:
                    user = driver.find_element_by_xpath(
                        '//span[@title = "{}"]'.format(dude))
                    user.click()
                    message_box = driver.find_element_by_class_name('_13mgZ')

                    for i in range(10):
                        message_box.send_keys(msg)
                        button = driver.find_element_by_class_name('_3M-N-')
                        button.click()
