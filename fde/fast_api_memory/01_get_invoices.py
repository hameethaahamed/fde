from fastapi import APIRouter
from data_store import invoices


router = APIRouter()


@router.get("/invoices")
def get_invoices():
    return invoices


@router.get("/customers")
def get_customers():
    return [invoice["customer"] for invoice in invoices]


@router.get("/invoices/{invoice_id}")
def get_invoice(invoice_id: int):
    for invoice in invoices:
        if invoice["id"] == invoice_id:
            return invoice
    return {"error": "Invoice not found"}


@router.get("/invoices{customer_name}")
def get_invoices_by_customer(customer_name: str):
    for invoice in invoices:
        if invoice["customer"] == customer_name:
            return invoice
    return {"error": "Invoice not found"}