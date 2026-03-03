class HashTable:
    
    def __init__(self):
        self.collection = {}
    def hash(self,data):
        result = 0
        for i in data:
            result += ord(i)
        return result
    def add(self,key,value):
        h_value = self.hash(key)
        if h_value not in self.collection:
            self.collection[h_value] = {}
        self.collection[h_value][key] = value
    def remove(self,key):
        h_value = self.hash(key)
        if h_value in self.collection and key in self.collection[h_value]:
            del self.collection[h_value][key]
    def lookup(self,key):
        h_value = self.hash(key)
        if h_value in self.collection and key in self.collection[h_value]:
            return self.collection[h_value][key]
        return None

h = HashTable()
print(h.hash('golf'))
h.add('golf', 'sport')
h.add('dear', 'friend')
h.add('read', 'book')

print(h.lookup('golf'))
print(h.lookup('cfc'))
print(h.collection)