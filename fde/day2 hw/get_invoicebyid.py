import json
from pathlib import Path

from fastapi import APIRouter


router = APIRouter()


def load_invoices():
    invoices_file = Path(__file__).resolve().parent.parent / "data" / "invoices.json"
    with invoices_file.open(encoding="utf-8") as file:
        return json.load(file)


@router.get("/invoices/{invoice_id}")
def get_invoice_by_id(invoice_id: str):
    invoices = load_invoices()
    for invoice in invoices:
        if invoice["invoice_id"] == invoice_id:
            return invoice
    return {"error": "Invoice not found"}