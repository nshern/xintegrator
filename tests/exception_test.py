import pytest
from xintegrator import Integration, TooManyRequestsError


@pytest.fixture
def rihanna():
    return Integration("rihanna")


def test_429_error(rihanna):
    with pytest.raises(TooManyRequestsError):
        for i in range(50):
            rihanna.get_tweet_table(max_results=5, type="mentions")
