import gc

class Node():
    def __init__(self,name):
        self.name = name
        self.next = None
    def __del__(self):
        print(f"{self.name} is deleted")

a = Node("A")
b = Node("B")

a.next = b
b.next = a

print('Collecting garbage...')
gc.collect()