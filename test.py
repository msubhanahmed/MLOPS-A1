import pytest
from app import app


@pytest.fixture
def client():
    yield app.test_client()


def test_predict_endpoint(client):
    response = client.post('/predict', json={'plot_size': "100"})
    assert response.status_code == 200
    assert response.json['predicted_price'] is not None


def test_invalid_json(client):
    response = client.post('/predict', json={})
    assert response.status_code == 400


def test_missing_plot_size(client):
    response = client.post('/predict', json={'foo': 'bar'})
    assert response.status_code == 400


def test_invalid_method(client):
    response = client.get('/predict')
    assert response.status_code == 405


if __name__ == '__main__':
    pytest.main()
