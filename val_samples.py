from pydantic import BaseModel, ValidationError
from typing import Optional, Annotated
from annotated_types import Gt


class Sample(BaseModel):
    id: int
    firstname: str
    lastname: str
    age: Optional[int] = 0

sample1 = Sample(id=1, firstname='ahmet', lastname='g', age=20)

print(sample1)

###
data2 = {"id":1, "firstname":"mehmet", "lastname":"s"}

sample2 = Sample(**data2)

print(sample2)

###
data3 = {"id":"str", "firstname":"asd", "lastname":"fgh"}

try:
    Sample(**data3)
except ValidationError as e:
    print(e.errors())

###
class Product(BaseModel):
    name: str
    price: Annotated[int, Gt(10)]

product1 = Product(name="bilgisayar", price=20)

print(product1)