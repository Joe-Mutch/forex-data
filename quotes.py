import urllib2
import calendar
import datetime
import zipfile
from StringIO import StringIO

root = 'http://www.forexite.com/free_forex_quotes/'
#RUN THIS WITH A CORRECT RANGE!!!
years = range(2015, 2016)
months = range(1, 13)
quotesDir = 'quotes/'

def DownloadFile(url):
	file = urllib2.urlopen( url )
	return file

def SaveFile(file, name):
	output = open(quotesDir + name, "wb")
	output.write(file.read())
	output.close()
	
def IsWeekDay(day, month, year):
	try:
		dateObj = datetime.datetime(year, month, day)
		return dateObj.weekday() < 5
	except:
		print 'Invalid date'
		return False
	
def Unzip(name):
	try:
		with zipfile.ZipFile(quotesDir + name, "r") as z:
			z.extractall(quotesDir)
	except:
		print 'Unable to unzip file: ' + name
			
for year in years:
	for month in months:
		for day in range(1, calendar.monthrange(year,month)[1]+1):
			if ( IsWeekDay(day, month, year) ):
				print day, month, year
				file = DownloadFile("%s/%d/%02d/%02d%02d%02d.zip"%(root,year,month,day,month,year-2000))
				SaveFile(file, "%02d%02d%02d.zip" % (day, month, year-2000))
				Unzip("%02d%02d%02d.zip" % (day, month, year-2000))
				
