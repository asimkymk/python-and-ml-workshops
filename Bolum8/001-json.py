# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 00:03:29 2019

@author: Asım
"""

#json dosyası ile çalışma

import json as js

data = '{"firstName":"Asım","lastName":"Kaymak"}'

y = js.loads(data)

print(type(y))
print(y["firstName"])
print(y["lastName"])

customer = {
        "firstName":"Engin",
        "email":"kaymakasm@gmail.com"
        }

customerJson = js.dumps(customer)
print(customerJson)