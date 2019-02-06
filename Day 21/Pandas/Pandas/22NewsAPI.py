#https://newsapi.org/
#API : 9fe4be099c6c417a8c00b56ee67f9db5
import requests
import json
a=requests.get("https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=9fe4be099c6c417a8c00b56ee67f9db5") 
b=json.loads(a.text)
for i in range(10):
	my_data=b['articles'][i]['title']
	print "Title:",my_data

