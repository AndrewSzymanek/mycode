#!/usr/bin/env python3
"""AWS Amazon Apprenticeship | Author: Andrew Szymanek"""

import requests

def main():
    r = requests.get("http://api.open-notify.org/astros.json")
    print("People in space: " +str(r.json().get('number')))
    for person in r.json()["people"]:
     print(str(person.get("name")) + " on the " + str(person.get("craft")))
        
main()
