import csv
import math
from pathlib import Path


csv_file = Path(__file__).with_name("homework_invoices.csv")
total_invoices = 0
high_amount_invoices = 0
invalid_amount_invoices = 0

with csv_file.open(mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for invoice in reader:
        total_invoices += 1
        vendor = invoice["vendor"].strip()
        amount_text = invoice["amount"].strip()
        status = invoice["status"].strip()

        try:
            if not amount_text:
                raise ValueError("amount is missing")

            amount = float(amount_text)
            if not math.isfinite(amount):
                raise ValueError("amount is not a finite number")
        except ValueError:
            invalid_amount_invoices += 1
            print(
                f"Vendor: {vendor or 'Missing'}, "
                f"Amount: {amount_text or 'Missing/invalid'}, "
                f"Status: {status}"
            )
            continue

        if amount > 100_000:
            high_amount_invoices += 1

        print(f"Vendor: {vendor or 'Missing'}, Amount: {amount}, Status: {status}")

print("\nInvoice Summary")
print(f"Total number of records: {total_invoices}")
print(f"Invoices greater than 100,000: {high_amount_invoices}")
print(f"Invoices with missing/invalid amount: {invalid_amount_invoices}")