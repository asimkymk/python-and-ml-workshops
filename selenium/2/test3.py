import requests
import os
import urllib
opener = urllib.request.FancyURLopener({})
opener.version = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Safari/537.36'
url = 'http://www.watchill.org/storage/series/February2019/0WRbPiBOzJPDJFQgPbJt.png'  
opener.retrieve(url, 'test.jpg') 

#urlretrieve('http://www.watchill.org/storage/series/February2019/0WRbPiBOzJPDJFQgPbJt.png', "test.png")