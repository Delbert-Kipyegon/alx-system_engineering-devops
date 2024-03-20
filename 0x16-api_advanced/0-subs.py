#!/usr/bin/python3

"""
A script that queries the Reddit API and returns the number of subscribers
for a given subreddit. If an invalid subreddit is given, the function returns 0.
"""
import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Python:subreddit.subscriber.counter:v1.0 (by /u/IndependenceMotor409)'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            return data.get('subscribers', 0)
        else:
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
