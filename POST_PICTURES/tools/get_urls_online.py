# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 18:16:28 2023

@author: mimounid


Une fois que j'ai upload les photos en ligne sur https://paris-pics-aesthetic.blogspot.com/2023/10/blog-post_30.html
Il faut que je trouve les urls de chaque photos stockée en ligne

"""
import pandas as pd
import numpy as np 
import os
import time
from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
#from requests_html import HTMLSession
import winsound    
import datetime

from seleniumbase import Driver

browser = Driver(uc=True, incognito=True)
#charger la page
url = 'https://paris-pics-aesthetic.blogspot.com/2023/10/blog-post_30.html'
browser.get(url)

xp = "//a[contains(@href, 'googleusercontent')]"
liste = browser.find_elements(By.XPATH, xp)
list_urls = [u.get_attribute("href") for u in liste]
df = pd.DataFrame({'image_urls':list_urls})
df.to_csv('list_urls.csv')

