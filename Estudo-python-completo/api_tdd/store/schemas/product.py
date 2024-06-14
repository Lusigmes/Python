from pydantic import Field
from store.schemas.base import BaseSchemaMixin


class ProductIn(BaseSchemaMixin):  # id nome quantidade preço status
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    valor: float = Field(..., description="Product valor")
    status: bool = Field(..., description="Product status")
