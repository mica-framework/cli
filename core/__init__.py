class Singelton:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singelton, cls).__new__(cls)
        return cls.instance
    

class SessionStorage(Singelton):
    def __init__(self):
        self.storage = {}

    def store(self, key, value):
        self.storage[key] = value

    def remove(self, key):
        del self.storage[key]

    def clear(self):
        del(self.storage)
        self.storage = {}

    def get_value(self, key):
        if key not in self.storage.keys():
            return None
        return self.storage[key]
    
    def get_storage(self):
        return self.storage


#class AbstractModule:
#    def execute(self):
#        print("Abstract Module is used! The execute function was not implemented by the Child!")