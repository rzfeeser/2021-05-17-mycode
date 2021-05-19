#!/usr/bin/python3


farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


for farm in farms:
    print("On the farm: " + farm.get("name"))
    print("You will find... ")
    print(farm.get("agriculture"), end="\n\n")
