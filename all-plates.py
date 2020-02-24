#!/usr/bin/env python
import string
from os import system
import sys
import time

#for i in range(1,9):
#    print("{:03}".format(i))

#for letter in string.ascii_lowercase:
#    print(letter)

list_letter1 = []
list_letter1 = string.ascii_lowercase
list_letter2 = list_letter1
list_letter3 = list_letter1
list_letter4 = list_letter1



import time
import urllib.request
import urllib
import bs4
from urllib import request
from os import system


def plaque_format(plaque_raw):
    plaque = ''
    # Remove spaces and '-'
    plaque_raw = plaque_raw.replace(' ', '')
    plaque = plaque_raw.replace('-', '')
    return(plaque)

def yak_parse(url_yak):
    # Define the url then specify a specific User-Agent for the read() request
    req_yak = urllib.request.Request(url=url_yak, method='POST', headers={'User-Agent': 'Mozilla/5.0'})
    req_yak_text = request.urlopen(req_yak).read()

    page_yak = bs4.BeautifulSoup(req_yak_text, "lxml")

    # Parse page_yak then find the <h2 class="title-car>" HTML tag
    for item_yak in page_yak.findAll("h2", {"class" : "title-car"}):
        # Grab only the text without HTML tag
        if item_yak.get("class") :
            return(item_yak.getText())


for ltr4 in list_letter4:
    for ltr3 in list_letter3:
        for ltr2 in list_letter2:
            for ltr1 in list_letter1:
                for i in range(1, 999):
                    num1 = ("{:03}".format(i))
                    plate = (ltr4 + ltr3 + num1 + ltr2 + ltr1)
                    if plate == 'aa010aa':
                        print("finished")
                        sys.exit()
                    else:
                        time.sleep(30)
                        #print(plate + ": ")
                        try:
                            print(plate + ": " + yak_parse(
                            "https://www.yakarouler.com/car_search/immat?immat=" + plate + "&name=undefined&redirect=true"))
                        except:
                            print(plate + ": No response")

#print("YAKAROULER: " + yak_parse("https://www.yakarouler.com/car_search/immat?immat=" + plate + "&name=undefined&redirect=true"))
