from decimal import Decimal
from typing import Annotated, Optional
from bson import Decimal128
from pydantic import AfterValidator, BaseModel, Field
from store.schemas.base import BaseSchemaMixin, OutSchema


class ProductBase(BaseModel):  # id nome quantidade preço status
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    valor: Decimal = Field(..., description="Product valor")
    status: bool = Field(..., description="Product status")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn, OutSchema):
    ...


def convert_decimal128(valor):
    return Decimal128(str(valor))


Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal128)]


class ProductUpdate(BaseSchemaMixin):
    quantity: Optional[int] = Field(None, description="Product quantity")
    valor: Optional[Decimal_] = Field(None, description="Product valor")
    status: Optional[bool] = Field(None, description="Product status")


class ProductUpdateOut(ProductOut):
    ...
