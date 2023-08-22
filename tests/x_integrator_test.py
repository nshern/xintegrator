from x_integrator.__main__ import Integration


def test_create_integration():
    rihanna = Integration("rihanna")
    assert rihanna.user_id == "79293791"
