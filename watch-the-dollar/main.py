# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as BS
import time


class CURRENCY():
    dollar_rub = "https://www.google.com/search?sxsrf=ALeKk02fgf59mruV4QLACGUX1ca5K5CYCg%3A1584906851515&ei=Y8J3Xu7_HsqLmwWAv4vACQ&q=dollar+to+rub&oq=dolla&gs_l=psy-ab.1.0.0i67l3j0i131i67j0i131i20i263j0i67l2j0i131l2j0i67.4877.6293..8083...0.1..0.178.780.0j5......0....1..gws-wiz.......0i71j35i39j0.MJvTEu-saoo"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    
    cur_converted_value = 0
    
    def __init__(self):
        self.cur_converted_value = CHECK()
    
    def CHECK(self):
        full_page = requests.get(dollar_rub, headers=headers)
        #print(full_page.content)        
        soup = BS(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class":"DFlfde SwHCTb", "data-precision":"2"}) 
        return convert[0].text
        
    def value_out(self):
        soup = BS(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class":"DFlfde SwHCTb", "data-precision":"2"})
        print("-" * 10)
        print(time.ctime())
        print("for now 1$ equals")
        print(CHECK() + "₽")
        print()
        time.sleep(60)
        CHECK()
        
    
    CHECK()