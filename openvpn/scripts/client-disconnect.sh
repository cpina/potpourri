#!/bin/bash

# logTraffic.sh: Generate a log entry with IT mandated fields
# 12/23/11 Tom Noonan II

# Modified by Carles Pina <git@pina.cat>

## Mandatory variables
sessionStart="UNSET"
clientHostAddress="UNSET"
clientUID="UNSET"
sessionDuration="UNSET"
txVolume="UNSET"
rxVolume="UNSET"
commonName="UNSET"

env >> /tmp/test.txt

## Parse variables

if [ ! -z "$time_ascii" ]; then
        sessionStart="$time_ascii"
fi

if [ ! -z "$trusted_ip" ]; then
        clientHostAddress="$trusted_ip"
fi

if [ ! -z "$username" ]; then
        clientUID="$username"
fi

if [ ! -z "$time_duration" ]; then
        sessionDuration="$time_duration"
fi

if [ ! -z "$bytes_sent" ]; then
        txVolume="$bytes_sent"
fi

if [ ! -z "$bytes_received" ]; then
        rxVolume="$bytes_received"
fi

if [ ! -z "$common_name" ]; then
        commonName="$common_name"
fi

logger -t openvpn "Session $commonName TX: $txVolume bytes RX: $rxVolume bytes Duration: $sessionDuration seconds HostIP: $clientHostAddress"

exit 0
