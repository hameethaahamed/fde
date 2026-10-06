import importlib
from fastapi import FastAPI


get_invoices = importlib.import_module("get_invoices").router
get_invoiceby_id = importlib.import_module("get_invoicebyid").router
create_invoice = importlib.import_module("create_invoice").router
delete_invoice = importlib.import_module("delete_invoice").router

app = FastAPI()


app.include_router(get_invoices)
app.include_router(get_invoiceby_id)
app.include_router(create_invoice)
app.include_router(delete_invoice)