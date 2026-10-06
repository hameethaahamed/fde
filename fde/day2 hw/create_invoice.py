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


@router.post("/invoices")
def create_invoice(invoice: Invoice):
    new_invoice = invoice.model_dump()
    invoices = load_invoices()
    invoices.append(new_invoice)
    save_invoices(invoices)
    return {"message": "Invoice created successfully", "invoice": new_invoice}