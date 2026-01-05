from pydantic import BaseModel, Field
from typing import Optional

class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Quantity (must be greater than 0)")

class CartItemCreate(CartItemBase):
    pass


class CartItemUpdate(CartItemBase):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0,
                          description="Quantity (must be greater than 0)")

class CartItem(BaseModel):
    product_id: int = Field(..., description="The unique ID of the product")
    name: str = Field(..., description="Name of the product added to cart")
    price: float = Field(..., description="Price per unit of the product")
    quantity: int = Field(..., gt=0, description="Number of items in the cart")
    subtotal: float = Field(...,
                            description="Total price for this item (price * quantity)")
    image_url: Optional[str] = Field(None, description="Link to the product image")

class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description="List of items in cart")
    total: float = Field(..., description="Total cart price")
    items_count: int = Field(..., description="Total number of items in cart")

class Config:
    from_attributes = True