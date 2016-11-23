#!/usr/bin/python3
import sys
sys.path.append('./request')
import requests
import webbrowser
import argparse
import hashlib
import re

monitor_file = 'monitor.txt'

def getUrlHash(url):
    r = requests.get(url)
    return hashlib.md5(r.text.encode('utf-8')).hexdigest()

def addUrl(url, hash=None):
    if hash is None:
        r = requests.get(url)
        hash = hashlib.md5(r.text.encode('utf-8')).hexdigest()
    with open(monitor_file, 'a+') as f:
        f.seek(0, 0)
        text = f.read()
        if re.search(url+r'\s', text) is None:
            f.seek(0, 2)
            f.write('{}\t{}\n'.format(url, hash))
def removeUrl(url):
    with open(monitor_file, 'r+') as f:
        lines = f.readlines()
    with open(monitor_file, 'w+') as f:
        for line in lines:
            if re.match(url, line) is None:
                f.write(line)
            
def showActiveUrls():
    try:
        with open(monitor_file, 'r') as f:
            for line in f:
                url = re.split(r'\s', line)[0]
                print(url)
    except IOError:
        exit('Couldn\'t open the list')

def check():
    with open(monitor_file, 'r') as f:
        lines = f.readlines()
    if len(lines) == 0:
        exit('There are no urls, or the list doesn\'t exist')
    for line in lines:
        parts = re.split(r'\s', line)
        url, oldHash = parts[0], parts[1]
        newHash = getUrlHash(url)
        if oldHash != newHash:
            print(url +' has been changed recently')
            removeUrl(url)
            addUrl(url, newHash)
            webbrowser.open_new(url)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a','--add', metavar='URL', dest='add_url', help='Add url to the list')
    parser.add_argument('-r','--remove', metavar='URL',dest='remove_url', help='Remove url from the list')
    parser.add_argument('--check', action='store_true', help='Check websites from the list')
    parser.add_argument('--list', action='store_true', help='List all urls in the list')

    args = parser.parse_args()

    checkUrl = re.compile(r'http://.*')

    if args.add_url:
        url = args.add_url
        if checkUrl.match(url) is None:
            exit('Error: invalid url (should begin with http://www)')
        addUrl(url)
    if args.remove_url:
        removeUrl(args.remove_url)
    if args.list:
        showActiveUrls()
    if args.check:
        check()


if __name__ == '__main__':
    main()
