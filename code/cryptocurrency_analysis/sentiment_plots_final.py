import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def coin_prices(chosen_dataframe, duration, search_term):
    df = pd.DataFrame(chosen_dataframe, columns=['Date', 'Close'])
    df.plot.line(x='Date', y='Close', color='blue')
    plt.ylabel('Close Price ($USD)')
    plt.title("%s Prices" % (search_term.capitalize()))
    plt.xticks(rotation=45)
    if duration == "snapshot":
        plt.savefig('../../output_data/plots/coin_price/%s_price_snapshot.png' %
                    (search_term), bbox_inches='tight')
    else:
        plt.savefig('../../output_data/plots/coin_price/%s_price_extended.png' %
                    (search_term), bbox_inches='tight')

def polarity_hist(chosen_dataframe, duration, search_term):
    total_bins = 60
    plt.hist(
        chosen_dataframe.Polarity, total_bins, facecolor='Purple')
    plt.xlabel('Polarity')
    plt.ylabel('Volume of Tweets')
    if duration == "snapshot":
        plt.title('%s Polarity Distribution Mar 2021' %
                  (search_term.capitalize()))
        plt.savefig('../../output_data/plots/polarity/%s_polarity_dist_snapshot.png' %
                    (search_term), bbox_inches='tight')
    else:
        plt.title('%s Polarity Distribution 2018-2021' %
                  (search_term.capitalize()))
        plt.savefig('../../output_data/plots/polarity/%s_polarity_dist_extended.png' %
                    (search_term), bbox_inches='tight')

def objec_neut_bar(chosen_dataframe, duration, search_term):
    plt.figure(figsize=(12, 10))
    pos_bar = plt.barh(chosen_dataframe.date,
                       (chosen_dataframe.positive_percentage), color='blue')
    neg_bar = plt.barh(chosen_dataframe.date,
                       (chosen_dataframe.negative_percentage), left=chosen_dataframe.positive_percentage,  color='red')
    neut_bar = plt.barh(chosen_dataframe.date, chosen_dataframe.neutral, left=(chosen_dataframe.positive_percentage + chosen_dataframe.negative_percentage),
                        color='grey')
    plt.legend([pos_bar, neg_bar, neut_bar], ["Positive Tweets", "Negative Tweets",
                                              "Neutral Tweets"], title="% Breakdown", loc="upper right")
    if duration == "snapshot":
        plt.title('%s Ojective vs Neutral Distribution Mar 2021' %
                  (search_term.capitalize()))
        plt.savefig('../../output_data/plots/objectivity/%s_object_neut_bar_snapshot.png' %
                    (search_term), bbox_inches='tight')
    else:
        plt.title('%s Ojective vs Neutral Distribution 2018-2021' %
                  search_term.capitalize())
        plt.savefig('../../output_data/plots/objectivity/%s_object_neut_bar_extended.png' %
                    (search_term), bbox_inches='tight')

def sentiment_price_graph(chosen_dataframe, chosen_prices_dataframe, duration, search_term):
    fig, ax1 = plt.subplots()
    plt.xticks(rotation=45)
    ax1.set_ylabel('Average Polarity', color='blue')
    ax1.plot(chosen_dataframe.date,
             chosen_dataframe.average_polarity, color='blue')
    ax2 = ax1.twinx()
    ax2.set_ylabel('Close Price ($USD)', color='green')
    ax2.plot(chosen_dataframe.date,
             chosen_prices_dataframe.Close, color='green')
    fig.tight_layout()
    if duration == "snapshot":
        ax1.set_xlabel('Date')
        plt.title('%s Average Polarity vs Price Mar 2021' %
                  search_term.capitalize())
        plt.savefig('../../output_data/plots/sentiment_price/%s_price_vs_polarity_snapshot.png' %
                    (search_term), bbox_inches='tight')
    else:
        plt.xticks([])
        plt.title('%s Average Polarity vs Price Jan 2018 - Aug 2021' %
                  search_term.capitalize())
        ax1.set_xlabel('January 2018 - August 2021')
        plt.savefig('../../output_data/plots/sentiment_price/%s_price_vs_polarity_extended.png' %
                    (search_term), bbox_inches='tight')

