from xintegrator import Integration

rihanna = Integration("rihanna")

rihanna.get_tweet_table(max_results=5, type="user")

fig = rihanna.visualize_popularity(rihanna.user_tweet_table)

fig.show()
