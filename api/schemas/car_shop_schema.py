from typing import Optional

from pydantic import BaseModel

from api.schemas.mixins_schema import CreationBase, PaymentConfirmedBase


class CarShopBase(BaseModel):
    FK_UserID: Optional[int] = None


class NewItemCarShop(CarShopBase, CreationBase, PaymentConfirmedBase):
    FK_ProductID: Optional[int] = None

    class Config:
        orm_mode = True


class RemoveItemCarShop(NewItemCarShop):
    CarShopID: Optional[int] = None


class PaymentConfirmed(NewItemCarShop, PaymentConfirmedBase):
    pass
