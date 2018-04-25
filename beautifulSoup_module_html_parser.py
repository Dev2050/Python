Python 3.7.0a1 (v3.7.0a1:8f51bb4, Sep 19 2017, 18:50:29) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from bs4 import BeautifulSoup
>>> html_doc="""
<html><head><title>Tasks are things to be accomplished in an organized and predetermined way.</title></head>
<body>
<p class="title"><b>If you finish taks or not is upto you.</b></p>
<p class="story">One day there was a man. He chose to be faithful to God. In the end, his time on earth was up. Now thanks to The Lord Jesus Christ and to God in Jesus name he is enjoying eternity in heaven. What a lucky man he is.
<a href="https://en.wikipedia.org/wiki/Ethiopia" class="sister" id="link1">Ethiopia</a>,
<a href="https://en.wikipedia.org/wiki/USA" class="sister" id="link2">USA</a> and 
<a href="https://en.wikipedia.org/wiki/Finland" class="sister" id="link3">Finland</a>,
<a href="https://en.wikipedia.org/wiki/Israel" class="sister" id="link4">Israel</a>;

<p class="story">...</p>
"""
>>> from bs4 import BeautifulSoup
>>> soup=BeautifulSoup("html_doc", "html.parser")
>>> soup.find_all("a")
[]
>>> soup=BeautifulSoup(html_doc,"html.parser")
>>> soup.find_all("a")
[<a class="sister" href="https://en.wikipedia.org/wiki/Ethiopia" id="link1">Ethiopia</a>, <a class="sister" href="https://en.wikipedia.org/wiki/USA" id="link2">USA</a>, <a class="sister" href="https://en.wikipedia.org/wiki/Finland" id="link3">Finland</a>, <a class="sister" href="https://en.wikipedia.org/wiki/Israel" id="link4">Israel</a>]
>>> soup.prettify("b")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    soup.prettify("b")
  File "C:\Users\Fissha\AppData\Local\Programs\Python\Python37-32\lib\site-packages\beautifulsoup4-4.6.0-py3.7.egg\bs4\element.py", line 1216, in prettify
    return self.encode(encoding, True, formatter=formatter)
  File "C:\Users\Fissha\AppData\Local\Programs\Python\Python37-32\lib\site-packages\beautifulsoup4-4.6.0-py3.7.egg\bs4\element.py", line 1109, in encode
    return u.encode(encoding, errors)
LookupError: unknown encoding: b
>>> soup

<html><head><title>Tasks are things to be accomplished in an organized and predetermined way.</title></head>
<body>
<p class="title"><b>If you finish taks or not is upto you.</b></p>
<p class="story">One day there was a man. He chose to be faithful to God. In the end, his time on earth was up. Now thanks to The Lord Jesus Christ and to God in Jesus name he is enjoying eternity in heaven. What a lucky man he is.
<a class="sister" href="https://en.wikipedia.org/wiki/Ethiopia" id="link1">Ethiopia</a>,
<a class="sister" href="https://en.wikipedia.org/wiki/USA" id="link2">USA</a> and 
<a class="sister" href="https://en.wikipedia.org/wiki/Finland" id="link3">Finland</a>,
<a class="sister" href="https://en.wikipedia.org/wiki/Israel" id="link4">Israel</a>;

<p class="story">...</p>
</p></body></html>
>>> head_tag=soup.head
>>> head_tag
<head><title>Tasks are things to be accomplished in an organized and predetermined way.</title></head>
>>> head_tag.content
>>> head_tag.contents
[<title>Tasks are things to be accomplished in an organized and predetermined way.</title>]
>>> head_tag.contents.title
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    head_tag.contents.title
AttributeError: 'list' object has no attribute 'title'
>>> body_tag=soup.body
>>> bod_tag
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    bod_tag
NameError: name 'bod_tag' is not defined
>>> body_tag
<body>
<p class="title"><b>If you finish taks or not is upto you.</b></p>
<p class="story">One day there was a man. He chose to be faithful to God. In the end, his time on earth was up. Now thanks to The Lord Jesus Christ and to God in Jesus name he is enjoying eternity in heaven. What a lucky man he is.
<a class="sister" href="https://en.wikipedia.org/wiki/Ethiopia" id="link1">Ethiopia</a>,
<a class="sister" href="https://en.wikipedia.org/wiki/USA" id="link2">USA</a> and 
<a class="sister" href="https://en.wikipedia.org/wiki/Finland" id="link3">Finland</a>,
<a class="sister" href="https://en.wikipedia.org/wiki/Israel" id="link4">Israel</a>;

