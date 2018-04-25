Python 3.7.0a1 (v3.7.0a1:8f51bb4, Sep 19 2017, 18:50:29) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> import urllib.request
>>> def getStock():
	url="https://finance.google.com/finance?q="
	stock=input("Please enter the stock market name? ")
	url=url+stock
	d1=urllib.request.urlopen(url).read()
	d2=d1.decode('utf-8')
	##location data
	d3l=re.search('meta itemprop="price"', d2)
	st1=d3l.start()
	ed1=d3l.end()+23
	###obtained elements containing the values
	d3=d2[st1:ed1]
	##location data for the hidden content attribute
	d4l=re.search('content="',d3)
	st2=d4l.end()
	##the actual value
	stock_value=d3[st2:]
	print("The stock market value for " +stock+ " is " +stock_value)

	
>>> 
>>> getStock()
Please enter the stock market name? FB
The stock market value for FB is 170.8
>>> getStock()
Please enter the stock market name? Total
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    getStock()
  File "<pyshell#3>", line 9, in getStock
    st1=d3l.start()
AttributeError: 'NoneType' object has no attribute 'start'
>>> getStock
<function getStock at 0x02CC6270>
>>> getStock()
Please enter the stock market name? TACI
The stock market value for TACI is 0.210
>>> getStock()
Please enter the stock market name? IPC
The stock market value for IPC is 0.590
>>> getStock()
Please enter the stock market name? TSEC
The stock market value for TSEC is 10,38
>>> 
