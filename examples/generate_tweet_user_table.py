from xintegrator import Integration
import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
# pd.set_option("display.width", None)
# pd.set_option("display.max_colwidth", -1)

rihanna = Integration("rihanna")

rihanna.get_tweet_table(max_results="5", type="user")

table = rihanna.user_tweet_table

print(table)