<p class="story">...</p>
</p></body>
>>> for i in body_tag:
	print(i)

	


<p class="title"><b>If you finish taks or not is upto you.</b></p>


<p class="story">One day there was a man. He chose to be faithful to God. In the end, his time on earth was up. Now thanks to The Lord Jesus Christ and to God in Jesus name he is enjoying eternity in heaven. What a lucky man he is.
<a class="sister" href="https://en.wikipedia.org/wiki/Ethiopia" id="link1">Ethiopia</a>,
<a class="sister" href="https://en.wikipedia.org/wiki/USA" id="link2">USA</a> and 
<a class="sister" href="https://en.wikipedia.org/wiki/Finland" id="link3">Finland</a>,
<a class="sister" href="https://en.wikipedia.org/wiki/Israel" id="link4">Israel</a>;

<p class="story">...</p>
</p>
>>> for i in body_tag.children:
	print(i)

	


<p class="title"><b>If you finish taks or not is upto you.</b></p>


<p class="story">One day there was a man. He chose to be faithful to God. In the end, his time on earth was up. Now thanks to The Lord Jesus Christ and to God in Jesus name he is enjoying eternity in heaven. What a lucky man he is.
<a class="sister" href="https://en.wikipedia.org/wiki/Ethiopia" id="link1">Ethiopia</a>,
<a class="sister" href="https://en.wikipedia.org/wiki/USA" id="link2">USA</a> and 
<a class="sister" href="https://en.wikipedia.org/wiki/Finland" id="link3">Finland</a>,
<a class="sister" href="https://en.wikipedia.org/wiki/Israel" id="link4">Israel</a>;

<p class="story">...</p>
</p>
>>> for i in body_tag.decendants:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    for i in body_tag.decendants:
TypeError: 'NoneType' object is not iterable
>>> for i in body_tag.descendants:
	print(i)

	


<p class="title"><b>If you finish taks or not is upto you.</b></p>
<b>If you finish taks or not is upto you.</b>
If you finish taks or not is upto you.


<p class="story">One day there was a man. He chose to be faithful to God. In the end, his time on earth was up. Now thanks to The Lord Jesus Christ and to God in Jesus name he is enjoying eternity in heaven. What a lucky man he is.
<a class="sister" href="https://en.wikipedia.org/wiki/Ethiopia" id="link1">Ethiopia</a>,
<a class="sister" href="https://en.wikipedia.org/wiki/USA" id="link2">USA</a> and 
<a class="sister" href="https://en.wikipedia.org/wiki/Finland" id="link3">Finland</a>,
<a class="sister" href="https://en.wikipedia.org/wiki/Israel" id="link4">Israel</a>;

<p class="story">...</p>
</p>
One day there was a man. He chose to be faithful to God. In the end, his time on earth was up. Now thanks to The Lord Jesus Christ and to God in Jesus name he is enjoying eternity in heaven. What a lucky man he is.

<a class="sister" href="https://en.wikipedia.org/wiki/Ethiopia" id="link1">Ethiopia</a>
Ethiopia
,

<a class="sister" href="https://en.wikipedia.org/wiki/USA" id="link2">USA</a>
USA
 and 

<a class="sister" href="https://en.wikipedia.org/wiki/Finland" id="link3">Finland</a>
Finland
,

<a class="sister" href="https://en.wikipedia.org/wiki/Israel" id="link4">Israel</a>
Israel
;


<p class="story">...</p>
...


