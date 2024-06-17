from typing import List
from uuid import UUID
import pytest
from store.usecases.product import product_usecase

# from tests.conftests import product_in
from store.schemas.product import ProductOut, ProductUpdateOut
from store.core.exceptions import NotFoundException


# breakpoint()
async def test_usecases_create_should_return_success(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Notebook"


async def test_usecases_get_should_return_success(product_id):
    result = await product_usecase.get(id=product_id)

    assert isinstance(result, ProductOut)
    assert result.name == "Notebook"


async def test_usecases_get_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=UUID("6f123456-18ba-45f5-1234-333e222a111c"))
        # err.value.args[0]
    assert (
        err.value.message
        == "Product not found with ID: 6f123456-18ba-45f5-1234-333e222a111c"
    )


async def test_usecases_query_should_return_success():
    result = await product_usecase.query()

    assert isinstance(result, List)


async def test_usecases_update_should_return_success(product_id, product_upd):
    product_upd.valor = 4.000
    result = await product_usecase.update(id=product_id, body=product_upd)

    assert isinstance(result, ProductUpdateOut)
