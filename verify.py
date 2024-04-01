import tweepy
import config

### CONFIG
bearer_token = config.BEARER_TOKEN
api_key = config.API_KEY
api_secret = config.API_SECRET
access_token = config.ACCESS_TOKEN
access_token_secret = config.ACCESS_TOKEN_SECRET
interval = config.INTERVAL

def initialize_tweepy():
    client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
    return client

client = initialize_tweepy()
user = client.me()  # Retrieve authenticated user's details
name = user.name
username = user.username
print(f"Authenticated as {name} (@{username})")