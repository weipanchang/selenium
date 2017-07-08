#!/usr/bin/env python

#import MySQLdb
import requests, urllib3, sys
from bs4 import BeautifulSoup
import unittest
from selenium import webdriver
import time
 
class PingShow_test(unittest.TestCase):
     def setUp(self):
          self.url =  "http://99.43.90.10/login_page"
          # create a new Firefox session
          self.driver = webdriver.Firefox()
          self.driver.implicitly_wait(30)
  #        self.driver.maximize_window()
          # navigate to the application home page
          self.driver.get(self.url)
 
     def test_log_on(self):
         # get the search textbox
         
          elm_lists = self.driver.find_elements_by_tag_name("a")
          for elm in elm_lists:
#              print elm.get_attribute('href'), elm.text
               if elm.get_attribute('href') == "http://99.43.90.10/login_page/login.php":
                    elm.click()
                    self.url = elm.get_attribute('href')
#                    print self.url
                    time.sleep(5.5)
                    break
#          self.driver.get(self.url)
          self.assertIn('Login', self.driver.title)
#          time.sleep(5.5)
#         self.driver.get(self.url)
          username = self.driver.find_element_by_id("username")
          password = self.driver.find_element_by_id("password")
          username.send_keys("wchang")
          password.send_keys("Lonna821")
          # login_attempt = self.driver.find_element_by_xpath("//*[@type='submit']")
          # login_attempt.submit()
          login_attempt = self.driver.find_element_by_name("Submit")
          login_attempt.submit()
          time.sleep(5.5)
          print self.driver.current_url
          self.assertIn('Home page', self.driver.title)
          
   
     def tearDown(self):
          # close the browser window
          self.driver.quit()
          
if __name__ == '__main__':
    unittest.main()          