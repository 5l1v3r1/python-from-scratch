#!/usr/bin/env python

import urllib.request as url2
import xml.etree.ElementTree as et

def addnumbers(A):
    result = 0
    for x in A:
        result = result+x
    return result

web_data = url2.urlopen('http://www.w3schools.com/xml/cd_catalog.xml')
str_data = web_data.read()

xml_data = et.fromstring(str_data)

cd_list = xml_data.findall('CD')
cd_prices = []

for x in cd_list:
    print(x.find('TITLE').text)

# for x in cd_list:
#     cd_prices.append(x.find('PRICE').text)

for x in cd_list:
    cd_prices.append(float(x.find('PRICE').text))

# print(cd_prices)

print(addnumbers(cd_prices))