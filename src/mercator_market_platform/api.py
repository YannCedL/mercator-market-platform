from fastapi import FastAPI
from genesis_core import ResultContract
from .engine import market_full_report

app = FastAPI(title="Mercator Market Platform API", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Mercator"}

@app.get("/api/v1/market/{siren}", response_model=ResultContract)
def market_report(siren: str):
    return market_full_report(siren)
