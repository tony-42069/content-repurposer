import os
import tweepy
from dotenv import load_dotenv

class TwitterClient:
    def __init__(self):
        load_dotenv()
        
        # Initialize Twitter API client
        auth = tweepy.OAuthHandler(
            os.getenv('TWITTER_API_KEY'),
            os.getenv('TWITTER_API_SECRET')
        )
        auth.set_access_token(
            os.getenv('TWITTER_ACCESS_TOKEN'),
            os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        )
        self.api = tweepy.API(auth)
        self.client = tweepy.Client(
            consumer_key=os.getenv('TWITTER_API_KEY'),
            consumer_secret=os.getenv('TWITTER_API_SECRET'),
            access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
            access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        )

    def post_tweet(self, content):
        """Post a tweet with the given content."""
        try:
            response = self.client.create_tweet(text=content)
            return response
        except Exception as e:
            print(f"Error posting tweet: {str(e)}")
            return None

    def get_user_tweets(self, username, count=10):
        """Fetch recent tweets from a specific user."""
        try:
            user = self.client.get_user(username=username)
            tweets = self.client.get_users_tweets(user.data.id, max_results=count)
            return tweets
        except Exception as e:
            print(f"Error fetching tweets: {str(e)}")
            return None
