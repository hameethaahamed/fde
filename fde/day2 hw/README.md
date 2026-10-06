# Day 2 Invoice API

A small FastAPI application for reading, creating, and deleting invoice records.
Invoice data is stored in `data/invoices.json`.

## Requirements

- Python 3.10 or later
- The packages listed in `..\requirements.txt` (`fastapi` and `uvicorn`)

From this folder, install the dependencies with:

```powershell
python -m pip install -r ..\requirements.txt
```

## Run the API

Run these commands from the `day2 hw` folder:

```powershell
python -m uvicorn main:app --reload
```

By default, the server is available at `http://127.0.0.1:8000`.

## Swagger and API documentation

With the server running, open:

- Swagger UI: <http://127.0.0.1:8000/docs>
- ReDoc: <http://127.0.0.1:8000/redoc>
- OpenAPI schema: <http://127.0.0.1:8000/openapi.json>

Swagger UI lets you expand an operation, select **Try it out**, enter any
required path or JSON body, and select **Execute**.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/invoices` | Return all invoices. |
| `GET` | `/invoices/{invoice_id}` | Return the invoice matching its ID. |
| `POST` | `/invoices` | Add an invoice to the JSON file. |
| `DELETE` | `/invoices/{invoice_id}` | Delete the invoice matching its ID. |

Invoice IDs are strings, for example `INV-101`.

### Create an invoice

Send `POST /invoices` with a JSON body containing all fields:

```json
{
  "invoice_id": "INV-103",
  "vendor": "Example Supplies",
  "amount": 125000.0,
  "status": "PENDING"
}
```

The `amount` field must be a number. The endpoint appends the invoice to
`data/invoices.json`.

### Example responses

`GET /invoices/INV-101` returns the matching record:

```json
{
  "invoice_id": "INV-101",
  "vendor": "ABC Ltd",
  "amount": 85000,
  "status": "PENDING"
}
```

The GET and DELETE handlers return a JSON message if the requested invoice ID
is not found.
