# Auto Tweet Scheduler

This Python program automates the process of posting tweets at regular intervals using the Tweepy library and the Twitter API.

## Setup

1. **Install Dependencies**: Make sure you have Python installed on your system. You also need to install the Tweepy library. You can install it using pip:

    ```
    pip install tweepy
    ```

    If schedule is not installed, install it using pip:

   ```
   pip install schedule
   ```

3. **Twitter API Credentials**: Obtain your Twitter API credentials (API key, API secret key, Access token, and Access token secret) from the Twitter Developer Portal. You'll need these credentials to authenticate with the Twitter API.

4. **Configuration**: Create a `config.py` file in the same directory as the program and define your Twitter API credentials and other configurations:

    ```python
    BEARER_TOKEN = "YOUR_BEARER_TOKEN"
    API_KEY = "YOUR_API_KEY"
    API_SECRET = "YOUR_API_SECRET"
    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
    ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"
    INTERVAL = 60  # Interval in minutes
    ```

5. **Tweet Text**: Prepare your tweet messages and save them in a file named `tweets.txt`. Each line in this file represents a tweet message.

## Usage

To start the auto tweet scheduler:

1. Run the program by executing the following command in your terminal:

    ```
    python auto_tweet.py
    ```

2. The program will start posting tweets at regular intervals specified in the `INTERVAL` variable in the `config.py` file.

3. The program will continue running indefinitely, posting tweets according to the schedule.

## Notes

- Make sure your system's date and time settings are accurate for proper scheduling.
- Ensure that your Twitter API credentials are kept secure and not shared publicly.
- You can modify the `INTERVAL` variable in the `config.py` file to change the posting frequency.
- Remember to include meaningful and engaging tweet messages in the `tweets.txt` file to keep your audience interested.
- Because of Twitter's limitations to posting content (you cannot repeat the same tweet in any 24 hours), a set called `posted_tweets` is created and the bot will stop posting when you've run out of tweets.

