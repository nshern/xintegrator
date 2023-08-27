import pytest
from xintegrator import Integration
import plotly


def test_username_is_string():
    with pytest.raises(ValueError):
        rihanna = Integration(42)


def test_create_integration_rihanna():
    rihanna = Integration("rihanna")
    assert rihanna.user_id == "79293791"


def test_get_user_timeline():
    rihanna = Integration("rihanna")
    timeline = rihanna._get_user_timeline(max_results=5)
    assert timeline["meta"]["result_count"] > 0


def test_visualization():
    rihanna = Integration("rihanna")
    rihanna.get_tweet_table(6)
    fig = rihanna.visualize_popularity(rihanna.tweet_table)
    assert isinstance(fig, plotly.graph_objs._figure.Figure)
