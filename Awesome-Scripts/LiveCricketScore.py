import time
import urllib2
from bs4 import BeautifulSoup
from gi.repository import Notify
Notify.init("Cricket Update")

#Display Function
def disp(body):
	notification = Notify.Notification.new(body,)
	notification.show()

#Get all the matches name
def getname():
	src1="http://www.cricbuzz.com/cricket-match/live-scores"
	conn=urllib2.urlopen(src1).read()
	soup=BeautifulSoup(conn,"lxml")
	i=1
	lst = soup.select("div.cb-bg-white.cb-col-100.cb-col div.cb-col-67.cb-col.cb-left.cb-schdl div.cb-col.cb-col-100.cb-lv-main div.cb-mtch-lst.cb-col.cb-col-100.cb-tms-itm div.cb-col-100.cb-col.cb-schdl")
	for x in lst[::2]:	
			for y in x.select(" h3.cb-lv-scr-mtch-hdr.inline-block "):
				print str(i)+")"+y.text
			for z in x.select(" span.text-gray "):
				print z.text
			i+=1

	choice=input("Enter your choice: ")

	d1= lst[2*choice-2].select(" h3.cb-lv-scr-mtch-hdr.inline-block ")[0].text
	d2= lst[2*choice-2].select(" span.text-gray ")[0].text
	return [d1,d2]

#RefreshScore
def refresh(d1,d2):
	while(True):
		flag=0
		src1="http://www.cricbuzz.com/cricket-match/live-scores"
		conn=urllib2.urlopen(src1).read()
		soup=BeautifulSoup(conn,"lxml")
		lst = soup.select("div.cb-bg-white.cb-col-100.cb-col div.cb-col-67.cb-col.cb-left.cb-schdl div.cb-col.cb-col-100.cb-lv-main div.cb-mtch-lst.cb-col.cb-col-100.cb-tms-itm div.cb-col-100.cb-col.cb-schdl")
		for index,x in enumerate(lst[::2]):
			y=x.select(" h3.cb-lv-scr-mtch-hdr.inline-block ")[0].text
			z=x.select(" span.text-gray ")[0].text
			if(d1==y and d2==z):
				try:
					z1=lst[2*index+1].select("div.cb-lv-scrs-col.text-black")[0].text
					disp(z1)
					time.sleep(30)
				except IndexError:
					print "Match not started"
					flag=1
					break
		if(flag==1):
			break



val=getname()
d1=val[0]
d2=val[1]
refresh(d1,d2)
