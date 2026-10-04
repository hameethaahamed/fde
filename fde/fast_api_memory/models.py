from pydantic import BaseModel


class Invoice(BaseModel):
    id: int
    amount: float
    customer: str