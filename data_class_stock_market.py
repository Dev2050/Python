Python 3.7.0a1 (v3.7.0a1:8f51bb4, Sep 19 2017, 18:50:29) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> import urllib.request
>>> class Stock:
	def __init__(self):
		pass
	def getReadStock():
		url="https://finance.google.com/finance?q="
		stock=input("Please enter the stock market name? ")
		url=url+stock
		raw_data=urllib.request.urlopen(url).read()
		utf_data=raw_data.decode('UTF-8')
		#d1 stands for data one, and d1l data one location(position)
		d1l=re.search('meta itemprop="price"', utf_data)
		#stock data containing tag block st1=start postion one/ed1=end position one
		st1=d1l.start()
		ed1=d1l.end()+23
		stock_data_area=utf_data[st1:ed1]
		##need to find stock data location with tag name "content"
		d2l=re.search('content="',stock_data_area)
		st2=d2l.end()
		stock_value=stock_data_area[st2:]
		print("The stock market value for " +stock+ " is " +stock_value)

		
>>> Stock.getReadStock()
Please enter the stock market name? AIG
The stock market value for AIG is 61.39
>>> class Stock:
	def __init__(self):
		pass
	def getReadStock():
		url="https://finance.google.com/finance?q="
		stock=input("Please enter the stock market name?\n")
		url=url+stock
		raw_data=urllib.request.urlopen(url).read()
		utf_data=raw_data.decode('UTF-8')
		#d1 stands for data one, and d1l data one location(position)
		d1l=re.search('meta itemprop="price"', utf_data)
		#stock data containing tag block st1=start postion one/ed1=end position one
		st1=d1l.start()
		ed1=d1l.end()+23
		stock_data_area=utf_data[st1:ed1]
		##need to find stock data location with tag name "content"
		d2l=re.search('content="',stock_data_area)
		st2=d2l.end()
		stock_value=stock_data_area[st2:]
		print("The stock market value for " +stock+ " is " +stock_value)

		
>>> Stock.getReadStock()
Please enter the stock market name?
AIG
The stock market value for AIG is 61.39
>>> Stock.getReadStock()
Please enter the stock market name?
FB
The stock market value for FB is 170.8
>>> Stock.getReadStock()
Please enter the stock market name?
DANSKE BANK
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    Stock.getReadStock()
  File "<pyshell#10>", line 8, in getReadStock
    raw_data=urllib.request.urlopen(url).read()
  File "C:\Users\Fissha\AppData\Local\Programs\Python\Python37-32\lib\urllib\request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Users\Fissha\AppData\Local\Programs\Python\Python37-32\lib\urllib\request.py", line 531, in open
    response = meth(req, response)
  File "C:\Users\Fissha\AppData\Local\Programs\Python\Python37-32\lib\urllib\request.py", line 641, in http_response
    'http', request, response, code, msg, hdrs)
  File "C:\Users\Fissha\AppData\Local\Programs\Python\Python37-32\lib\urllib\request.py", line 569, in error
    return self._call_chain(*args)
  File "C:\Users\Fissha\AppData\Local\Programs\Python\Python37-32\lib\urllib\request.py", line 503, in _call_chain
    result = func(*args)
  File "C:\Users\Fissha\AppData\Local\Programs\Python\Python37-32\lib\urllib\request.py", line 649, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 400: Bad Request
>>> Stock.getReadStock()
Please enter the stock market name?
Nordea
The stock market value for Nordea is 110.4
>>> 
