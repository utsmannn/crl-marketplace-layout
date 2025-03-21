from product_services import Product, fetch_products, fetch_product_id


def formatted_price(price):
    return f"Rp {int(price):,}".replace(",", ".")


def product_item(product: Product):
    click_id = f"navigate:/product/{product.id}"

    layout = {
        "column": {
            "modifier": {
                "base": {
                    "fillMaxWidth": True,
                    "shadow": {
                        "elevation": 4,
                        "shape": {
                            "type": "roundedcorner",
                            "cornerRadius": 6
                        }
                    },
                    "clickId": click_id
                }
            },
            "children": [
                {
                    "image": {
                        "modifier": {
                            "base": {
                                "fillMaxWidth": True,
                                "height": 120
                            }
                        },
                        "url": product.images
                    }
                },
                {
                    "box": {
                        "modifier": {
                            "base": {
                                "fillMaxWidth": True,
                                "background": {
                                    "color": "#ffff"
                                }
                            }
                        },
                        "children": [
                            {
                                "column": {
                                    "modifier": {
                                        "base": {
                                            "fillMaxWidth": True,
                                            "padding": {
                                                "all": 12
                                            }
                                        }
                                    },
                                    "children": [
                                        {
                                            "text": {
                                                "content": product.name,
                                                "fontSize": 16,
                                                "fontWeight": "bold",
                                                "maxLines": 2,
                                                "minLines": 2,
                                                "overflow": "ellipsis"
                                            }
                                        },
                                        {
                                            "spacer": {
                                                "height": 12
                                            }
                                        },
                                        {
                                            "text": {
                                                "content": formatted_price(product.price)
                                            }
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }

    return layout


def product_item_row(product: Product):
    click_id = f"navigate:/product/{product.id}"

    layout = {
        "column": {
            "modifier": {
                "base": {
                    "width": 200,
                    "shadow": {
                        "elevation": 4,
                        "shape": {
                            "type": "roundedcorner",
                            "cornerRadius": 6
                        }
                    },
                    "clickId": click_id
                }
            },
            "children": [
                {
                    "image": {
                        "modifier": {
                            "base": {
                                "fillMaxWidth": True,
                                "height": 100
                            }
                        },
                        "url": product.images
                    }
                },
                {
                    "box": {
                        "modifier": {
                            "base": {
                                "fillMaxWidth": True,
                                "background": {
                                    "color": "#ffff"
                                }
                            }
                        },
                        "children": [
                            {
                                "column": {
                                    "modifier": {
                                        "base": {
                                            "fillMaxWidth": True,
                                            "padding": {
                                                "all": 12
                                            }
                                        }
                                    },
                                    "children": [
                                        {
                                            "text": {
                                                "content": product.name,
                                                "fontSize": 16,
                                                "fontWeight": "bold",
                                                "maxLines": 2,
                                                "minLines": 2,
                                                "overflow": "ellipsis"
                                            }
                                        },
                                        {
                                            "spacer": {
                                                "height": 12
                                            }
                                        },
                                        {
                                            "text": {
                                                "content": formatted_price(product.price)
                                            }
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }

    return layout


def render_product_list():
    product_response = fetch_products()
    product_items = [product_item(product) for product in product_response.data]
    product_row_items = [product_item_row(product) for product in product_response.data]

    layout = {
        "column": {
            "modifier": {
                "base": {
                    "fillMaxWidth": True,
                    "scrollable": True
                }
            },
            "children": [
                # Header
                {
                    "spacer": {
                        "height": 12
                    }
                },
                {
                    "text": {
                        "modifier": {
                            "base": {
                                "padding": {
                                    "horizontal": 12
                                }
                            }
                        },
                        "content": "For You",
                        "fontSize": 20,
                        "fontWeight": "bold"
                    }
                },
                {
                    "spacer": {
                        "height": 12
                    }
                },
                {
                    "grid": {
                        "modifier": {
                            "base": {
                                "fillMaxWidth": True,
                                "scrollable": True,
                                "padding": {
                                    "all": 12
                                },
                            },
                            "rows": 2,
                            "orientation": "horizontal",
                            "horizontalArrangement": 12,
                            "verticalArrangement": 12
                        },
                        "children": [
                            *product_row_items[:10]
                        ]
                    }
                },
                {
                    "spacer": {
                        "height": 6
                    }
                },
                {
                    "text": {
                        "modifier": {
                            "base": {
                                "padding": {
                                    "horizontal": 12
                                }
                            }
                        },
                        "content": "All Products",
                        "fontSize": 20,
                        "fontWeight": "bold"
                    }
                },
                {
                    "spacer": {
                        "height": 6
                    }
                },
                {
                    "grid": {
                        "modifier": {
                            "base": {
                                "fillMaxWidth": True,
                                "scrollable": True,
                                "padding": {
                                    "all": 12
                                },
                            },
                            "columns": 2,
                            "orientation": "vertical",
                            "horizontalArrangement": 12,
                            "verticalArrangement": 12
                        },
                        "children": [
                            *product_items
                        ]
                    }
                }
            ]
        }
    }

    return layout


def render_single_product(id):
    single_product = fetch_product_id(id).data

    layout = {
        "column": {
            "modifier": {
                "base": {
                    "fillMaxWidth": True,
                    "scrollable": True,
                }
            },
            "children": [
                {
                    "image": {
                        "modifier": {
                            "base": {
                                "fillMaxWidth": True,
                                "height": 300
                            }
                        },
                        "url": single_product.images[0]
                    }
                },
                {
                    "column": {
                        "modifier": {
                            "base": {
                                "margin": {
                                    "all": 12
                                }
                            }
                        },
                        "children": [
                            {
                                "text": {
                                    "content": single_product.name,
                                    "fontSize": 18,
                                    "fontWeight": "bold"
                                }
                            },
                            {
                                "spacer": {
                                    "height": 10
                                }
                            },
                            {
                                "text": {
                                    "content": formatted_price(single_product.price)
                                }
                            },
                            {
                                "spacer": {
                                    "height": 10
                                }
                            },
                            {
                                "text": {
                                    "content": single_product.description
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }

    return layout
