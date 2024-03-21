# When to use class methods and when to use static methods ?

class Item:
    @staticmethod
    def is_integer():
        '''
        Cela devrait faire quelque chose qui a une relation
        avec la classe, mais pas quelque chose qui doit être unique
        par exemple !
        '''
    @classmethod
    def instantiate_from_something(cls):
        '''
        Cela devrait également faire quelque chose qui a une relation
        avec la classe, mais généralement, ceux-ci sont habitués à
        manipuler différentes structures de données pour instancier
        objets, comme nous l'avons fait avec CSV.
        '''

# THE ONLY DIFFERENCE BETWEEN THOSE:
# Static methods are not passing the object reference as the first argument in the background!


# NOTE: However, those could be also called from instances.

item1 = Item()
item1.is_integer()
item1.instantiate_from_something()