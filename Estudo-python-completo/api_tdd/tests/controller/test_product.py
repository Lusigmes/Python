from tests.factories import product_data
from fastapi import status


async def test_controller_create_should_return_success(client, products_url):
    response = await client.post(products_url, json=product_data())

    content = response.json()
    del content["created_at"]
    del content["updated_at"]
    del content["id"]
    assert response.status_code == status.HTTP_201_CREATED
    assert content == {
        "name": "Notebook",
        "quantity": 4,
        "valor": "5842.30",
        "status": True,
    }


async def test_controller_get_should_return_success(
    client, product_inserted, products_url
):
    response = await client.get(f"{products_url}{product_inserted.id}")

    content = response.json()
    del content["created_at"]
    del content["updated_at"]
    del content["id"]

    assert response.status_code == status.HTTP_200_OK
    assert content == {
        "id": str(product_inserted.id),
        "name": "Notebook",
        "quantity": 4,
        "valor": "5842.30",
        "status": True,
    }
