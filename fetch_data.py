import urllib2
from urllib2 import HTTPError, URLError
import re

"""
Fetch data from a source URL passed at instantiation and return the raw
  result.
"""

class FetchData(object):
  
  def __init__(self, url):
    if self.__check_url(url):
      self.url = url
    else:
      raise Exception('Invalid or missing URL')
    

  def __check_url(self, url):
    if re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url):
      return True
    return False


  def fetch_data(self):
    req = urllib2.Request(self.url)
    try:
      response = urllib2.urlopen(req)
    except HTTPError as e:
      raise Exception('Error opening URL: ' + e.code + '\n' + e.read())
    except URLError as e:
      raise Exception('Error reaching server: ' + e.reason)
    except Exception:
      import traceback
      raise Exception('Generic exception fetching data: ' + traceback.format_exc())
      
    html = response.read()
    
    #with open('file.foo', 'w') as f:
    #  f.write(html)
    #print "FetchData::html: " + html + "\n\n\n"
    
    return html
  
  
