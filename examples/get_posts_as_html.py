from xintegrator import Integration

riri = Integration("rihanna")

riri.get_tweet_table(max_results=5, type="mentions")

doc = riri.get_posts_as_embedded("mentions")

print(doc)
