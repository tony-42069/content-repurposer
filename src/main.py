from twitter_client import TwitterClient
from content_processor import ContentProcessor
from scheduler import ContentScheduler

def main():
    # Initialize components
    twitter_client = TwitterClient()
    content_processor = ContentProcessor()
    scheduler = ContentScheduler(twitter_client, content_processor)

    # Example usage
    content = "This is a test tweet from our content repurposer!"
    processed_content = content_processor.process_content(content)
    
    # Post directly
    twitter_client.post_tweet(processed_content)
    
    # Or schedule for later
    scheduler.schedule_post("Scheduled tweet content", "14:00")
    
    # Start the scheduler
    scheduler.start()

if __name__ == "__main__":
    main()
