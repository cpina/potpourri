#!/usr/bin/python3

import datetime
import filecmp
import glob
import os
import requests

def main(path):
    filename=save_file(path)
    deduplicate(path)


def deduplicate(path):
    # Gets all the files from path, sorts alphabetically and
    # deletes the last one if it's the same as the pre-last one
    files=glob.glob(path + "/*")

    if len(files) <= 1:
        # There aren't duplicates
        return

    files.sort()

    last=files[-1]
    prelast=files[-2]

    if filecmp.cmp(last,prelast):
        os.remove(last)

def save_file(path):
    now=datetime.datetime.now()

    filename=now.strftime("IMG_%Y%m%d_%H%M%S.jpg")

    filepath=path + "/" + filename

    r=requests.get("https://legacy.bas.ac.uk/webcams/rrs_james_clark_ross/webcam.jpg")
    with open(filepath, 'wb') as fd:
        for chunk in r.iter_content(1024*1024):
            fd.write(chunk)

    return filepath

if __name__ == "__main__":
    main("/home/carles/jcr-webcam")

