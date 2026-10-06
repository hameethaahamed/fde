from fastapi import APIRouter
from data_store import invoices


router = APIRouter()


@router.get("/invoices")
def get_invoices():
    return invoices


@router.put("/invoices/{invoice_id}")
def update_invoice(invoice_id: int, updated_invoice: dict):
    for i, invoice in enumerate(invoices):
        if invoice["id"] == invoice_id:
            invoices[i] = {**invoice, **updated_invoice}
            return invoices[i]
    return {"error": "Invoice not found"}