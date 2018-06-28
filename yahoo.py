#!/usr/bin/env python
import re
import xml.etree.ElementTree as ET
#import urllib2
import requests, urllib3, sys
from bs4 import BeautifulSoup
import unittest
from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver

def get_historical_data(name):
    stock_name = name
    downloadPath = '/home/wchang/Downloads/data'
#    url = "https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch"    
    url = "https://finance.yahoo.com/quote/" + stock_name + "?p=" + stock_name + "&.tsrc=fin-srch"
#    driver = webdriver.Firefox(executable_path="/usr/bin/geckodriver")
#    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
#    webdriver.FirefoxProfile()
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", downloadPath)
    profile.set_preference("browser.helperApps.neverAsk.openFile", "text/csv,application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml")
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv,application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml")
    profile.set_preference("browser.helperApps.alwaysAsk.force", False)
    profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
    profile.set_preference("browser.download.manager.focusWhenStarting", False)
    profile.set_preference("browser.download.manager.useWindow", False)
    profile.set_preference("browser.download.manager.showAlertOnComplete", False)
    profile.set_preference("browser.download.manager.closeWhenDone", False)
    desiredCapabilities = DesiredCapabilities.FIREFOX.copy()
    desiredCapabilities['firefox_profile'] = profile.encoded
    driver = webdriver.Firefox(capabilities=desiredCapabilities)
    # firefoxProfile = webdriver.FirefoxProfile()  
    # firefoxProfile.set_preference("browser.download.folderList",2)
    # firefoxProfile.set_preference("browser.download.manager.showWhenStarting", False)
    # firefoxProfile.set_preference("browser.download.manager.showAlertOnComplete", False)
    # firefoxProfile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/force-download")
    # firefoxProfile.set_preference("browser.download.dir", "~/Downloads")
    # firefoxProfile.update_preferences()
    # driver = webdriver.Firefox(firefox_profile="/tmp/tmpAtsIRF", executable_path="/usr/bin/geckodriver")
    # print driver.firefox_profile.path
    #webdriver.FirefoxProfile().set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
    
    # options = Options();
    # options.set_preference("browser.download.folderList",1);
    # options.set_preference("browser.download.manager.showWhenStarting", False);
    # options.set_preference("browser.download.dir","~/Downloads");
    # options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/csv");
    # driver = webdriver.Firefox(executable_path="/usr/bin/geckodriver", firefox_options=options);

    try:
        driver.get(url)
#        print "Page is ready!"
    except TimeoutException:
 #       print "Loading took too much time!"
        print "Page loading is done"
    time.sleep(2.5)
#    print "Finding tag span Done"
    button_elm_lists = driver.find_elements_by_tag_name("button")
    for button_elm in button_elm_lists:
        try:
            if button_elm.get_attribute("class") == "Bd(0) P(0) O(n):f D(ib) Fz(s) Fl(end) Mt(6px) Mend(8px) close":
                button_elm.click()
                break
        except:
            pass
    
    elm_lists = driver.find_elements_by_tag_name("span")
    for elm in elm_lists:
        try:        
#               print elm.get_attribute('href'), elm.text
            if elm.text == "Historical Data":
                print "Found Historical Data Button"
#                print elm.text
                elm.click()
                time.sleep(2.5)
                len_of_input_elm = 0
                while len_of_input_elm < 5:
                    input_elm_lists = driver.find_elements_by_tag_name("input")
                    len_of_input_elm = len(input_elm_lists)
#                print len(input_elm_lists)
                for input_elm in input_elm_lists:
                     if input_elm.get_attribute("class") == "C(t) O(n):f Tsh($actionBlueTextShadow) Bd(n) Bgc(t) Fz(14px) Pos(r) T(-1px) Bd(n):f Bxsh(n):f Cur(p) W(190px)":
                         print "find right input tag"
#                         print input_elm.get_attribute("data-test")
                         input_elm.click()
                         time.sleep(2.5)
                         elm = driver.find_element_by_name("startDate")
                         print "Input startDate"
                         elm.clear()
                         elm.send_keys("6/25/2012")
                         elm = driver.find_element_by_name("endDate")
                         print "Input endDate"
                         elm.clear()
                         elm.send_keys("6/25/2015")
                         break
                button_elm_lists = driver.find_elements_by_tag_name("button")
#                print len(button_elm_lists)
                for button_elm in button_elm_lists:
                        if button_elm.get_attribute("class") == " Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Miw(80px)! Fl(start)":
                            print "Found Done"
                            button_elm.click()
                            time.sleep(2.5)                
      
# #                    print input_elm.get_attribute("class")
#                             break
                            break
            button_elm_lists = driver.find_elements_by_tag_name("button")
            for button_elm in button_elm_lists:
                if button_elm.get_attribute("class") == " Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Fl(end)":
                    print "Found Apply"
                    button_elm.click()
                    time.sleep(5.5)
                    break
        except:
            pass
    a_elm_lists = driver.find_elements_by_tag_name("a")
    for a_elm in a_elm_lists:
        if a_elm.get_attribute("class") == "Fl(end) Mt(3px) Cur(p)":
            print "get download link"
            url = a_elm.get_attribute('href')
            print url
            a_elm.click()
            break
