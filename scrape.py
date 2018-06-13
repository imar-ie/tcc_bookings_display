#!/usr/bin/env python

""" Parse bookings table

Auth's with the webcalender, parses and returns just the bookings table
"""

import requests

import configparser

from os import environ

from lxml import html, etree

config = configparser.ConfigParser()

config.read('config.ini')

USERNAME = environ.get('user')
PASSWORD = environ.get('password')

LOGIN_URL = config.get('urls', 'BASE') + config.get('urls', 'LOGIN')
SCRAPE_URL = config.get('urls', 'BASE') + config.get('urls', 'SCRAPE')

def scrape():

    print(' * Fetching bookings...')

    # create a session
    session_requests = requests.session()

    # Create payload
    payload = {
        "login": USERNAME,
        "password": PASSWORD,
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(SCRAPE_URL, headers = dict(referer = SCRAPE_URL))

    # Parse doc tree
    tree = html.fromstring(result.content)

    # Select table
    table = tree.xpath("//table[@class='glance']")

    return etree.tostring(table[0], pretty_print=True, encoding='unicode')


if __name__ == '__main__':
    scrape()
