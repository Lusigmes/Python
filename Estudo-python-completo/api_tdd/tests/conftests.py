import asyncio
import pytest
from store.db.mongo import db_client
from store.schemas.product import ProductIn, ProductUpdate
from tests.factories import product_data
from uuid import UUID
from store.usecases.product import product_usecase
from httpx import AsyncClient


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mongo_client():
    return db_client.get()


@pytest.fixture(autouse=True)
async def clear_collections(mongo_client):
    yield
    collections_names = await mongo_client.get_database().list_collections_names()
    for collection in collections_names:
        if collection.startswith("system"):
            continue

        await mongo_client.get_database()[collection].delete_many({})


@pytest.fixture
async def client() -> AsyncClient:  # type: ignore
    from store.main import app

    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def products_url() -> str:
    return "/products/"


@pytest.fixture
def product_id() -> UUID:
    return UUID("6f829372-18ba-45f5-9640-340e272af81c")


@pytest.fixture
def product_in(product_id):
    return ProductIn(
        id=product_id, name="Notebook", quantity=4, valor=5842.30, status=True
    )


@pytest.fixture
def product_upd(product_id):
    return ProductUpdate(**product_data(), id=product_id)


@pytest.fixture
async def product_inserted(product_in):
    return await product_usecase.create(body=product_in)


@pytest.fixture
async def products_ins():
    return [ProductIn(**product) for product in product_data()]


@pytest.fixture
async def products_inserteds(products_ins):
    return [
        await product_usecase.create(body=product_in) for product_in in products_ins
    ]
