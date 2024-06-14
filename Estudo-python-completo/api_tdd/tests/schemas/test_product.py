from store.schemas.product import ProductIn
from uuid import UUID
import pytest
from pydantic import ValidationError
from tests.factories import product_data, product_data_raise


def test_schemas_validated():
    data = product_data()
    product = ProductIn(**data)

    assert product.name == "Notebook"
    assert isinstance(product.id, UUID)


def test_schemas_return_raise():
    data = product_data_raise()

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    # breakpoint() #  usar err.value.errors()
    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Notebook", "quantity": 4, "valor": 5842.3},
        "url": "https://errors.pydantic.dev/2.7/v/missing",
    }
