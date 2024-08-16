import asyncio
import pandas as pd
from twscrape import API
from twscrape.logger import set_log_level

# Initialize an empty list to store tweet data
tweets_data = []

async def main():
    api = API()
    
    q = "USA bans Huawei since:2022-09-01 until:2022-12-01"
    async for tweet in api.search(q, limit=5000):
        # Append a dictionary for each tweet to the tweets_data list
        tweets_data.append({
			'username': tweet.user.username,
			'followersCount' : tweet.user.followersCount,
			'location' : tweet.user.location,
            'id': tweet.id,
			'id_str':tweet.id_str,
            'rawcontent': tweet.rawContent,
            'replyCount': tweet.replyCount,
			'retweetCount': tweet.retweetCount,
			'likeCount': tweet.likeCount,
			'quoteCount': tweet.quoteCount,
			'hashtags':tweet.hashtags,
			'created': tweet.user.created
        })

    # Convert the list of dictionaries into a pandas DataFrame
    df = pd.DataFrame(tweets_data)
	
    # Convert timezone-aware datetime objects to timezone-naive
    if not df.empty and 'created' in df.columns:
        df['created'] = pd.to_datetime(df['created']).dt.tz_localize(None)
        df['date_created'] = df['created'].dt.date
        df['time_created'] = df['created'].dt.strftime('%H:%M:%S')

	   
    # Save the DataFrame to an Excel file
    df.to_csv('tweets_data.csv', index=False)

if __name__ == "__main__":
    asyncio.run(main())
