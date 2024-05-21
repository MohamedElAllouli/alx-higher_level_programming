#!/usr/bin/python3

"""
send a GET request to a the url provided
as an Argument to the script and print the
X-Request-Id value of the header
"""


from requests import get
from sys import argv


def get_alx_intranet(url):
    if url:
        try:
            return get(url).headers.get('X-Request-Id')
        except Exception as e:
            return e


if __name__ == "__main__":
    print(get_alx_intranet(argv[1]))
