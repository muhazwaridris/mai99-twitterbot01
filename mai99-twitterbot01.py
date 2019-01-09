import tweepy
import time

print ('Loading mai99-twitterbot01 program...')

consumer_key = 'xxxxxxxxx'
consumer_secret = 'xxxxxxxxx'
access_token = 'xxxxxxxxx'
access_token_secret = 'xxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Last Saved ID Tweet 1035421687725129728 for testing.
FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('Retrieving newest tweet from twitter server...', flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # Use tweet_mode='extended' and full_text to display long tweet.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if 'hai kak' in mention.full_text.lower():
            print('Found tweet that mentioning you, responding back...', flush=True)
            api.update_status('Hai @' + mention.user.screen_name +
                    ', this is just automatic reply, this is happen because you are mentioning me with a word "hai kak"', mention.id)
            time.sleep(3)
        print('Retrieving newest tweet from twitter server is complete!')
        print('Restart mai99-twitterbot01 program...')
        time.sleep(3)
        print('<=============================================================>')

while True:
    reply_to_tweets()