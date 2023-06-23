import pandas as pd
from textblob import TextBlob
import re
import twint

def scrape(cryptocoin):
    coin_search = twint.Config()
    coin_search.Search = cryptocoin
    coin_search.Store_csv = True
    coin_search.Hide_output = True
    coin_search.Count = True
    if cryptocoin == "#Bitcoin":
        coin_search.Output = "../../output_data/raw_tweet_data/bitcoin_tweets_results_snapshot.csv"
    else:
        coin_search.Output = "../../output_data/raw_tweet_data/cardano_tweets_results_snapshot.csv"
    coin_search.Since = "2021-03-14"
    coin_search.Until = "2021-03-31"
    twint.run.Search(coin_search)

def extendedScrape(cryptocoin, year, month):
    coin_search = twint.Config()
    coin_search.Search = cryptocoin
    coin_search.Store_csv = True
    coin_search.Hide_output = True
    coin_search.Limit = 5000
    coin_search.Count = True
    if cryptocoin == "#Bitcoin":
        coin_search.Output = "../../output_data/raw_tweet_data/bitcoin_tweets_results_extended.csv"
    else:
        coin_search.Output = "../../output_data/raw_tweet_data/cardano_tweets_results_extended.csv"
    coin_search.Since = "20%s-%s-01" % (year, month)
    coin_search.Until = "20%s-%s-02" % (year, month)
    print(coin_search.Since)
    print(coin_search.Until)
    print(cryptocoin)
    twint.run.Search(coin_search)

def timeline_scrape(search_term):
    months = ['01', '02', '03', '04', '05',
              '06', '07', '08', '09', '10', '11', '12']
    years = ['18', '19', '20', '21']
    curr_month = 0
    curr_year = 0
    i = 0
    while i < 4:
        if curr_month < 11:
            extendedScrape(search_term, years[curr_year], months[curr_month])
            curr_month += 1
        else:
            extendedScrape(search_term, years[curr_year], months[curr_month])
            curr_month = 0
            curr_year += 1
            i += 1

def cleaned_tweet(original_tweet):
    original_tweet = re.sub('#Bitcoin', 'Bitcoin', original_tweet)
    original_tweet = re.sub('#Cardano', 'Cardano', original_tweet)
    original_tweet = re.sub('#bitcoin', 'bitcoin', original_tweet)
    original_tweet = re.sub('#cardano', 'cardano', original_tweet)
    original_tweet = re.sub('#[A-Za-z0-9]+', '', original_tweet)
    original_tweet = re.sub('@[A-Za-z0-9]+', '', original_tweet)
    original_tweet = re.sub('\\n', '', original_tweet)
    original_tweet = re.sub('https\S+', '', original_tweet)
    return original_tweet

def getSubjectivity(original_tweet):
    return TextBlob(original_tweet).sentiment.subjectivity


def getPolarity(original_tweet):
    return TextBlob(original_tweet).sentiment.polarity

