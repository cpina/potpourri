#!/usr/bin/python

"""
From a log file with the OpenVPN connection lines like:

Apr 14 23:18:31 localhost openvpn: Session $Client TX: 592794812 bytes RX: 42195316 bytes Duration: 11679 seconds HostIP: $IP

shows nicer lines like:

Apr 14 23:18:31 $Client TX: 565.333187 MB RX: 40.240589 MB 194 min. $IP
"""

import re

f = open("/var/log/openvpn-traffic.log")

def seconds_to_minutes(seconds):
    return seconds/60

def format_bytes(b):
    return "%f MB" % (float(b)/1024/1024)

for line in f.readlines():
    line = line.rstrip()
    m = re.match("(.*) localhost.*Session ([^ ]+) TX: ([0-9]+) bytes RX: ([0-9]+) bytes Duration: ([0-9]+) seconds HostIP: ([0-9\.]+).*",line)

    if m:
        date=m.group(1)
        user=m.group(2)
        tx=int(m.group(3))
        rx=int(m.group(4))
        seconds=int(m.group(5))
        ip=m.group(6)

        print date,user,"TX:",format_bytes(tx),"RX:",format_bytes(rx),seconds_to_minutes(seconds),"min.",ip