def price_vs_tweet_volume(chosen_dataframe, chosen_prices_dataframe, duration, search_term):
    fig, ax1 = plt.subplots()
    plt.xticks(rotation=45)
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Tweet Volume', color='blue')
    ax1.plot(chosen_dataframe.Date,
             chosen_dataframe.Tweets, color='blue')
    ax2 = ax1.twinx()
    ax2.set_ylabel('Close Price ($USD)', color='green')
    ax2.plot(chosen_dataframe.Date,
             chosen_prices_dataframe.Close, color='green')
    fig.tight_layout()
    if duration == "snapshot":
        plt.title('%s Tweet Volume vs Price Mar 2021' %
                  search_term.capitalize())
        plt.savefig('../../output_data/plots/tweet_volume_price/%s_price_vs_tweet_snapshot.png' %
                    (search_term), bbox_inches='tight')
    else:
        plt.xticks([])
        plt.title('%s Tweet Volume vs Price Jan 2018 - Aug 2021' %
                  search_term.capitalize())
        plt.savefig('../../output_data/plots/tweet_volume_price/%s_price_vs_tweet_extended.png' %
                    (search_term), bbox_inches='tight')

def price_vs_google_trend(chosen_dataframe, chosen_prices_dataframe, duration, search_term):
    fig, ax1 = plt.subplots()
    plt.xticks(rotation=45)
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Trend Interest', color='blue')
    ax1.plot(chosen_dataframe.Date,
             chosen_dataframe.Search_Volume, color='blue')
    ax2 = ax1.twinx()
    ax2.set_ylabel('Close Price ($USD)', color='green')
    ax2.plot(chosen_dataframe.Date,
             chosen_prices_dataframe.Close, color='green')
    fig.tight_layout()
    if duration == "snapshot":
        plt.title('%s Google Trend Interest vs Price Mar 2021' %
                  search_term.capitalize())
        plt.savefig('../../output_data/plots/google_trend_price/%s_price_vs_google_snapshot.png' %
                    (search_term), bbox_inches='tight')
    else:
        plt.xticks([])
        plt.title('%s Google Trend Interest vs Price Jan 2018 - Aug 2021' %
                  search_term.capitalize())
        plt.savefig('../../output_data/plots/google_trend_price/%s_price_vs_google_extended.png' %
                    (search_term), bbox_inches='tight')

def tweet_volume_graph(chosen_dataframe, duration, search_term):
    chosen_dataframe.plot.line(x='Date', y='Tweets',  color='blue')
    plt.xticks(rotation=45)
    if duration == 'snapshot':
        plt.title('%s Total Tweet Volume Mar 2021' % search_term.capitalize())
        plt.savefig('../../output_data/plots/tweet_volume/%s_tweet_volume_snapshot.png' %
                    (search_term), bbox_inches='tight')
    else:
        plt.title('%s Total Tweet Volume 2018 - 2021' %
                  search_term.capitalize())
        plt.savefig('../../output_data/plots/tweet_volume/%s_tweet_volume_extended.png' %
                    (search_term), bbox_inches='tight')

def corr_graph(chosen_dataframe, duration, search_term):
    correlation = chosen_dataframe.corr()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    axis_parameters = ax.matshow(correlation, cmap='seismic', vmin=-1, vmax=1)
    fig.colorbar(axis_parameters)
    tick_marks = np.arange(0, len(chosen_dataframe.columns), 1)
    ax.set_xticks(tick_marks)
    ax.set_yticks(tick_marks)
    ax.set_xticklabels(chosen_dataframe.columns)
    ax.set_yticklabels(chosen_dataframe.columns)
    plt.xticks(rotation=45)
    plt.title("%s Correlation HeatMap" % (search_term.capitalize()))
    if duration == "snapshot":
        plt.savefig('../../output_data/plots/correlation/%s_correlation_snapshot.png' %
                    (search_term), bbox_inches='tight')
    else:
        plt.savefig('../../output_data/plots/correlation/%s_correlation_extended.png' %
                    (search_term), bbox_inches='tight')

# Coin Charts

bitcoin_price_snapshot_df = pd.read_csv(
    "../../input_data/bitcoin_cp_snapshot.csv")

bitcoin_price_extended_df = pd.read_csv(
    "../../input_data/bitcoin_cp_extended.csv")

cardano_price_snapshot_df = pd.read_csv(
    "../../input_data/cardano_cp_snapshot.csv")

cardano_price_extended_df = pd.read_csv(
    "../../input_data/cardano_cp_extended.csv")

coin_prices(bitcoin_price_snapshot_df, "snapshot", "bitcoin")
coin_prices(bitcoin_price_extended_df, "extended", "bitcoin")
coin_prices(cardano_price_snapshot_df, "snapshot", "cardano")
coin_prices(cardano_price_extended_df, "extended", "cardano")

