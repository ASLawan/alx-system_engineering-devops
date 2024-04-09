#!/usr/bin/python3
"""
    Module with function that queries the Reddit API and prints
    the top ten hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """ Returns top ten hot posts from given reddit"""
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    params = {
        'limit': 10
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    dic = response.json()
    posts = dic['data']['children']
    if len(posts) == 0:
        print(None)
    else:
        for post in posts:
            print(post['data']['title'])
