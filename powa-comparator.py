#!/usr/bin/env python
#!/usr/bin/env python
# author: Julien ESCOFFIER
# email: julien.escoffier@protonmail.com
#
# Todo:
# - add installation instructions(README.md)
# - add an addition license plate website (for informations crossing & verification)
# - add technical stats of vehicule
# - add comparator (with a saved license plate) (0-60) (400m) (1/4 mile) ...


def banner():
    print(" _________")
    print("\_   ___ \  ____   _____ ______")
    print("/    \  \/ /  _ \ /     \\____ \ ")
    print("\     \___(  <_> )  Y Y  \  |_> >")
    print("\______  /\____/|__|_|  /   __/")
    print("     ________        \/|__|")
    print("     \______ \ _____")
    print("      |    |  \\__  \ ")
    print("      |    `   \/ __ \_")
    print("_______________  (____  /")
    print("\______   \______  _  _______")
    print("|     ___/  _ \ \/ \/ /\__  \ ")
    print("|    |  (  <_> )     /  / __ \_")
    print("|____|   \____/ \/\_/  (____  /")
    print("                           \/  ")


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

#def osc_parse(url_osc):



# Test longueur de la plaque 3min(1A1) 10max(9999ZZZ999)
banner()
plaque_raw = input("Plaque: ")
while len(plaque_raw) <=3:
    print("La plaque est trop courte.")
    time.sleep(1)
    system('clear')
    banner()
    plaque_raw = input("\nPlaque: ")

while len(plaque_raw) >= 11:
    print("La plaque est trop longue.")
    time.sleep(1)
    system('clear')
    banner()
    plaque_raw = input("\nPlaque: ")

#print(plaque_format(plaque_raw))

# YAKAROULER
print("YAKAROULER: " + yak_parse("https://www.yakarouler.com/car_search/immat?immat=" + plaque_format(plaque_raw) + "&name=undefined&redirect=true"))

# PIECESAUTO.COM

# OSCARO.COM (QA in progress in scratch-oscaro.py)
#url_string_osc = 'https://www.oscaro.com/Catalog/SearchEngine/GetPlateSearchResult'
#data = "plateValue=" + plaque_format(plaque_raw) + "&genartId=null"
#data = data.encode('utf-8')
#req_osc = urllib.request.Request(url=url_string_osc, data=data, method='POST', headers={'User-Agent': 'Mozilla/5.0'})
#response_osc = urllib.request.urlopen(req_osc).read()
#print("\n\nOSCARO\n" + str(response_osc))
