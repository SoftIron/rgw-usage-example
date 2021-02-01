#!/usr/bin/python3
#
# Copyright 2021 SoftIron Ltd.
# Example script to extract per-user usage statistics from RGW

import json
import os
import radosgw
import sys

def _load_keys(filename):

    try:
        with open(filename) as json_file:
            data = json.load(json_file)
            secret_key = data['secret_key']
            access_key = data['access_key']
            return (secret_key, access_key)
    except:
        print("Unable to read keys from file: " + filename)
        exit(-1)



if __name__ == "__main__":

    # Check if keys.json file exists in current working directory
    if os.path.isfile('keys.json'):
        secret_key, access_key = _load_keys('keys.json')
    else:
        print("Keys file not found")
        exit(-1)

    # Check that we've received a single argument
    if len(sys.argv) != 2:
        print("Usage: {} RGW_HOSTNAME:PORT".format(sys.argv[0]))
        exit(-1)

    # Split address
    address = sys.argv[1].split(':')

    # Use default port of 7480 if no port specified
    if len(address) == 1:
        address.append(7480)

    # Open connection to RGW
    rgw = radosgw.connection.RadosGWAdminConnection(host=address[0],
                                                         port=address[1],
                                                         access_key=access_key,
                                                         secret_key=secret_key,
                                                         is_secure=False)

    # Fetch list of UIDs
    users = rgw.get_uids()

    # Print usage for each user
    for uid in users:
        usage = rgw.get_usage(uid=uid)

        try:
            totals = usage["summary"][0]["total"]
        except:
            totals = "No Usage"

        print("{}\t\t{}".format(uid,totals))

