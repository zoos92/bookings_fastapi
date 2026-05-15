import pytest
from httpx import AsyncClient, ASGITransport

from main import app


@pytest.mark.asyncio
async def test_post_book():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url='http://test',
        ) as ac:
        resp = await ac.post('/books', 
                             json={'title': 'Nazvanie,',
                             'author': 'Author'})
        assert resp.status_code == 200
        data = resp.json()
        assert data == {'success': True, 'message': 'Book is created'}
        print(resp)