>>> head_tag.title
<title>Tasks are things to be accomplished in an organized and predetermined way.</title>
>>> head_tag.title.string
'Tasks are things to be accomplished in an organized and predetermined way.'
>>> head_tag.title.parent
<head><title>Tasks are things to be accomplished in an organized and predetermined way.</title></head>
>>> >> head_tag.parent
SyntaxError: invalid syntax
>>> >>head_tag.parent
SyntaxError: invalid syntax
>>> head_tag.parent
<html><head><title>Tasks are things to be accomplished in an organized and predetermined way.</title></head>
<body>
<p class="title"><b>If you finish taks or not is upto you.</b></p>
<p class="story">One day there was a man. He chose to be faithful to God. In the end, his time on earth was up. Now thanks to The Lord Jesus Christ and to God in Jesus name he is enjoying eternity in heaven. What a lucky man he is.
<a class="sister" href="https://en.wikipedia.org/wiki/Ethiopia" id="link1">Ethiopia</a>,
<a class="sister" href="https://en.wikipedia.org/wiki/USA" id="link2">USA</a> and 
<a class="sister" href="https://en.wikipedia.org/wiki/Finland" id="link3">Finland</a>,
<a class="sister" href="https://en.wikipedia.org/wiki/Israel" id="link4">Israel</a>;

<p class="story">...</p>
</p></body></html>
>>> head_tag.string.parent
<title>Tasks are things to be accomplished in an organized and predetermined way.</title>
>>> soup.find_all('p')
[<p class="title"><b>If you finish taks or not is upto you.</b></p>, <p class="story">One day there was a man. He chose to be faithful to God. In the end, his time on earth was up. Now thanks to The Lord Jesus Christ and to God in Jesus name he is enjoying eternity in heaven. What a lucky man he is.
<a class="sister" href="https://en.wikipedia.org/wiki/Ethiopia" id="link1">Ethiopia</a>,
<a class="sister" href="https://en.wikipedia.org/wiki/USA" id="link2">USA</a> and 
<a class="sister" href="https://en.wikipedia.org/wiki/Finland" id="link3">Finland</a>,
<a class="sister" href="https://en.wikipedia.org/wiki/Israel" id="link4">Israel</a>;

<p class="story">...</p>
</p>, <p class="story">...</p>]
>>> soup.find_all('a')
[<a class="sister" href="https://en.wikipedia.org/wiki/Ethiopia" id="link1">Ethiopia</a>, <a class="sister" href="https://en.wikipedia.org/wiki/USA" id="link2">USA</a>, <a class="sister" href="https://en.wikipedia.org/wiki/Finland" id="link3">Finland</a>, <a class="sister" href="https://en.wikipedia.org/wiki/Israel" id="link4">Israel</a>]
>>> 
>>> soup.find_all(id="link2")
[<a class="sister" href="https://en.wikipedia.org/wiki/USA" id="link2">USA</a>]
>>> soup.find_all("a",id="link2")
[<a class="sister" href="https://en.wikipedia.org/wiki/USA" id="link2">USA</a>]
>>> import re
>>> for tag in soup.find_all(re.compile("^b")):
	print(tag.name)

	
body
b
>>> for tag in soup.find_all(re.compile("t"):
			 
SyntaxError: invalid syntax
>>> for tag in soup.find_all(re.compile("t"):
			 
SyntaxError: invalid syntax
>>> for tag in soup.find_all(re.compile("t")):
	print(i)

	




>>> for tag in soup.find_all(re.compile("t")):
	print(tag.name)

	
html
title
>>> soup.find_all(href=re.compile("Ethiopia"))
[<a class="sister" href="https://en.wikipedia.org/wiki/Ethiopia" id="link1">Ethiopia</a>]
>>> soup.find_all(href=re.compile("Ethiopia"),id="link1")
[<a class="sister" href="https://en.wikipedia.org/wiki/Ethiopia" id="link1">Ethiopia</a>]
>>> soup.find_all(href=re.complie("Israel"), id="link4")
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    soup.find_all(href=re.complie("Israel"), id="link4")
AttributeError: module 're' has no attribute 'complie'
>>> soup.find_all(href=re.compile("Israel"), id="link4")
[<a class="sister" href="https://en.wikipedia.org/wiki/Israel" id="link4">Israel</a>]
>>> 
