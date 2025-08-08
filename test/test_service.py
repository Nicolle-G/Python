import pytest
from proyecto.service import app

@pytest.mark.asyncio
async def test_check_palindrome():
    test_client = app.test_client() 
    person = await test_client.post('/palindrome', json={"word": "oño"})
    data = await person.get_json()

    assert data == {
        "word": "oño",
        "is_palindrome": True
    }   