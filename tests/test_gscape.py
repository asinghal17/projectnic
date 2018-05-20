"""
UnitTests for Google Sheet Scraping.
"""
from __future__ import absolute_import
import sys,os,unittest
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"../"))
from lib.gscrape import getURL,getTitle,getPosition,getEmail,getPhoto,getHashtag,getDueDate,getAppLink,getSeal,getContactInfo,getAppLink,getChapterStatus

__author__ = 'asinghal17'

class TestURL(unittest.TestCase):
	chap = "1BPnZpUqYNw-W9NI8aCIfI-OqL4DNCZf2r1YfEb5gOB0"
	marq = "15odV2nwZvLJLvBi5g51Ma8UsgN2WSCKiDt0JeyhEthw"
	def test_url(self):
		exp1="https://spreadsheets.google.com/feeds/list/1BPnZpUqYNw-W9NI8aCIfI-OqL4DNCZf2r1YfEb5gOB0/od6/public/basic?alt=json"
		exp2="https://spreadsheets.google.com/feeds/list/15odV2nwZvLJLvBi5g51Ma8UsgN2WSCKiDt0JeyhEthw/od6/public/basic?alt=json"
		self.assertEqual(getURL(self.chap),exp1)
		self.assertEqual(getURL(self.marq),exp2)

class TestDataFunctions(unittest.TestCase):
	json2={
	  "category": [
	    {
	      "term": "http://schemas.google.com/spreadsheets/2006#list",
	      "scheme": "http://schemas.google.com/spreadsheets/2006"
	    }
	  ],
	  "updated": {
	    "$t": "2017-05-21T03:54:45.255Z"
	  },
	  "title": {
	    "$t": "University of California, Los Angeles",
	    "type": "text"
	  },
	  "content": {
	    "$t": "seal: http://s3.projectrishi.org/img/chapters/seal/ucla-seal.png, contact: ucla@projectrishi.org, duedate: TBA, applicationlink: TBA, hashtag: #ucla, status: Active",
	    "type": "text"
	  },
	  "link": [
	    {
	      "href": "https://spreadsheets.google.com/feeds/list/1BPnZpUqYNw-W9NI8aCIfI-OqL4DNCZf2r1YfEb5gOB0/od6/public/basic/cokwr",
	      "type": "application/atom+xml",
	      "rel": "self"
	    }
	  ],
	  "id": {
	    "$t": "https://spreadsheets.google.com/feeds/list/1BPnZpUqYNw-W9NI8aCIfI-OqL4DNCZf2r1YfEb5gOB0/od6/public/basic/cokwr"
	  }
	}
	json1={
	  "category": [
	    {
	      "term": "http://schemas.google.com/spreadsheets/2006#list",
	      "scheme": "http://schemas.google.com/spreadsheets/2006"
	    }
	  ],
	  "updated": {
	    "$t": "2017-05-12T00:04:25.410Z"
	  },
	  "title": {
	    "$t": "Jane Doe",
	    "type": "text"
	  },
	  "content": {
	    "$t": "position: President, email: email@email.com, photolink: http://s3.projectrishi.org/img/chapters/ucb/photo.png",
	    "type": "text"
	  },
	  "link": [
	    {
	      "href": "https://spreadsheets.google.com/feeds/list/17KCKd-x8WL5NJHL1dnFex3zHAfSGCqrqCsC0q6Fqljw/od6/public/basic/cokwr",
	      "type": "application/atom+xml",
	      "rel": "self"
	    }
	  ],
	  "id": {
	    "$t": "https://spreadsheets.google.com/feeds/list/17KCKd-x8WL5NJHL1dnFex3zHAfSGCqrqCsC0q6Fqljw/od6/public/basic/cokwr"
	  }
	}
	def test_get_title(self):
		exp1 = "Jane Doe"
		exp2 = "University of California, Los Angeles"
		self.assertEqual(getTitle(self.json1),exp1)
		self.assertEqual(getTitle(self.json2),exp2)

	def test_get_photo(self):
		exp1= "http://s3.projectrishi.org/img/chapters/ucb/photo.png"
		self.assertEqual(getPhoto(self.json1),exp1)

	def test_get_position(self):
		exp1= "President"
		self.assertEqual(getPosition(self.json1),exp1)

	def test_get_email(self):
		exp1= "email@email.com"
		self.assertEqual(getEmail(self.json1),exp1)

	def test_get_hashtag(self):
		exp1="#ucla"
		self.assertEqual(getHashtag(self.json2),exp1)

	def test_get_duedate(self):
		exp1="TBA"
		self.assertEqual(getDueDate(self.json2),exp1)

	def test_get_applink(self):
		exp1="TBA"
		self.assertEqual(getAppLink(self.json2),exp1)

	def test_get_seal(self):
		exp1="http://s3.projectrishi.org/img/chapters/seal/ucla-seal.png"
		self.assertEqual(getSeal(self.json2),exp1)

	def test_get_chapterstatus(self):
		exp1="Active"
		self.assertEqual(getChapterStatus(self.json2),exp1)

	def test_get_contactinfo(self):
		exp1="ucla@projectrishi.org"
		self.assertEqual(getContactInfo(self.json2),exp1)

if __name__ == "__main__":
	unittest.main()