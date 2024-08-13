#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        try:
            data = response.json()
            if 'data' in data and 'subscribers' in data['data']:
                subscribers = data['data']['subscribers']
                return subscribers
            else:
                return 0
        except json.JSONDecodeError:
            return 0
    else:
        return 0