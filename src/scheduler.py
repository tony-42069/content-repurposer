import schedule
import time
from datetime import datetime
import os
from dotenv import load_dotenv

class ContentScheduler:
    def __init__(self, twitter_client, content_processor):
        load_dotenv()
        self.twitter_client = twitter_client
        self.content_processor = content_processor
        self.posting_interval = int(os.getenv('POSTING_INTERVAL', 3600))
        self.max_tweets_per_day = int(os.getenv('MAX_TWEETS_PER_DAY', 24))
        
    def schedule_post(self, content, post_time):
        """Schedule a post for a specific time."""
        processed_content = self.content_processor.process_content(content)
        schedule.every().day.at(post_time).do(
            self.twitter_client.post_tweet,
            processed_content
        )

    def start(self):
        """Start the scheduling loop."""
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

    def clear_schedule(self):
        """Clear all scheduled jobs."""
        schedule.clear()
