Python 3.7.0a1 (v3.7.0a1:8f51bb4, Sep 19 2017, 18:50:29) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import request
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import request
ModuleNotFoundError: No module named 'request'
>>> import requests
>>> from bs4 import*
>>> data=requests.get("https://www.accuweather.com/en/fi/finland-weather")
>>> data
<Response [200]>
>>> soup=BeautifulSoup(data.text,"html.parser")
>>> soup.find("div")
<div id="eu-cookie-notify-wrap">
<div id="eu-cookie-notify">
<a href="https://www.accuweather.com/en/privacy#adChoices" id="lnk-eu-cookie-learn">
                This site uses cookies. By continuing to browse the site you are agreeing to our use of cookies. Find out more here
            </a>
</div>
</div>
>>> ##soup.find('',{})
>>> soup.find('div',{'class':'info'})
<div class="info">
<div class="temp">
<span class="large-temp">59°</span>
<span class="real-feel">RealFeel® 61°</span>
</div>
<ul class="special-forecast"></ul>
</div>
>>> data2=soup.find('div',{'class':'info'})
>>> data3=soup.find('strong',{'class':'active'})
>>> data3
>>> data3=soup.find('span',{'class':'large-temp'})
>>> data3
<span class="large-temp">59°</span>
>>> data3.contents
['59°']
>>> data3.contents[0]
'59°'
>>> for i in soup.find('span'):
	print(i)

	
>>> x=soup.find('span')
>>> x
<span id="dynamic-menu-container"></span>
>>> x=soup.find_all('span')
>>> x
[<span id="dynamic-menu-container"></span>, <span>°F</span>, <span class="temp">59°</span>, <span class="icon i-33-s"></span>, <span class="temp">79°</span>, <span class="icon i-35-s"></span>, <span class="temp">66°</span>, <span class="icon i-33-s"></span>, <span></span>, <span class="arrow"></span>, <span class="arrow-border"></span>, <span class="arrow"></span>, <span class="arrow-border"></span>, <span class="ir flag-FI">Finland</span>, <span><span class="flag-FI">Finland</span></span>, <span class="flag-FI">Finland</span>, <span class="menu-arrow"><span>           </span>, °F</span>, <span>           </span>, <span></span>, <span>°F</span>, <span>°C</span>, <span>World</span>, <span>World</span>, <span>World</span>, <span>World</span>, <span>World</span>, <span>World</span>, <span>World</span>, <span>World</span>, <span>World</span>, <span>World</span>, <span>Weather</span>, <span class="menu-arrow"><span>Login</span></span>, <span>Login</span>, <span class="current-country">Finland</span>, <span class="title">Weather</span>, <span class="bottom-line"></span>, <span class="current-city">Select a City</span>, <span class="title"> </span>, <span class="divider"></span>, <span class="more-info-arrow"></span>, <span class="arrow"></span>, <span class="right-arrow"></span>, <span class="cover-line"></span>, <span>Personalized Forecasts: <span class="highlighted">Allergies</span></span>, <span class="highlighted">Allergies</span>, <span class="arrow"></span>, <span class="icon-pencil"></span>, <span class="large-temp">59°</span>, <span class="real-feel">RealFeel® 61°</span>, <span class="large-temp">79°</span>, <span class="real-feel">RealFeel® 82°</span>, <span class="large-temp">66°</span>, <span class="real-feel">RealFeel® 67°</span>, <span><strong>Home</strong></span>, <span class="bing-attrib"></span>, <span class="large-temp">59°</span>, <span class="small-temp">
<em>RealFeel®</em>
                                                            61°
                                                        </span>, <span class="large-temp">79°</span>, <span class="small-temp">
<em>RealFeel®</em>
                                                            82°
                                                        </span>, <span class="large-temp">66°</span>, <span class="small-temp">
<em>RealFeel®</em>
                                                            67°
                                                        </span>, <span>45°</span>, <span>44°</span>, <span>44°</span>, <span>45°</span>, <span>45°</span>, <span>43°</span>, <span>45°</span>, <span>48°</span>, <span>45°</span>, <span>46°</span>, <span>43°</span>, <span>43°</span>, <span>45°</span>, <span>45°</span>, <span>46°</span>, <span>39°</span>, <span>45°</span>, <span>43°</span>, <span>50°</span>, <span>44°</span>, <span class="adr">
<span class="locality">
<span class="value-title" title="New York"></span>
</span>
<abbr class="region" title="New York">
<span class="value-title" title="NY"></span>
</abbr>
<span class="postal-code">
<span class="value-title" title="10007"></span>
</span>
<abbr class="country-name" title="United States">
<span class="value-title" title="US"></span>
</abbr>
</span>, <span class="locality">
<span class="value-title" title="New York"></span>
</span>, <span class="value-title" title="New York"></span>, <span class="value-title" title="NY"></span>, <span class="postal-code">
<span class="value-title" title="10007"></span>
</span>, <span class="value-title" title="10007"></span>, <span class="value-title" title="US"></span>, <span class="geo">
<span class="latitude">
<span class="value-title" title="40.779"></span>
</span>
<span class="longitude">
<span class="value-title" title="-73.969"></span>
</span>
</span>, <span class="latitude">
<span class="value-title" title="40.779"></span>
</span>, <span class="value-title" title="40.779"></span>, <span class="longitude">
<span class="value-title" title="-73.969"></span>
</span>, <span class="value-title" title="-73.969"></span>]
>>> y=soup.find_all('span', {'class':'large-temp'})
>>> y
[<span class="large-temp">59°</span>, <span class="large-temp">79°</span>, <span class="large-temp">66°</span>, <span class="large-temp">59°</span>, <span class="large-temp">79°</span>, <span class="large-temp">66°</span>]
>>> for i in y:
	print(i)

	
<span class="large-temp">59°</span>
<span class="large-temp">79°</span>
<span class="large-temp">66°</span>
<span class="large-temp">59°</span>
<span class="large-temp">79°</span>
<span class="large-temp">66°</span>
>>> for i in y:
	print(i.contents)

	
['59°']
['79°']
['66°']
['59°']
['79°']
['66°']
>>> 
