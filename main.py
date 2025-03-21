from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from layout_services import render_product_list, render_single_product

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/home")
def product_list():
    return render_product_list()

@app.get("/product/{product_id}")
def product_detail(product_id: int):
    return render_single_product(product_id)