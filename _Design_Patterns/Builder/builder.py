class Product():
    def __init__(self):
        self.components = {}

    def add(self, key: str, value: str):
        self.components[key] = value

    def show(self):
        for key, value in self.components.items():
            print(value, end = " ")

class ProductBuilder:
    def __init__(self):
        self._parts = Product()
        
    def add_part(self, key: str, value: str):
        self._parts.add(key, value)

    def build(self) -> Product:
        product = self._parts
        self._parts = Product()
        return product

if __name__ == '__main__':
    builder = ProductBuilder()
    builder.add_part("1","Siulek")
    builder.add_part("2","został")
    builder.add_part("3","wzorcem")
    builder.add_part("4","projektowym")
    builder.add_part("5",'"Builder"')

    siulek = builder.build()
    siulek.show()
