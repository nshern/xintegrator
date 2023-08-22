from x_integrator.__main__ import Integration
import plotly


def test_create_integration():
    rihanna = Integration("rihanna")
    assert rihanna.user_id == "79293791"


def test_get_user_timeline():
    rihanna = Integration("rihanna")
    timeline = rihanna._get_user_timeline()
    assert timeline["meta"]["result_count"] > 0


def test_visualization():
    rihanna = Integration("rihanna")
    rihanna.get_tweet_table(2)
    fig = rihanna.visualize_popularity(rihanna.tweet_table)
    assert isinstance(fig, plotly.graph_objs._figure.Figure)
