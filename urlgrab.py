#!/usr/bin/env python

import urllib.request as url

web_data = url.urlopen('https://docs.python.org/2/library/urllib.html')

web_content = url.urlretrieve('https://docs.python.org/2/library/urllib.html', 'urllib.txt')
