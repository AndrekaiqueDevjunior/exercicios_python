from pydantic import BaseModel


class VendaCreate(BaseModel):
    cliente: str
    valor: float