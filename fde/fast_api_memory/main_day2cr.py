import importlib
from fastapi import FastAPI


get_invoices = importlib.import_module("01_get_invoices").router
create_invoice = importlib.import_module("01_post_invoices").router
delete_invoice = importlib.import_module("01_delete_invoicebyid").router
put_invoice = importlib.import_module("01_put_invoicebyid").router

app = FastAPI()
app.include_router(create_invoice)
app.include_router(get_invoices)
app.include_router(delete_invoice)
app.include_router(put_invoice)
