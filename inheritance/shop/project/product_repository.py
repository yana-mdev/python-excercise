from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: list[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        product = next((product for product in self.products if product.name == product_name), None)
        return product

    def remove(self, product_name):
        self.products = [product for product in self.products if product.name != product_name]

    def __repr__(self):
        result = []
        for product in self.products:
            result.append(f"{product.name}: {product.quantity}")

        return "\n".join(result)