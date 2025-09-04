from typing import Annotated

from fastapi import Depends, Query
from pydantic import BaseModel, Field

hotels = [
    {"id": 1, "title": "Sochi", "name": "sochi"},
    {"id": 2, "title": "Дубай", "name": "dubai"},
    {"id": 3, "title": "Мальдивы", "name": "maldivi"},
    {"id": 4, "title": "Геленджик", "name": "gelendzhik"},
    {"id": 5, "title": "Москва", "name": "moscow"},
    {"id": 6, "title": "Казань", "name": "kazan"},
    {"id": 7, "title": "Санкт-Петербург", "name": "spb"},
]

class PaginationParams(BaseModel):
    page: Annotated[int | None, Query(None, ge=1, description="Номер страницы")]
    per_page: Annotated[int | None, Query(None, ge=1, le=len(hotels), description="Количество отелей на странице",)]

PaginationDep = Annotated[PaginationParams, Depends()]
