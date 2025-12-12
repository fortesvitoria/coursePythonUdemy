#when to use class methods and when to use static methods?

class Item:
    @staticmethod
    def is_integer():
        '''
        This should do something that has realitionship with the class, but not something that must be unique per instance
        '''