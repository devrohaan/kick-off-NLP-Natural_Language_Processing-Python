#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:00:10 2018

@author: Rohan

Simple Python Web Scraper: English Premier League score table updates

Script Requirements: Python3, BeautifulSoup, Selenium, PhantomJS, csv, time, pandas, tabulate, pickle

"""
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from time import sleep
import time
import pickle
import re
import sys
sys.path.append("/Users/Rohan/Desktop/3rdAug/NLP/0_Data_Extraction/Eg_Data_Extraction_WebScarping")
from WebDriver import WebDriver

url = "https://www.worldclasslearning.com/akbar-birbal-stories/index.html"

def getStories(links):
    
    
    try:
        
        data = list()
        for chapid, storylink in enumerate(links, start = 1):
            
            browser = WebDriver("PhantomJS")
            browser.driver.get(storylink)
           
            story = browser.driver.find_elements_by_xpath("//div[@class='main-content']/p")
            #browser.driver.find_element_by_class_name("main-content")
            storyString = ""
            for text in story:
                text = processText(text.text)
                storyString += text
            
            data.append(storyString)
            
        with open("/Users/Rohan/Desktop/3rdAug/NLP/0_Data_Extraction/Story.pkl", "wb") as f:
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
        
        return data
        '''
        with open('filename.pickle', 'rb') as handle:
            unserialized_data = pickle.load(handle)
        '''        
        
    except (HTTPError, AttributeError) as e:
            
            print("Error:", e)
        
    finally:
        browser.driver.quit()
    

def getlinks(browser):
    
    try:
        print("Fetching Links: ")
        browser.driver.get(url)
        links = browser.driver.find_elements_by_xpath("//li/a")
        # find_element_by_link_text can be used too!
        
        # preprocessing links
        links = preprcesslinks(links)
        # exclude the last link: :-C It is paid!
        
        return links[:len(links)-1] # Eliminate the last useless link! 
        
    except (HTTPError, AttributeError) as e:
        
        print("Error:", e)
        
    finally:
        
        browser.driver.quit()
    
def preprcesslinks(links):
    
    chapters = list()
    for link in links:
        
        #print(link.text) # Store title if needed!
        #print(link.get_attribute('href'))
        chapters.append(link.get_attribute('href'))
    
    return chapters
    
def processText(text):
    
    pattern = r"[\n]+"
    regex = re.compile(pattern)
    processedtext = regex.sub(" ", text)
    return processedtext



    
if __name__ == "__main__":
    
    print("Fetching Data")
    start_time = time.time()
    browser = WebDriver("PhantomJS") # you can give three options here 1.Firefox 2.ChromeDriver 3.PhantomJS
    links = getlinks(browser)
    data = getStories(links)
    print("Stories Fetched: ",len(data))
    print("DONE!! Execution Time: ", time.time() - start_time, "secomds")
    
	
"""
Output:
    
Fetching Links: 
Stories Fetched:  56
DONE!! Execution Time:  421.83614802360535 secomds

"""