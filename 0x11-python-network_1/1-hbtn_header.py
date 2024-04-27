#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url1 = sys.argv[1]

    request = urllib.request.Request(url1)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
