#!/usr/bin/env python3

import requests
import re

def get_temperature(code):
    base_url = "http://tgftp.nws.noaa.gov/weather/current/{}.html".format(code)

    answer = requests.get(base_url).text

    for line in answer.split("\n"):
        temperature = re.match(".*[0-9]+ F \(([0-9]+) C\).*", line)

        if temperature:
            return temperature.group(1)

if __name__ == "__main__":
    print(get_temperature("LEBL"))
