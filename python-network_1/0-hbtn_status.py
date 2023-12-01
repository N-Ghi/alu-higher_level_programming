#!/usr/bin/python3
"""Documented"""
import urllib.request

url = 'https://intranet.hbtn.io/status'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) '
                  'AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Chrome/116.0.5845.187 Safari/605.1.15',
}

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as response:
    content = response.read()
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode("utf-8"))
