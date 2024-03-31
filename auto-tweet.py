import tweepy
import datetime
import schedule
import time
import config

### CONFIG
bearer_token = config.BEARER_TOKEN
api_key = config.API_KEY
api_secret = config.API_SECRET
access_token = config.ACCESS_TOKEN
access_token_secret = config.ACCESS_TOKEN_SECRET
interval = config.INTERVAL

posted_tweets = set()

def initialize_tweepy():
    client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
    auth = tweepy.OAuthHandler(api_key, api_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    return client, api

def get_formatted_date():
    current_date = datetime.date.today()
    return current_date.strftime("%B %d, %Y")

def send_post():
    client, _ = initialize_tweepy()

    with open(('tweets.txt'), 'r') as file:
        lines = file.readlines()

    lines = [tweet for tweet in lines if tweet.strip() not in posted_tweets]

    if lines: 
        tweet_text = lines.pop(0).strip()  # Get and remove the first tweet from the list
        client.create_tweet(text=f"{tweet_text}")
        confirmation = f"'{tweet_text}' has been tweeted successfully on {get_formatted_date()}"
        print(confirmation)
        posted_tweets.add(tweet_text)
    else:
        print("No new tweets to post.")

    # Reschedule the send_post function to run again after the specified interval
    schedule.every(interval).minutes.do(send_post)

def run_scheduler():
    print('Auto tweet has started')
    send_post()  # Start by sending the first tweet immediately
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_scheduler()
