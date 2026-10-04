import importlib
from fastapi import FastAPI


get_invoices = importlib.import_module("01_get_invoices").router
create_invoice = importlib.import_module("01_post_invoices").router


app = FastAPI()
app.include_router(create_invoice)
app.include_router(get_invoices)
