import time
import urllib.request
import urllib
import bs4
from urllib import request
from os import system
import re

def osc_parse(url_osc, url_osc_data):
    url_osc_data = url_osc_data.encode('utf-8')
    req_osc = urllib.request.Request(url=url_osc, data=url_osc_data, method='POST',
                                     headers={'User-Agent': 'Mozilla/5.0'})
    response_osc = urllib.request.urlopen(req_osc).read()
#    print("\n\nOSCARO\n" + str(response_osc))

    page_osc = bs4.BeautifulSoup(response_osc, "lxml")
    print(page_osc)
    #print(re.search('(.*?"){10}', str(page_osc), re.DOTALL).group())
    print(re.search('.+?(?="){10}', str(page_osc)))

    for item_osc in page_osc.findAll("(.*?\"){9}(.*?)\""):
#        print(item_osc)
        return(response_osc)

print(osc_parse("https://www.oscaro.com/Catalog/SearchEngine/GetPlateSearchResult","plateValue=aw512bm&genartId=null"))

#url_string_osc = 'https://www.oscaro.com/Catalog/SearchEngine/GetPlateSearchResult'
#data = "plateValue=aw512bm&genartId=null"
