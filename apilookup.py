#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com"""

# python3 -m pip install requests
import requests

def main():

    # send an HTTP GET to this location, and record the response ans majortom
    # GET ---------------------------> http://api.open-notify.org/astros.json
    # <-------------------- 200 + JSON
    majortom = requests.get("http://api.open-notify.org/astros.json")

    # display what is inside of our response object
    print(dir(majortom))

    # display what response code was returned
    print(majortom.status_code)

    # display what URL was looked up
    print(majortom.url)

    # display the JSON attached to the 200 response
    spacejson = majortom.json() # converts to pythonic data
    print(spacejson)

    #
    print()
    print()

    print(spacejson.get("people"))
    astrolist = spacejson.get("people")

    for astro in astrolist:
        print(astro.get("name"))


if __name__ == "__main__":
    main()
