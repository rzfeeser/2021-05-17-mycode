#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   API Review Friday Morning."""

API = "https://api.nasa.gov/planetary/apod?api_key="

# standard library imports

# 3rd party imports
# python3 -m pip install requests
import requests

# classes

# functions
def getkey():
    """Pull the NASA API Key"""
    with open("/home/student/.ssh/nasa_key") as keyfile:
        apikey = keyfile.read().strip()
    return apikey

def main():
    """Called at runtime"""
    r = requests.get(f"{API}{getkey()}")

    # figuring out techniques for manipulating our returned data
    #print(r.json().get("hdurl").split("/")[-1])

    imgurl = r.json().get("hdurl")
    imgdata = requests.get(imgurl).content
    with open(f"/home/student/static/{imgurl.split('/')[-1]}", 'wb') as handler:
        handler.write(imgdata)

# call main if called from CLI
if __name__ == "__main__":
    main()

