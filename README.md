# Examples for using the RGW Admin API

This script is an example to illustrate how you can extract per-user usage statistics from Ceph's Rados Gateway, which can be useful for management, user monitoring, and billing.

## Installation

    pip install -r requirements.txt

## Usage

Drop a `keys.json` file in the repo that looks like this:

    {
      "uid": "alice",
      "access_key": "RTZREJDAB4VRCCZF2SJN",
      "secret_key": "pzLq6MjprdyI21UjXvBm6N5MgmhWeswaPR7PmwPX"
    }

The above user will need admin caps on the rados gateway, which you can assign with the following commands:

    radosgw-admin caps add --uid="alice" --caps="users=*"
    radosgw-admin caps add --uid="alice" --caps="buckets=*"
    radosgw-admin caps add --uid="alice" --caps="metadata=*"
    radosgw-admin caps add --uid="alice" --caps="usage=*"

You should then be able to pass a hostname and port as an argument:

    $ ./usage_example.py
    Usage: ./usage_example.py RGW_HOSTNAME:PORT

For example:

    $ ./usage_example.py 192.168.3.99
    danny           {'bytes_sent': 3080, 'bytes_received': 11534336000, 'ops': 749, 'successful_ops': 744}
    alice           {'bytes_sent': 1038, 'bytes_received': 1048576000, 'ops': 73, 'successful_ops': 72}
    bob             No Usage
