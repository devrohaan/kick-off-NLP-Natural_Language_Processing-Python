#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:00:10 2018

@author: Rohan

This class gets the instance of specified web driver.

"""

from selenium import webdriver


class WebDriver(object):
	
	def __init__(self,drivername):
		
		if drivername == 'Firefox':
			self.driver = webdriver.Firefox()
		elif drivername == 'ChromeDriver':
			self.driver = webdriver.Chrome(r"/usr/local/bin/chromedriver")  # provide the chromedriver binaries in case of error
		elif drivername == 'PhantomJS':
			self.driver = webdriver.PhantomJS(r"/usr/local/bin/phantomjs")  # provide the phantomjs binaries in case of error
			
	
		#self.driver = driver.implicitly_wait(20) 
		#This tells Selenium that we would like it to wait for a certain amount of time before throwing an exception that if it cannot find the element on the page. 
	


