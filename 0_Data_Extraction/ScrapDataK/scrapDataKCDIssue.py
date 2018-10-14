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
import pandas as pd
import pickle
import re
import sys
sys.path.append("/Users/Rohan/Desktop/3rdAug/NLP/0_Data_Extraction/ScrapDataK")
from WebDriver import WebDriver

url = "http://www.gita-society.com/bhagavadgita_children.html"

def getConversation(links):
    
    
    try:
        
        qDict = dict()
        aDict = dict()
    
        for chapid, chapter in enumerate(links, start = 1):
            
            browser = WebDriver("PhantomJS")
            browser.driver.get(chapter)
            soup = BeautifulSoup(browser.driver.page_source)
            paratext = soup.find_all('p')
            data =[]
            for text in paratext:
                
                text = processText(text.get_text())
                data.append(text)
                
            tempQDict, tempADict = makeQADict(data, chapid)
            qDict.update(tempQDict)
            aDict.update(tempADict)
            
        with open("/Users/Rohan/Desktop/3rdAug/NLP/0_Data_Extraction/ScrapDataK/dataQ.pkl", "wb") as f:
            pickle.dump(qDict, f, protocol=pickle.HIGHEST_PROTOCOL)
        
        with open("/Users/Rohan/Desktop/3rdAug/NLP/0_Data_Extraction/ScrapDataK/dataA.pkl", "wb") as f:
            pickle.dump(aDict, f, protocol=pickle.HIGHEST_PROTOCOL)
        
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
        links = browser.driver.find_elements_by_class_name("blacklinks")
        
        # preprocessing links
        links = preprcesslinks(links)
        print(links[:18]) # exclude the last link: :-C It is paid!
        
        return links[:18]
        
    except (HTTPError, AttributeError) as e:
        
        print("Error:", e)
        
    finally:
        
        browser.driver.quit()
    
def preprcesslinks(links):
    
    chapters = list()
    for link in links:
        
        chapters.append(link.get_attribute('href'))
    
    return chapters
    
def processText(text):
    
    pattern = r"[\s\s]+"
    regex = re.compile(pattern)
    processedtext = regex.sub(" ", text)
    return processedtext


def makeQADict(data, chapid):
    
    qDict = dict()
    aDict = dict()
    
    qKeyPref = str(chapid)+"Q"
    aKeyPref = str(chapid)+"A"

    qkey = 1
    akey = 1
    
    
    for question in data:
        
        if question.startswith('Jai: ') and len(question) > 1:
            key = qKeyPref+str(qkey)
            
            value = question.replace("Jai: ","")
            qDict[key] = value
            qkey += 1
    
    
    for answer in data:
        
        if (answer.startswith('Grandma: ') or answer.startswith(' ')) and len(answer) > 1:
            key = aKeyPref+str(akey)
            value = answer.replace("Grandma: ","")
            aDict[key] = value
            akey += 1
    
    return qDict, aDict
            


    
if __name__ == "__main__":
    
    print("Fetching Conversation:")
    start_time = time.time()
    browser = WebDriver("PhantomJS") # you can give three options here 1.Firefox 2.ChromeDriver 3.PhantomJS
    links = getlinks(browser)
    getConversation(links)
    print("DONE!! Execution Time: ", time.time() - start_time, "secomds")
    
	
	