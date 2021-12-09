# Twitter Keyword Alert and Dogecoin Auto-Buy Bot

This bot monitors tweets from a specific Twitter profile for a specific keyword and alerts the user when a new tweet is found containing the keyword. Additionally, if the keyword is "doge" and the tweet is from Elon Musk, the bot will automatically place a buy order for Dogecoin on Binance.

## Installation

1. Clone the repository: `git clone https://github.com/username/twitter-bot.git`
2. Install the required packages: `pip install tweepy python-binance`
3. Create a Twitter developer account and obtain API keys and access tokens for the account.
4. Create a Binance account and obtain API keys for the account.

## Usage

1. Run the bot with `python main.py`.
2. Enter the Twitter username to monitor and the keyword to search for.
3. If the keyword is "doge" and the tweet is from Elon Musk, the bot will ask for confirmation before placing a buy order for Dogecoin on Binance.
4. The bot will continue to run and monitor the specified Twitter account for new tweets containing the keyword.

## Configuration

The following values can be configured in the `config.py` file:

- `TWITTER_CONSUMER_KEY`: The Twitter API consumer key.
- `TWITTER_CONSUMER_SECRET`: The Twitter API consumer secret.
- `TWITTER_ACCESS_TOKEN`: The Twitter API access token.
- `TWITTER_ACCESS_TOKEN_SECRET`: The Twitter API access token secret.
- `BINANCE_API_KEY`: The Binance API key.
- `BINANCE_SECRET_KEY`: The Binance secret key.
- `SYMBOL`: The symbol to trade on Binance.
- `QUANTITY`: The quantity to buy on Binance.

## Disclaimer

Use this bot at your own risk. The author is not responsible for any financial losses incurred as a result of using this bot.
