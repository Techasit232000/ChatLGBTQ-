from app import app


def test_index_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'ChatLGBTQ+' in response.data


def test_chat_endpoint():
    client = app.test_client()
    response = client.post('/api/chat', json={'message': 'Hello'})
    assert response.status_code == 200
    assert response.get_json()['response']


def test_chat_rejects_empty_message():
    client = app.test_client()
    response = client.post('/api/chat', json={'message': ' '})
    assert response.status_code == 400
