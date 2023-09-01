import pytest
from xintegrator import Integration
import plotly
from bs4 import BeautifulSoup


@pytest.fixture
def rihanna():
    return Integration("rihanna")


def test_username_is_string():
    with pytest.raises(ValueError):
        Integration(42)


def test_create_integration_rihanna(rihanna):
    assert rihanna.user_id == "79293791"


def test_get_user_timeline(rihanna):
    timeline = rihanna._get_user_timeline(max_results=5)
    assert timeline["meta"]["result_count"] > 0


def test_get_mentions_timeline(rihanna):
    mentions = rihanna._get_mentions_timeline(max_results=5)
    assert mentions["meta"]["result_count"] > 0


def test_get_user_tweet_table(rihanna):
    rihanna.get_tweet_table(5, "mentions")


def test_visualization(rihanna):
    rihanna.get_tweet_table(max_results=6, type="user")
    fig = rihanna.visualize_popularity(rihanna.user_tweet_table)
    assert isinstance(fig, plotly.graph_objs._figure.Figure)


def test_get_tweet_table(rihanna):
    with pytest.raises(ValueError):
        rihanna.get_tweet_table(5, type="non_existant_type")


def test_get_posts_as_embedded(rihanna):
    rihanna.get_tweet_table(max_results=5, type="mentions")
    posts = rihanna.get_posts_as_embedded("mentions")

    assert "blockquote" in posts[0]
