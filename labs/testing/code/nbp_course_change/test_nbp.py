import requests

from nbp_change import calc_statistics


class MockResponse:
    @staticmethod
    def json():
        return {'currency': 'dolar', 'rates': [{'mid': 1}, {'mid': 2}, {'mid': 4}]}


def test_calc_statistics(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    result = {'AUD': {'change': 4.0, 'course': 4, 'full_name': 'dolar'}}
    assert calc_statistics(['AUD'], 3) == result