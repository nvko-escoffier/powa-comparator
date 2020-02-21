
import urllib.request
#import re
import urllib
import bs4
from urllib import request


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


# User entry
plaque_tmp = input("Plaque: ")

# Remove spaces then '-'
plaque_tmp = plaque_tmp.replace(' ', '')
plaque = plaque_tmp.replace('-','')

print(plaque)

# Test longueur de la plaque 3min(1A1) 10max(9999ZZZ999)
if len(plaque) <= 3:
    print("La plaque est trop courte.")
if len(plaque) >= 11:
    print("La plaque est trop longue.")

# YAKAROULER
print(yak_parse("https://www.yakarouler.com/car_search/immat?immat=" + plaque + "&name=undefined&redirect=true"))

# PIECESAUTO.COM

# OSCARO.COM
url_string_osc = 'https://www.oscaro.com/Catalog/SearchEngine/GetPlateSearchResult'
data = "plateValue=" + plaque + "&genartId=null"
data = data.encode('utf-8')
req_osc = urllib.request.Request(url=url_string_osc, data=data, method='POST', headers={'User-Agent': 'Mozilla/5.0'})
response_osc = urllib.request.urlopen(req_osc).read()
print("\n\nOSCARO\n" + str(response_osc))
