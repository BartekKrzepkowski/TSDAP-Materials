import os


def get_config():
    return int(os.environ.get("VERBOSITY"))
    # return int(os.getenv("VERBOSITY"))


def test_get_config(monkeypatch):
    monkeypatch.setenv('VERBOSITY', '0')
    assert get_config() == 0
