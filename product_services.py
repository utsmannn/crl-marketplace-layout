from dataclasses import dataclass
from typing import List, Optional

import requests


@dataclass
class Category:
    id: int
    name: str
    description: str


@dataclass
class Review:
    user: str
    review: str


@dataclass
class Product:
    id: int
    name: str
    sort_description: str
    description: Optional[str] = None
    category: Optional[Category] = None
    price: float = 0.0
    rating: float = 0.0
    discount: int = 0
    images: Optional[List[str]] = None
    user_review: Optional[List[Review]] = None


@dataclass
class ApiResponse:
    status: bool
    message: str
    data: List[Product]


@dataclass
class SingleProductResponse:
    status: bool
    message: str
    data: Product


def parse_json_to_models(json_data):
    products = []

    for product_data in json_data.get('data', []):
        category_data = product_data.get('category', {})
        category = Category(
            id=category_data.get('id'),
            name=category_data.get('name'),
            description=category_data.get('description')
        )

        product = Product(
            id=product_data.get('id'),
            name=product_data.get('name'),
            sort_description=product_data.get('sort_description'),
            category=category,
            price=product_data.get('price'),
            rating=product_data.get('rating'),
            discount=product_data.get('discount'),
            images=product_data.get('images')
        )

        products.append(product)

    api_response = ApiResponse(
        status=json_data.get('status'),
        message=json_data.get('message'),
        data=products
    )

    return api_response


def parse_single_product(json_data):
    product_data = json_data.get('data', {})

    category_data = product_data.get('category', {})
    category = Category(
        id=category_data.get('id'),
        name=category_data.get('name'),
        description=category_data.get('description')
    )

    reviews = []
    for review_data in product_data.get('user_review', []):
        review = Review(
            user=review_data.get('user'),
            review=review_data.get('review')
        )
        reviews.append(review)

    product = Product(
        id=product_data.get('id'),
        name=product_data.get('name'),
        sort_description=product_data.get('sort_description', ''),
        description=product_data.get('description'),
        category=category,
        price=product_data.get('price'),
        rating=product_data.get('rating'),
        discount=product_data.get('discount'),
        images=product_data.get('images'),
        user_review=reviews
    )

    api_response = SingleProductResponse(
        status=json_data.get('status'),
        message=json_data.get('message'),
        data=product
    )

    return api_response


def fetch_products(page=1, page_size=20, category_id=None, query=None, sort=None, as_models=True):
    base_url = "https://marketfake.fly.dev/product"

    params = {
        'page': page,
        'pageSize': page_size
    }

    if category_id is not None:
        params['categoryId'] = category_id

    if query is not None:
        params['query'] = query

    if sort is not None:
        params['sort'] = sort

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        json_data = response.json()

        if as_models:
            return parse_json_to_models(json_data)
        else:
            return json_data
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None


def fetch_product_id(id, as_models=True):
    url = f"https://marketfake.fly.dev/product/{id}"

    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()

        if as_models:
            return parse_single_product(json_data)
        else:
            return json_data
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None