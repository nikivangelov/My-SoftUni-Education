class Catalogue:
    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, product_name: str):
        Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        new_list = list(x for x in Catalogue.products if str(x).startswith(first_letter))
        return new_list

    def __repr__(self):
        Catalogue.products.sort()
        return f"Items in the {self.name} catalogue:\n" + \
               '\n'.join(Catalogue.products)



catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
