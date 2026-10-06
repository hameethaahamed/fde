import json
from pathlib import Path

from fastapi import APIRouter
from models import Invoice


router = APIRouter()
INVOICES_FILE = Path(__file__).resolve().parent.parent / "data" / "invoices.json"


def load_invoices():
    with INVOICES_FILE.open(encoding="utf-8") as file:
        return json.load(file)


def save_invoices(invoices):
    with INVOICES_FILE.open("w", encoding="utf-8") as file:
        json.dump(invoices, file, indent=2)
        file.write("\n")


@router.delete("/invoices/{invoice_id}")
def delete_invoice(invoice_id: str):
    invoices = load_invoices()
    invoice_to_delete = next((invoice for invoice in invoices if invoice["invoice_id"] == invoice_id), None)
    if not invoice_to_delete:
        return {"message": "Invoice not found"}
    invoices.remove(invoice_to_delete)
    save_invoices(invoices)
    return {"message": "Invoice deleted successfully", "invoice": invoice_id}