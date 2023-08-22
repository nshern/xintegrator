from x_integrator.__main__ import Integration


def test_create_integration():
    rihanna = Integration("rihanna")
    assert rihanna.user_id == "79293791"


def test_get_user_timeline():
    rihanna = Integration("rihanna")
    timeline = rihanna._get_user_timeline()
    assert timeline["meta"]["result_count"] > 0
