"""Dessert classes."""


class Cupcake:
    """A cupcake."""
    cache = {}


    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'
    

    def __init__(self, name, flavor, price):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0
        self.cache[name] = self
    
    def add_stock(self, amount):
        self.qty += amount
    
    def sell(self, amount):  
        if self.qty == 0:
            print("Sorry, these cupcakes are sold out")
        elif self.qty >= amount:  
            self.qty = self.qty - amount
        else:
            if self.qty < amount:
                self.qty = 0
                    
    @staticmethod
    def scale_recipe(ingredients, amount):
        output_list = []
        for ingredient_name, ingredient_qty in ingredients:
            ingredient_qty = ingredient_qty * amount
            output_list.append((ingredient_name , ingredient_qty))
        return output_list

        # Another method of doing this
        # return [(ingredient, qty * amount)
        #         for ingredient, qty in ingredients]

        

    @classmethod
    def get(cls, name):
        if name in cls.cache:
            return cls.cache[name]
        else:
            print("Sorry, that cupcake doesn't exist")
        # return cls.cache.get(name, 

class Brownie(Cupcake):

    def __init__(self, name, flavor, price):
        super.__init__(self, name, 'chocolate', price)


    

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
