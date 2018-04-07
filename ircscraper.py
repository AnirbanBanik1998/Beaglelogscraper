import requests
from bs4 import BeautifulSoup
import os
headers = {
	    'User-Agent': 'BeagleLogScraper 2.0'
	    }
source_code=requests.get("http://logs.nslu2-linux.org/livelogs/beagle-gsoc/", headers=headers)
text=source_code.text
soup=BeautifulSoup(text)
dictionary={
		'Jan': '01',
		'Feb': '02',
		'Mar': '03',
		'Apr': '04',
		'May': '05',
		'Jun': '06',
		'Jul': '07',
		'Aug': '08',
		'Sep': '09',
		'Oct': '10',
		'Nov': '11',
		'Dec': '12'
		}
word=""
month=""
date=""
year=""
def integer(s):
	n=0
	for i in range(0,len(s)):
		if s[i]=='0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
			n=n*10+int(s[i])
		
	return n
with open('Chat.txt','r') as r:
						
	ar=r.read().split("\n")
	n=len(ar)-1
	while ar[n]=="" and n>0:
		n=n-1
	word=ar[n]
for key, value in dictionary.items():
	if word[27:30]==key:
		month=value
date=str(word[31:33])
year=str(word[43:47])
string=year+month+date
string=string.strip()
for link in soup.findAll('a'):
	title=link.string
	k=0
	title_num=title[12:20]
	title_num=title_num.strip()
	
	if integer(title_num)-integer(string)>0:
		k=1
	if k==1:
		try:
			code=requests.get("http://logs.nslu2-linux.org/livelogs/beagle-gsoc/"+title)
			code=code.text
			arr=code.split("\n")
			print(arr)
			f=open("Chat.txt", "a")
			f.write("\n")
			for i in range(0,len(arr)):
				f.write(arr[i]+"\n")
			f.close()
		except:
			print("Failed")

