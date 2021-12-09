import tweepy
from binance.client import Client
from config import *
import time
# Twitter profile and keyword to monitor
twitter_profile = 'elonmusk'
keyword = 'doge'

# Binance client instance
client = Client(api_key=binance_api_key, api_secret=binance_api_secret)

# Twitter authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Twitter API instance
api = tweepy.API(auth)

# Keep track of the most recent tweet ID
since_id = None

# Loop to continuously monitor the Twitter profile
while True:
    try:
        # Get the latest tweet from the Twitter profile
        tweets = api.user_timeline(screen_name=twitter_profile, count=1, since_id=since_id)
        
        # If a new tweet was found
        if tweets:
            tweet = tweets[0]
            since_id = tweet.id
            
            # Check if the tweet contains the keyword
            if keyword in tweet.text.lower():
                # Buy dogecoin on Binance
                try:
                    order = client.order_market_buy(symbol='DOGEUSDT', quantity=100)
                    print('Bought DOGE at market price:', order['fills'][0]['price'])
                except Exception as e:
                    print('Error:', e)
            
            # Print the tweet text
            print(tweet.text)
        
        # Wait for 60 seconds before checking again
        time.sleep(60)
    
    except tweepy.TweepError as e:
        print('Error:', e)
        time.sleep(60)
