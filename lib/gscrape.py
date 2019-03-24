"""
Helper Functions for Google Spreadhseet Parsing for RISHI-NATWEB.
"""
from urllib2 import urlopen
from json import loads

__author__ = 'asinghal17'

def getURL(key):
	"""Takes in Spreadsheet key and appends url attributes. 

	key -- Google Spreadsheet Key
	"""
	return "https://spreadsheets.google.com/feeds/list/"+str(key)+"/od6/public/basic?alt=json"

def getTitle(dic):
	"""Takes a Dictionary to return 1st Row Value from Spreadsheet. 

	dic -- Dictionary from the JSON with all values.
	"""
	return str(dic["title"]["$t"])

def getPosition(dic):
	"""Returns the Position from the Member/Chapter Spreadsheets.

	dic -- Dictionary from the JSON with all values.
	"""
	return str(dic["content"]["$t"]).split(',')[0].split(':')[1].strip()

def getEmail(dic):
	"""Returns the Email for the Members/Chapter spreadhseets. 

	dic -- Dictionary from the JSON with all values.
	"""
	return str(dic["content"]["$t"]).split(',')[1].split(':')[1].strip()

def getPhoto(dic):
	"""Returns the Link for Photo.

	dic -- Dictionary from the JSON with all values.
	"""
	return str(dic["content"]["$t"]).split(',')[2].split(' ')[2].strip()

def getMemHash(dic):
	"""Returns the Link for Photo.

	dic -- Dictionary from the JSON with all values.
	"""
	return str(dic["content"]["$t"]).split(',')[3].split(' ')[2].strip()

def getDueDate(dic):
	"""Return the Due Date for Chapter Applications.

	dic -- Dictionary from the JSON with all values.
	"""
	return str(dic["content"]["$t"]).split(',')[2].split(':')[1].strip()

def getAppLink(dic):
	"""Returns the Link for Chapter Application Form.

	dic -- Dictionary from the JSON with all values.
	"""
	return str(dic["content"]["$t"]).split(',')[3].split(' ')[2].strip()

def getContactInfo(dic):
	"""Returns the Contact info for Chapters.

	dic -- Dictionary from the JSON with all values.
	"""
	return str(dic["content"]["$t"]).split(',')[1].split(':')[1].strip()

def getSeal(dic):
	"""Returns the Chapter Seal for each Chapter.

	dic -- Dictionary from the JSON with all values.
	"""
	return str(dic["content"]["$t"]).split(',')[0].split(' ')[1].strip()

def getHashtag(dic):
	"""Returns the relavant Modal hashtags for each chapter.

	dic -- Dictionary from the JSON with all values.
	"""
	return str(dic["content"]["$t"]).split(',')[4].split(':')[1].strip()

def getChapterStatus(dic):
	"""Returns the current status of the relevant chapter.

	dic -- Dictionary from the JSON with all values.
	"""
	return str(dic["content"]["$t"]).split(',')[5].split(':')[1].strip()

def getMarquee(dic):
	"""Returns messages to display on Home. 

	dic -- Dictionary from the JSON with all values.
	"""
	return str(dic["content"]["$t"]).split(',')[0].split(':')[1].strip()

def getMarqueeLink(dic):
	"""Returns the CTA Link on Marquee. 

	dic -- Dictionary from the JSON with all values.
	"""
	return str(dic["content"]["$t"]).split(',')[1].split(' ')[2].strip()

def getEntry(key):
	"""Takes in the key to obtain values for the key [Entry] from JSON. 
	
	key -- Google Spreadsheet Key
	"""
	url=getURL(key)
	response = urlopen(url)
	html = response.read()
	html = loads(html)
	feed=html["feed"]
	return feed["entry"]

def getFeedList(key):
	"""Takes in the key to return list of content values. 

	key -- Google Spreadsheet Key
	"""
	obj=getEntry(key)
	y=(x for x in obj)
	return y


# =======================================================
# Main Functions for Feed
# =======================================================
def getMarqueeFeed(key):
	"""Returns a tuple of Dictionaries with Content and CTA for Marquee. 

	key -- Google Spreadsheet Key
	"""
	feed=getFeedList(key)
	return [{"content":getMarquee(dic),"link":getMarqueeLink(dic)} for dic in feed]

def getAppFeed(key):
	"""Returns a tuple of Dictionaries with content for Chapter and Apply Page. 

	key -- Google Spreadsheet Key
	"""
	feed=getFeedList(key)
	return ({"chapter":getTitle(dic),"hashtag":getHashtag(dic),"due_date":getDueDate(dic),"link":getAppLink(dic),
		"contact":getContactInfo(dic),"seal":getSeal(dic),"status":getChapterStatus(dic)} for dic in feed)

def getMemberFeed(key):
	"""Returns a tuple of Dictionaries with content for Member Profiles including National. 

	key -- Google Spreadsheet Key
	"""
	if key:
		feed=getFeedList(key)
		return ({"name":getTitle(dic),"email": getEmail(dic),"position":getPosition(dic),"photo": getPhoto(dic),"hashtag":getMemHash(dic)} for dic in feed)
	else:
		return ({"name":"","email":"","position":"","photo": ""}) 

