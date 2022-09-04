from urllib import response

from app import app

def test():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_edit():
    response = app.test_client().get('/edit')
    assert response.status_code==200

def test_text():
    response = app.test_client().get('/edit')
    assert b"To Do App" in response.data
    assert b"Todo title" in response.data
    assert b"Bling" in response.data