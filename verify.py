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
    auth = tweepy.OAuthHandler(api_key, api_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

api = initialize_tweepy()

# Retrieve authenticated user's details directly from the API response
user = api.verify_credentials()
name = user.name
username = user.screen_name
print(f"Authenticated as {name} (@{username})")
