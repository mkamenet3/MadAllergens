#Code to scrape allergy data website daily
##Written in Python 3
##Run on Bash on Ubuntu on Windows


#Import Modules
import urllib
import json
import re
from bs4 import BeautifulSoup


def extract_grasspollen(idx_grasspollen, data):
    """This function will further clean grasspollen into useable lists"""




def scrape(website):
    """This function will download the weather file, extract necessary sections of the javascript file and then convert it to text for easier further processing"""
    #Create Empty
    grasspollen_status = []
    grasspollen_cat = []
    grasspollen_label = []
    
    treepollen_status = []
    treepollen_cat = []
    treepollen_label = []
    
    moldpollen_status = []
    moldpollen_cat = []
    moldpollen_label = []
    
    dust_status = []
    dust_cat = []
    dust_label = []
    
    airquality_status = []
    airquality_cat = []
    airquality_label = []
       
    
    #Download
    web = urlopen(website)
    soup = BeautifulSoup(web.read(), 'lxml')
    data = soup.find_all("script")[9].string.split(",")
    
    idx_grasspollen = [ i for i, word in enumerate(data) if re.search('grasspollen', word)]
    idx_treepollen = [ i for i, word in enumerate(data) if re.search('treepollen', word)]           
    idx_moldpollen = [ i for i, word in enumerate(data) if re.search('moldpollen', word)]
    idx_dust = [ i for i, word in enumerate(data) if re.search('ust &', word)]
    idx_airquality = [ i for i, word in enumerate(data) if re.search('quality', word)]
    
    