# Polarity Histograms

bitcoin_cleaned_snapshot_df = pd.read_csv(
    "../../output_data/clean_tweet_data/bitcoin_cleaned_tweets_snapshot.csv", lineterminator='\n')
bitcoin_cleaned_snapshot_df['date'] = pd.to_datetime(
    bitcoin_cleaned_snapshot_df['date'])

bitcoin_cleaned_extended_df = pd.read_csv(
    "../../output_data/clean_tweet_data/bitcoin_cleaned_tweets_extended.csv", lineterminator='\n')
bitcoin_cleaned_extended_df['date'] = pd.to_datetime(
    bitcoin_cleaned_extended_df['date'])

cardano_cleaned_snapshot_df = pd.read_csv(
    "../../output_data/clean_tweet_data/cardano_cleaned_tweets_snapshot.csv", lineterminator='\n')
cardano_cleaned_snapshot_df['date'] = pd.to_datetime(
    cardano_cleaned_snapshot_df['date'])

cardano_cleaned_extended_df = pd.read_csv(
    "../../output_data/clean_tweet_data/cardano_cleaned_tweets_extended.csv", lineterminator='\n')
cardano_cleaned_extended_df['date'] = pd.to_datetime(
    cardano_cleaned_extended_df['date'])

polarity_hist(bitcoin_cleaned_snapshot_df, "snapshot", "bitcoin")
polarity_hist(bitcoin_cleaned_extended_df, "extended", "bitcoin")
polarity_hist(cardano_cleaned_snapshot_df, "snapshot", "cardano")
polarity_hist(cardano_cleaned_extended_df, "extended", "cardano")

# Ojectivity vs Neutrality

bitcoin_sentiment_snapshot_df = pd.read_csv(
    "../../output_data/sentiment_dataframes_csv/bitcoin_sentiment_dataframe_snapshot.csv", lineterminator='\n')

bitcoin_sentiment_extended_df = pd.read_csv(
    "../../output_data/sentiment_dataframes_csv/bitcoin_sentiment_dataframe_extended.csv")

cardano_sentiment_snapshot_df = pd.read_csv(
    "../../output_data/sentiment_dataframes_csv/cardano_sentiment_dataframe_snapshot.csv", lineterminator='\n')

cardano_sentiment_extended_df = pd.read_csv(
    "../../output_data/sentiment_dataframes_csv/cardano_sentiment_dataframe_extended.csv")

objec_neut_bar(bitcoin_sentiment_snapshot_df, "snapshot", "bitcoin")
objec_neut_bar(bitcoin_sentiment_extended_df, "extended", "bitcoin")
objec_neut_bar(cardano_sentiment_snapshot_df, "snapshot", "cardano")
objec_neut_bar(cardano_sentiment_extended_df, "extended", "cardano")

# Sentiment vs Price

bitcoin_sentiment_snapshot_df = pd.read_csv(
    "../../output_data/sentiment_dataframes_csv/bitcoin_sentiment_dataframe_snapshot.csv", lineterminator='\n')

bitcoin_price_snapshot_df = pd.read_csv(
    "../../input_data/bitcoin_cp_snapshot.csv")

bitcoin_sentiment_extended_df = pd.read_csv(
    "../../output_data/sentiment_dataframes_csv/bitcoin_sentiment_dataframe_extended.csv")

bitcoin_price_month_extended_df = pd.read_csv(
    "../../input_data/bitcoin_cp_month_extended.csv")

cardano_sentiment_snapshot_df = pd.read_csv(
    "../../output_data/sentiment_dataframes_csv/cardano_sentiment_dataframe_snapshot.csv", lineterminator='\n')

cardano_price_snapshot_df = pd.read_csv(
    "../../input_data/cardano_cp_snapshot.csv")

cardano_sentiment_extended_df = pd.read_csv(
    "../../output_data/sentiment_dataframes_csv/cardano_sentiment_dataframe_extended.csv")

cardano_price_month_extended_df = pd.read_csv(
    "../../input_data/cardano_cp_month_extended.csv")


sentiment_price_graph(bitcoin_sentiment_snapshot_df,
                      bitcoin_price_snapshot_df, "snapshot", "bitcoin")
sentiment_price_graph(bitcoin_sentiment_extended_df,
                      bitcoin_price_month_extended_df, "extended", "bitcoin")
sentiment_price_graph(cardano_sentiment_snapshot_df,
                      cardano_price_snapshot_df, "snapshot", "cardano")
