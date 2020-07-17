import os
from os import system
#INITIATE removed, curl needs to be switched to use urllib2

#Dependencies: Python, fire, pyAesCrypt
import fire
def aescrypt(filename, password, bufferSize):
  import pyAesCrypt
  pyAesCrypt.encryptFile(filename, filename, password, bufferSize)
def aesdecrypt(filename, password):
    import pyAesCrypt
    pyAesCrypt.decryptFile(filename, filename, password, bufferSize)
#Dependencies: Python, fire
import fire
def sleep(seconds):
  import time
  time.sleep(seconds)
#Dependencies: Python, fire, use urllib2 for better cross-platform
import fire
def curl(url):
  os.system('cmd /k "curl " + url')
#Dependencies: Python, fire, gzip, zlib, shutil
import fire
def gzip(filename):
  import gzip
  import zlib
  import shutil
  with open(filename, 'rb') as f_in:
      with gzip.open(filename + ".gz", 'wb') as f_out:
          shutil.copyfileobj(f_in, f_out)
def ungzip(filename):
  import gzip
  with gzip.open(filename, 'rb') as f:
    file_content = f.read()
    with open(filename, "a") as myfile:
      myfile.write(file_content)
#########################################################
#Dependencies: Python, fire, PIL
import fire
def show(image):                #ADDED AS IND CODE SNIPPET
  from PIL import Image
  myImage = Image.open(image);
  myImage.show();
#############################################################

  #Dependencies: Python, fire, easygui
  import fire
  def msgbox(title, text):
    import easygui
    easygui.msgbox(text, title=title)
################################################
#Dependencies: Python, fire, hashlib
import fire
#DEPENDENCIES: hashlib
def sha256hash(content):
  import hashlib
  h = hashlib.sha256() # Construct a hash object using our selected hashing algorithm
  h.update(content.encode('utf-8')) # Update the hash using a bytes object
  print('HEX SHA256 String:')
  print(h.hexdigest()) # Print the hash value as a hex string
  print('BYTES SHA256 String:')
  print(h.digest())


import requests
def netdownload(url, saveas):
  link = url
  r = requests.get(link)
  with open(saveas, 'wb') as f:
    f.write(r.content)
    #this works

def geturlsrc(URLName):
    import urllib2
    response = urllib2.urlopen(URLName)
    page_source = response.read()
print('Loaded all defs in lotusCMD.py copyright c 2020')
print('Read SYNTAX.txt for more info')

while True:
    command = input("-lotuscli -original:")
    os.system(command)
