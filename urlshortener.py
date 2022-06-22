# pip install pyshorteners

import pyshorteners

url = input("Enter URL :\n")
shortened_url = pyshorteners.Shortener().tinyurl.short(url)
print("URL after shortening :- ", shortened_url)
