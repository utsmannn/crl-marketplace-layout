from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from layout_services import render_product_list, render_single_product

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/home")
def product_list():
    return render_product_list()

@app.get("/product/{product_id}")
def product_detail(product_id: int):
    return render_single_product(product_id)