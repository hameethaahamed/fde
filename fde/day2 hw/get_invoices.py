import json
from pathlib import Path

from fastapi import APIRouter


router = APIRouter()


def load_invoices():
    invoices_file = Path(__file__).resolve().parent.parent / "data" / "invoices.json"
    with invoices_file.open(encoding="utf-8") as file:
        return json.load(file)


@router.get("/invoices")
def get_invoices():
    return load_invoices()