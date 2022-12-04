import pytest

from main import app

# Создаем фикстуру
@pytest.fixture()
def client():
    return app.test_client()


@pytest.fixture()
def post_keys():
    return {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count',
            'likes_count', 'pk', 'short'}


def test_api_posts(client, post_keys):
    response = client.get('/api/posts/')
#  проверка статуса
    assert response.status_code == 200
    assert isinstance(response.json, list)

#  возвращается словарь и проверяет, что у элемента есть нужные ключи
    for parameter in response.json:
        assert isinstance(parameter, dict)
        assert set(parameter.keys()) == post_keys


def test_api_post(client, post_keys):
    response = client.get('/api/posts/1/')
#  проверка статуса
    assert response.status_code == 200

#  возвращается словарь
    assert isinstance(response.json, dict)

#  у элемента есть нужные ключи
    assert set(response.json.keys()) == post_keys


