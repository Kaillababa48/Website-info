print("\003[92m")
import os
import urllib2
import sys
url = raw_input("enter website link : ")
url.rstrip ( ) 
header = urllib2.urlopen (url) .info ( ) 
print(str (header) 