sentiment_price_graph(cardano_sentiment_extended_df,
                      cardano_price_month_extended_df, "extended", "cardano")

# Tweet Volumes

bitcoin_tweet_volume_snapshot_df = pd.read_csv(
    "../../input_data/bitcoin_tv_snapshot.csv")
bitcoin_tweet_volume_extended_df = pd.read_csv(
    "../../input_data/bitcoin_tv_extended.csv")
cardano_tweet_volume_snapshot_df = pd.read_csv(
    "../../input_data/cardano_tv_snapshot.csv")
cardano_tweet_volume_extended_df = pd.read_csv(
    "../../input_data/cardano_tv_extended.csv")

tweet_volume_graph(bitcoin_tweet_volume_snapshot_df, "snapshot", "bitcoin")
tweet_volume_graph(bitcoin_tweet_volume_extended_df, "extended", "bitcoin")
tweet_volume_graph(cardano_tweet_volume_snapshot_df, "snapshot", "cardano")
tweet_volume_graph(cardano_tweet_volume_extended_df, "extended", "cardano")

# Price vs Tweet Volume

bitcoin_tweet_volume_snapshot_df = pd.read_csv(
    "../../input_data/bitcoin_tv_snapshot.csv")

bitcoin_price_snapshot_df = pd.read_csv(
    "../../input_data/bitcoin_cp_snapshot.csv")

bitcoin_tweet_volume_extended_df = pd.read_csv(
    "../../input_data/bitcoin_tv_extended.csv")

bitcoin_price_extended_df = pd.read_csv(
    "../../input_data/bitcoin_cp_extended.csv")

cardano_tweet_volume_snapshot_df = pd.read_csv(
    "../../input_data/cardano_tv_snapshot.csv")

cardano_price_snapshot_df = pd.read_csv(
    "../../input_data/cardano_cp_snapshot.csv")

cardano_tweet_volume_extended_df = pd.read_csv(
    "../../input_data/cardano_tv_extended.csv")

cardano_price_extended_df = pd.read_csv(
    "../../input_data/cardano_cp_extended.csv")

price_vs_tweet_volume(bitcoin_tweet_volume_snapshot_df,
                      bitcoin_price_snapshot_df, "snapshot", "bitcoin")
price_vs_tweet_volume(bitcoin_tweet_volume_extended_df,
                      bitcoin_price_extended_df, "extended", "bitcoin")
price_vs_tweet_volume(cardano_tweet_volume_snapshot_df,
                      cardano_price_snapshot_df, "snapshot", "cardano")
price_vs_tweet_volume(cardano_tweet_volume_extended_df,
                      cardano_price_extended_df, "extended", "cardano")


# Price vs Google Trends

bitcoin_google_trend_snapshot_df = pd.read_csv(
    "../../input_data/bitcoin_gt_snapshot.csv")

bitcoin_price_snapshot_df = pd.read_csv(
    "../../input_data/bitcoin_cp_snapshot.csv")

bitcoin_google_trend_extended_df = pd.read_csv(
    "../../input_data/bitcoin_gt_extended.csv")

bitcoin_price_extended_df = pd.read_csv(
    "../../input_data/bitcoin_cp_week_extended.csv")

cardano_google_trend_snapshot_df = pd.read_csv(
    "../../input_data/cardano_gt_snapshot.csv")

cardano_price_snapshot_df = pd.read_csv(
    "../../input_data/cardano_cp_snapshot.csv")

cardano_google_trend_extended_df = pd.read_csv(
    "../../input_data/cardano_gt_extended.csv")

cardano_price_extended_df = pd.read_csv(
    "../../input_data/cardano_cp_week_extended.csv")

price_vs_google_trend(bitcoin_google_trend_snapshot_df,
                      bitcoin_price_snapshot_df, "snapshot", "bitcoin")
price_vs_google_trend(bitcoin_google_trend_extended_df,
                      bitcoin_price_extended_df, "extended", "bitcoin")
price_vs_google_trend(cardano_google_trend_snapshot_df,
                      cardano_price_snapshot_df, "snapshot", "cardano")
price_vs_google_trend(cardano_google_trend_extended_df,
                      cardano_price_extended_df, "extended", "cardano")


corr_df = pd.read_csv(
    "../../output_data/correlation_data/bitcoin_correlation.csv")
corr_graph(corr_df, "snapshot", "bitcoin")

corr_df = pd.read_csv(
    "../../output_data/correlation_data/cardano_correlation.csv")
corr_graph(corr_df, "snapshot", "cardano")
