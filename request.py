import requests

"""
# grab contents from a website
#r = requests.get("https://xkcd.com/353/")
r = requests.get("https://imgs.xkcd.com/comics/python.png") #image

#print(help(r)) #dir() of a request shows objects. for further explanation we can use help()

#print(r.text) #we get the html for this case, we can parse it with an specific method.

#print(r.content) #remember content , returns byte. We can take those bytes and save
#them to an image
"""
"""
with open("comic.png","wb") as f: #we are going to opened in wb mode (write bytes)
    f.write(r.content) #write the bytes of content in f 
"""
"""
print(r.status_code) #http status code (200 -> success, 300 -> redirect, 400 -> client error (permission error), 500 -> server errors)

#easier way is:
print(r.ok) #True or False. self explanatory

print(r.headers)

#for monitoring a website

#using web browser, we find the url of just the image 

"""
"""
payload = {"page" : 2, "count": 25} #this way is easier to set them correctly. get parameters
r = requests.get("https://httpbin.org/get",params=payload) #payload is a dictionary or URL parameters
#that we want to set.
print(r.text)
#in url we can see what url we requested. we can do it with print(r.url) as well

#if we are goint to post to a certain url, we can do that if we want to post form data to a route,
# or similar
"""

"""
#for this kind of uses, we have to look to the html data, to see what values that form is expecting
payload = {"username" : "Luis", "password": "testing"} #this way is easier to set them correctly. get parameters
r = requests.post("https://httpbin.org/post",data=payload) #we change the method wrote after the last slash. 
#print(r.text)

r_dict = r.json() # we can put it in a variable, that way we can check for value`s key.
#as we were using a dictionary

#example:
print(r_dict["form"])

print(r.json()) #it createsa  python disctionary

#and the method after request. as well.

#data to be posted is now payload, which will be data likely to be in a form

#Note: We are getting Json responses back from the httpbins website,but actually Json responses are pretty common
#when workings with certain APIs. When receiving those we can change the .text method for a .json() method instead


#we can do a pull request of some data using put (its basically the same thing, in code)

#to perform logins, not all of them goes through a form authetication.

#some of them are done through a basic authentication, if we required to pass credentials using basic authentication. 
#Then, request can do that also, we can also use httpbin to test this as well

"""
"""
#for this example we copy this url which includes basic authentication

r = requests.get("https://httpbin.org/basic-auth/corey/testing",auth=("corey","testing"))

#auth parameters is a tuple of of username, password
#if any of this is incorrent we wont get a response in our 
#print(r.text) declaration

print(r) #if we only print r when sending incorrect credentials for a .get method in a basic auth
#we get a response with the status code [401] (unathorized response code)
#for correct creds, we get 200 code response
"""
#another functionality we can implement is monitor for a website with a timeput limit for accessing 
#the page, this way if the page is not responding at the moment we can capture it too
try:
    r = requests.get("https://httpbin.org/delay/6",timeout=3)
except:
    print("timeout")
#the befored url returns a delayed response, the last number is actually the delayed time
#3 seconds of time out for this specific example

#if timeout elapses, we get an exception, in this case instead of getting all the 
#printed error, we can change the declaration with try , except for printing a smaller message

#it is a good idea to place the timeout parameter for some functionality
#except for some cases in which computation in the server takes a lots of time

