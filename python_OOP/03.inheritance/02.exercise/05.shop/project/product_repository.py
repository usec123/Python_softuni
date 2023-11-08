from .product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str):
        new_products = []
        for product in self.products:
            if product.name != product_name:
                new_products.append(product)
        self.products = new_products

    def __repr__(self):
        return '\n'.join([f'{product.name}: {product.quantity}' for product in self.products])
