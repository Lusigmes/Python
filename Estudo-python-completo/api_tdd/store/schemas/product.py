from typing import Optional
from pydantic import BaseModel, Field
from store.schemas.base import BaseSchemaMixin, OutSchema


class ProductModel(BaseModel):  # id nome quantidade preço status
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    valor: float = Field(..., description="Product valor")
    status: bool = Field(..., description="Product status")


class ProductIn(ProductModel, BaseSchemaMixin):
    ...


class ProductOut(ProductIn, OutSchema):
    ...


class ProductUpdate(ProductModel):
    quantity: Optional[int] = Field(None, description="Product quantity")
    valor: Optional[float] = Field(None, description="Product valor")
    status: Optional[bool] = Field(None, description="Product status")


class ProductUpdateOut(ProductUpdate):
    ...
