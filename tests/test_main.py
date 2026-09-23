from bmi_530_github_actions_demo.main import add


def test_add() -> None:
    assert add(2, 3) == 5
