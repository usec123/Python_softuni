class Catalogue:
    products = []
    def __init__(self,name):
        self.name = name
    
    def add_product(self,product):
        self.products.append(product)
    
    def get_by_letter(self,first_letter):
        return [item for item in self.products if item[0] == first_letter]
    
    def __repr__(self):
        list_of_products = '\n'.join(sorted(self.products))
        return f'Items in the {self.name} catalogue:\n{list_of_products}'

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)