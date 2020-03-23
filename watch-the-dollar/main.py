# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as BS
import time
import smtplib


class CURRENCY():
    DollarRub = "https://www.google.com/search?sxsrf=ALeKk02fgf59mruV4QLACGUX1ca5K5CYCg%3A1584906851515&ei=Y8J3Xu7_HsqLmwWAv4vACQ&q=dollar+to+rub&oq=dolla&gs_l=psy-ab.1.0.0i67l3j0i131i67j0i131i20i263j0i67l2j0i131l2j0i67.4877.6293..8083...0.1..0.178.780.0j5......0....1..gws-wiz.......0i71j35i39j0.MJvTEu-saoo"
    Headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    
    cur_converted_value = 0
    
    def __init__(self, difference= 3):
        self.cur_converted_value = float(self.CHECK())
        #by default difference is 3rub, but it may be customized as user need
        self.DIF = difference
        self.date = str(time.ctime())
        
    
    def CHECK(self):
        self.full_page = requests.get(self.DollarRub, headers=self.Headers)   
        soup = BS(self.full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class":"DFlfde SwHCTb", "data-precision":"2"}) 
        return str(convert[0].text).replace(",", ".")
    
        
    def value_out(self):
        currency = float(self.CHECK())
        
        #Here is warning about changes >= difference
        design = "-" * 100
        if currency >= self.cur_converted_value + self.DIF:
            print("!!! WARNING !!!")
            print("Big fall of ₽")

            t_dif = currency - self.cur_converted_value
            additional_text = "Watch out for $/₽ jumps/falls!\n\n  Since {} price for 1$ has grown by {}₽.\n  For now 1$ equals {}₽\n\n{}\n If you wish to be informed about less or more significant changes in currency\nREPLY to this email and describe size of changes you'd prefer to know about".format(self.date, t_dif, currency, design)
            additional_text = ''.join(additional_text)#.encode('utf-8')
            fall = "-- Big fall of ₽"
            
            self.SEND(additional_text, fall)
            
            self.cur_converted_value = currency
            self.date = str(time.ctime())
            
        elif currency <= self.cur_converted_value - self.DIF:
            print("!!! WARNING !!!")
            print("Big jump of ₽")
            
            t_dif = self.cur_converted_value - currency
            additional_text = "Watch out for $/₽ jumps/falls!\n\n  Since {} price for 1$ has fallen by {}₽.\n  For now 1$ equals {}₽\n\n{}\nIf you wish to be informed about less or more significant changes in currency reply to this email and describe size of changes you'd prefer to know about".format(self.date, t_dif, currency, design)
            additional_text = ''.join(additional_text)#.encode('utf-8')
            jump = "-- Big jump of ₽"
            
            self.SEND(additional_text, jump)
            
            self.cur_converted_value = currency
            self.date = str(time.ctime())
            
        soup = BS(self.full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class":"DFlfde SwHCTb", "data-precision":"2"})
        
        print("-" * 10)
        print(time.ctime())
        print("for now")
        print("1$ equals", str(currency).replace(".", ",") + "₽")
        print()
        
        time.sleep(60 * 30)
        self.value_out()
        
        
        
    def SEND(self, text, sub):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        #write your mail adress here  and  put the password that you get from google
        server.login("ix2.evdokimov@gmail.com", "rtcbevadisynmtxg")
        
        #pripare message to warn you about currensy changings 
        subject = "!Currency" + sub
        body = text
        message = 'Subject:{}\n\n{}'.format(subject, body)
        
        server.sendmail("ix2.evdokimov@gmail.com", ["ix2.evdokimov@gmail.com", "i_a_evdokimov@gmail.com", "fedor.ig.evdokimov@gmail.com", "gumbin.maksim@yandex.ru"], message)
        
        server.quit()
        
        

    
start = CURRENCY()
start.value_out()
