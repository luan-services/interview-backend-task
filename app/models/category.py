from sqlmodel import SQLModel, Field, Relationship
from typing import List, TYPE_CHECKING

# https://fastapi.tiangolo.com/tutorial/sql-databases/#update-the-app-with-multiple-models
# https://github.com/fastapi/full-stack-fastapi-template/blob/master/backend/app/models.py

if TYPE_CHECKING:
    from .product import Product

# SQLModel defines this class as a data model (like an interface in Javascript), and table=True ensures this is ALSO a table model to be created on the database
class Category(SQLModel, table=True):
    # setting default=None here lets the user set a custom id when creating a category (like 5442), or sending it as None, when doing
    # so, postgre database will automatically create an id for it before saving, since it is a primary_key and cannot be None.
    id: int | None = Field(default=None, primary_key=True)
    name: str
    # we must set the relationship here, this does not create a table, it only works as a helper if you want to do category.products
    products: List["Product"] = Relationship(back_populates="category", cascade_delete=True)