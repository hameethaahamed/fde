from fastapi import APIRouter
from data_store import invoices


router = APIRouter()


@router.get("/invoices")
def get_invoices():
    return invoices


@router.delete("/invoices/{invoice_id}")
def delete_invoice(invoice_id: int):
    for i, invoice in enumerate(invoices):
        if invoice["id"] == invoice_id:
            del invoices[i]
            return {"message": "Invoice deleted successfully"}
    return {"error": "Invoice not found"}