#    driver.get(url)
#    driver.find_element(By.LINK_TEXT, 'smilechart.xls').click()
    time.sleep(2)
    driver.close()
get_historical_data('amzn')     
#     button_elm_lists = driver.find_elements_by_tag_name("button") 
#     for button_elm in button_elm_lists:
#         if button_elm.get_attribute("class") == " Bgc($c-fuji-blue-1-b) Bdrs(3px) Px(20px) Miw(100px) Whs(nw) Fz(s) Fw(500) C(white) Bgc($actionBlueHover):h Bd(0) D(ib) Cur(p) Td(n)  Py(9px) Fl(end)":
#             print "Click at  Apply"
#             button_elm.click()
#             time.sleep(2.5)                
#     #                   print input_elm.get_attribute("class")
#             break
#     url = driver.current_url
#     print url
#     table_elm_lists = driver.find_elements_by_tag_name("table")
#     for table_elm in table_elm_lists:
#         if table_elm.get_attribute("class") == "W(100%) M(0)":
#  #           print  "find right table"
#             tbody_elm = table_elm.find_element_by_tag_name("tbody")
#             tr_elm  = driver.find_element_by_xpath("//tr[@class='BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)']")
# #            tr_elm  = driver.element_by_xpath("//p[@class='Py(10px) Pstart(10px)']/following-sibling::p")           
# #            tr_elm_lists = tbody_elm.find_elements_by_tag_name("tr")
# #            print "length of tr" + str(len(tr_elm_lists))
#  #           for row_elm in tr_elm_lists:
#             row_string="  "
#             cell_elm_lists = tr_elm.find_elements_by_tag_name("td")
# #                   print cell_elm.get_attribute("class")
#             # for cell_elm in cell_elm_lists:
#             #     row_string = row_string + " " + cell_elm.find_element_by_tag_name("span").text
#             # print row_string
# 
# #             tr_elm  = driver.find_element_by_xpath("//tr[@class='BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)']/following-sibling::tr")
# #             row_string="  "
# #             for cell_elm in tr_elm.find_elements_by_tag_name("td"):
# # #                   print cell_elm.get_attribute("class")
# #                 row_string = row_string + " " + cell_elm.find_element_by_tag_name("span").text
# #            print row_string
#             
#             for i in xrange(1,99):
#                 
#                 locator  = "//tr[@class='BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)']/following-sibling::tr[" + str(i) + "]"
#                 print i, locator
#                 tr_elm  = driver.find_element_by_xpath(locator)
#                 # time.sleep(2)
#                 # tr_elm.click()
#                 # time.sleep(2)
#                 # tr_elm.send_keys(Keys.PAGE_DOWN)
#                 # time.sleep(2)
#                 row_string="  "
#                 for cell_elm in tr_elm.find_elements_by_tag_name("td"):
#     #                   print cell_elm.get_attribute("class")
#                     row_string = row_string + " " + cell_elm.find_element_by_tag_name("span").text
#                 print row_string
# #            locator  = "//tr[@class='BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)']/following-sibling::tr[" + str(99) + "]"
# #            tr_elm = driver.find_element_by_xpath(locator)
#             for i in xrange(1,99):
# 
#                 print i, locator
#                 locator  = "//tr[@class='BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)']/following-sibling::tr[99]/following-sibling::tr[" + str(i) + "]"
#                 tr_elm  = driver.find_element_by_xpath(locator)
#                 # time.sleep(2)
#                 # tr_elm.click()
#                 # time.sleep(2)
#                 # tr_elm.send_keys(Keys.PAGE_DOWN)
#                 # time.sleep(2)
#                 row_string="  "
#                 for cell_elm in tr_elm.find_elements_by_tag_name("td"):
#     #                   print cell_elm.get_attribute("class")
#                     row_string = row_string + " " + cell_elm.find_element_by_tag_name("span").text
#                 print row_string
#             
#             break
#             tr_elm  = driver.find_element_by_xpath("//tr[@class='BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)']/following-sibling::tr[2]")
#             row_string="  "
#             for cell_elm in tr_elm.find_elements_by_tag_name("td"):
# #                   print cell_elm.get_attribute("class")
#                 row_string = row_string + " " + cell_elm.find_element_by_tag_name("span").text
#             print row_string            
    # try:
    #     driver.get(url)
    # except:
    #     print "get url failed"
    # time.sleep(5.5)
    # try:
    #     source = driver.page_source.get.text()
    # except:
    #     print "covert to source failed"
    # print source.prettify()
    # soup = BeautifulSoup(source, "html.parser")
    # rows_total = soup.find("tbody").find_all("tr")
    # for row in rows_total[1::]:
    #     cells = row.findAll("td")
    #     cell_string = ""
    #     for cell in cells:
    #         cell_string = cell + " " + cell_string
    #     print cell_string
            
    
            
    #print soup.prettify()
    

