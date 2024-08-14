'''
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
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
        '''
#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests
import sys

def get_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        int: The number of subscribers. Returns 0 if the subreddit does not exist or the request fails.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    except requests.RequestException as e:
        print(f"Error: {e}", file=sys.stderr)
        return 0
    
    data = response.json()
    return data['data']['subscribers']

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <subreddit_name>", file=sys.stderr)
        sys.exit(1)
    
    subreddit = sys.argv[1]
    subscribers = get_subscribers(subreddit)
    print(f"The subreddit r/{subreddit} has {subscribers} subscribers.")
