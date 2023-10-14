import requests
#Using the requests module here
#We used this module even in our college Python labs for downloading XKCD comics
tinyurl= 'http://tinyurl.com/api-create.php?url='
long_url=input("Enter a URL to shorten: ")
#Here we are using the TinyURL API ro shorten the input URL
response = requests.get(tinyurl+long_url)
short_url= response.text

print("The shortened URL: ")
print(short_url)
