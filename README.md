# Twitter Content Repurposer

A Python-based tool for repurposing and managing content for X/Twitter. This tool helps automate the process of content creation and posting on Twitter.

## Features

- Twitter API integration
- Content processing and transformation
- Scheduled posting
- Content management

## Setup

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your Twitter API credentials:
   ```
   TWITTER_API_KEY=your_api_key
   TWITTER_API_SECRET=your_api_secret
   TWITTER_ACCESS_TOKEN=your_access_token
   TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
   ```

## Project Structure

- `src/` - Main source code directory
  - `twitter_client.py` - Twitter API interaction
  - `content_processor.py` - Content processing logic
  - `scheduler.py` - Scheduling functionality
- `config/` - Configuration files
- `.env` - Environment variables (not tracked in git)
- `requirements.txt` - Python dependencies

## Usage

1. Set up your Twitter API credentials in the `.env` file
2. Run the main script:
   ```
   python src/main.py
   ```

## License

MIT
