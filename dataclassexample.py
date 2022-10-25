from dataclasses import dataclass
from tokenize import String

@dataclass
class Product:
    nombre: String
    precio: float

@dataclass
class Cart:
    products: list[Product]

    def totalCart(self):
        return sum(product.precio for product in self.products)

cart= Cart([Product("papa",2), Product("cebolla",3)])
print(cart.totalCart())