class category:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.products = []

class ProductHierarchy:
    def __init__(self):
        self.root = category("Amazon")
    
    def add_product(self, product_name, path):
        node = self.root
        for item in path:
            if item not in node.children:
                node.children[item] = category(item)
            node = node.children[item]
        node.products.append(product_name)
    
    def filter_products(self, path):
        node = self.root
        for item in path:
            if item in node.children:
                node = node.children[item]
            else:
                return []
        return self.get_products(node)
        
    def get_products(self, node):
        products = list(node.products)
        for child in node.children.values():
            products.extend(self.get_products(child))
        return products

hierarchy = ProductHierarchy()

hierarchy.add_product("Coke", ["Grocery", "Drinks", "SoftDrinks"])
hierarchy.add_product("Apple Juice", ["Grocery", "Drinks", "Juice"])
hierarchy.add_product("PS5 Console", ["Electronics", "Video Games", "PSS"])
hierarchy.add_product("FIFA 2025", ["Electronics", "Video Games", "PSS", "Sports"])
hierarchy.add_product("Nike", ["Clothings", "Shoes", "Running Shoes"])
hierarchy.add_product("Toilet Paper", ["Household Goods", "Bathroom"])

all_drinks = hierarchy.filter_products(["Grocery", "Drinks"])
pss_sports_games = hierarchy.filter_products(["Electronics", "Video Games", "PSS", "Sports"])

print(all_drinks)  # ['Coke', 'Apple Juice']
print(pss_sports_games)  # ['FIFA 2025']