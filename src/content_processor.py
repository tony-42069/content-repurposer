class ContentProcessor:
    def __init__(self):
        self.max_tweet_length = 280

    def process_content(self, content):
        """Process and format content for Twitter."""
        # Remove extra whitespace
        content = ' '.join(content.split())
        
        # Truncate if too long
        if len(content) > self.max_tweet_length:
            content = content[:self.max_tweet_length - 3] + "..."
            
        return content

    def create_thread(self, long_content, max_tweets=5):
        """Split long content into a thread of tweets."""
        words = long_content.split()
        tweets = []
        current_tweet = ""
        
        for word in words:
            if len(current_tweet) + len(word) + 1 <= self.max_tweet_length:
                current_tweet += " " + word if current_tweet else word
            else:
                tweets.append(current_tweet)
                current_tweet = word
                
                if len(tweets) >= max_tweets:
                    break
        
        if current_tweet and len(tweets) < max_tweets:
            tweets.append(current_tweet)
            
        return tweets

    def add_hashtags(self, content, hashtags):
        """Add hashtags to content if there's room."""
        hashtag_text = " " + " ".join(hashtags)
        if len(content) + len(hashtag_text) <= self.max_tweet_length:
            return content + hashtag_text
        return content