def getSentiment(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'

def dataframe_update(chosen_dataframe, coin, duration):
    chosen_dataframe['Clean_Tweet'] = chosen_dataframe['tweet'].apply(
        cleaned_tweet)

    chosen_dataframe['Subjectivity'] = chosen_dataframe['Clean_Tweet'].apply(
        getSubjectivity)
    chosen_dataframe['Polarity'] = chosen_dataframe['Clean_Tweet'].apply(
        getPolarity)

    chosen_dataframe['Sentiment'] = chosen_dataframe['Polarity'].apply(
        getSentiment)

    chosen_dataframe = chosen_dataframe[chosen_dataframe['language'] == 'en']
    chosen_dataframe.reset_index(inplace=True)

    chosen_dataframe = chosen_dataframe[[
        'date', 'Clean_Tweet', 'Subjectivity', 'Polarity', 'Sentiment']]

    if duration == "snapshot":
        chosen_dataframe.to_csv('../../output_data/clean_tweet_data/%s_cleaned_tweets_snapshot.csv' %
                                (coin))
    else:
        chosen_dataframe.to_csv('../../output_data/clean_tweet_data/%s_cleaned_tweets_extended.csv' %
                                (coin), index=False)

    return chosen_dataframe

def sentiment_dataframe_creation(raw_tweet_data, cryptocoin, duration):
    count_df = raw_tweet_data.groupby(
        'date')['Clean_Tweet'].count().reset_index(name='tweets')
    count_df['date'] = pd.to_datetime(count_df['date'])
    count_df = count_df.set_index('date')
    positive_df = raw_tweet_data.groupby('date')['Sentiment'].apply(
        lambda x: (x == 'Positive').sum()).reset_index(name='positive_sentiment')
    positive_df['date'] = pd.to_datetime(positive_df['date'])
    positive_df = positive_df.set_index('date')
    negative_df = raw_tweet_data.groupby('date')['Sentiment'].apply(
        lambda x: (x == 'Negative').sum()).reset_index(name='negative_sentiment')
    negative_df['date'] = pd.to_datetime(negative_df['date'])
    negative_df = negative_df.set_index('date')
    neutral_df = raw_tweet_data.groupby('date')['Sentiment'].apply(
        lambda x: (x == 'Neutral').sum()).reset_index(name='neutral_sentiment')
    neutral_df['date'] = pd.to_datetime(neutral_df['date'])
    neutral_df = neutral_df.set_index('date')

    average_polarity_df = raw_tweet_data.groupby(
        'date')['Polarity'].mean().reset_index(name='average_polarity')
    average_polarity_df['date'] = pd.to_datetime(average_polarity_df['date'])
    average_polarity_df = average_polarity_df.set_index('date')

    average_subjectivity_df = raw_tweet_data.groupby(
        'date')['Subjectivity'].mean().reset_index(name='average_subjectivity')
    average_subjectivity_df['date'] = pd.to_datetime(
        average_subjectivity_df['date'])
    average_subjectivity_df = average_subjectivity_df.set_index('date')

    sentiment_df = pd.concat([count_df, positive_df, negative_df,
                              neutral_df, average_polarity_df, average_subjectivity_df], axis=1)
    sentiment_df['positive_percentage'] = (sentiment_df.positive_sentiment /
                                           sentiment_df.tweets)
    sentiment_df['negative_percentage'] = (
        sentiment_df.negative_sentiment / sentiment_df.tweets)
    sentiment_df['objective'] = (sentiment_df.positive_sentiment +
                                 sentiment_df.negative_sentiment) / (sentiment_df.tweets)
    sentiment_df['neutral'] = (1 - sentiment_df.objective)

    if duration == 'snapshot':
        sentiment_df.to_csv(
            '../../output_data/sentiment_dataframes_csv/%s_sentiment_dataframe_snapshot.csv' % (cryptocoin))
    else:
        sentiment_df.to_csv(
            '../../output_data/sentiment_dataframes_csv/%s_sentiment_dataframe_extended.csv' % (cryptocoin))

def tweet_volume_console_print(cleaned_tweet_dataframe):
    print("Number of rows ", len(cleaned_tweet_dataframe.index))

scrape("#Bitcoin")
scrape("#Cardano")


timeline_scrape("#Cardano")
timeline_scrape("#Bitcoin")


bitcoin_tweets_snapshot_df = pd.read_csv(
    "../../output_data/raw_tweet_data/btc_tweets_results_snapshot.csv")
cardano_tweets_snapshot_df = pd.read_csv(
    "../../output_data/raw_tweet_data/ada_tweets_results_snapshot.csv")
bitcoin_tweets__extended_df = pd.read_csv(
    "../../output_data/raw_tweet_data/btc_tweets_results_extended.csv")
cardano_tweets_extended_df = pd.read_csv(
    "../../output_data/raw_tweet_data/ada_tweets_results_extended.csv")

dataframe_update(bitcoin_tweets_snapshot_df, "bitcoin", "snapshot")
dataframe_update(cardano_tweets_snapshot_df, "cardano", "snapshot")
dataframe_update(bitcoin_tweets__extended_df, "bitcoin", "extended")
dataframe_update(cardano_tweets_extended_df, "cardano", "extended")


bitcoin_cleaned_tweets_snapshot_df = pd.read_csv(
    "../../output_data/clean_tweet_data/bitcoin_cleaned_tweets_snapshot.csv", lineterminator='\n')
cardano_cleaned_tweets_snapshot_df = pd.read_csv(
    "../../output_data/clean_tweet_data/cardano_cleaned_tweets_snapshot.csv", lineterminator='\n')
bitcoin_cleaned_tweets_extended_df = pd.read_csv(
    "../../output_data/clean_tweet_data/bitcoin_cleaned_tweets_extended.csv", lineterminator='\n')
cardano_cleaned_tweets_extended_df = pd.read_csv(
    "../../output_data/clean_tweet_data/cardano_cleaned_tweets_extended.csv",lineterminator='\n')


sentiment_dataframe_creation(bitcoin_cleaned_tweets_snapshot_df, "bitcoin", "snapshot")
sentiment_dataframe_creation(cardano_cleaned_tweets_snapshot_df, "cardano", "snapshot")
sentiment_dataframe_creation(
    bitcoin_cleaned_tweets_extended_df, "bitcoin", "extended")
sentiment_dataframe_creation(
    cardano_cleaned_tweets_extended_df, "cardano", "extended")
