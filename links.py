#!/usr/bin/env python
'''
print out the links for the png files

'''



import os
import urllib
import thread
import time

# determine files
files = [ name for name in os.listdir('.') if name.lower().endswith('.png')]

# determine url for file
link_base = 'https://raw.github.com/niccokunzmann/maglev-wiki-pictures/master/'
def url(name):
    link = link_base + name
    return urllib.quote(link, safe = '/:')

# get remote urls
url_contents = {}
def add_content(name):
    try:
        link = url(name)
        url_contents[name] = urllib.urlopen(link).read()
    except:
        url_contents[name] = None
        raise
for name in files:
    thread.start_new(add_content, (name,))

# print names
for name in sorted(files):
    link = url(name)
    print(link)
    while not name in url_contents:
        time.sleep(0.001)
    content = url_contents[name]
    if content != file(name, 'rb').read():
        print('!needs update!')
    print('')
