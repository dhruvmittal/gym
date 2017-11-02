from flask import Flask, render_template, request, redirect
from twitterscraper import query_tweets

app = Flask(__name__)

const_account_name = 'DidAnGoToTheGym'
const_twitter_query = 'from%3A' + const_account_name


@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
    mrt = get_most_recent_tweet()  
    return render_template('index.html', tweet_text=mrt.text, tweet_time=mrt.time)


def get_most_recent_tweet():
    tweet = query_tweets(const_twitter_query, 1)[0]
    return { 'user': tweet.user
            , 'timestamp': tweet.timestamp
            , 'text' : tweet.text
           }



if __name__ == '__main__':
  app.run(host='0.0.0.0',port=33507)
