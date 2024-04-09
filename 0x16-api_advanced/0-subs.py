#!/usr/bin/python3
"""
    Module implementing a function that returns
    number of total subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """returns total number of subscribers"""
    u_agent = "Mozilla/5.0"
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "u_agent"
        }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    dict = response.json()
    if "data" not in dict:
        return 0
    if "subscribers" not in dict.get('data'):
        return 0
    subscribers = dict['data']['subscribers']
    return subscribers
