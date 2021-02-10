# Doubly linked chain
# Using an ADT list


class LinkedChain:
    def __init__(self):
        self.list = []


    def createList(self) -> bool:  # Will create a list
        self.list = []
        return True

    def destroyList(self) -> bool:  # Will make a list None (so delete it)
        self.list = None
        return True

    def isEmpty(self) -> bool: # Will check if a list is empty
        if self.list is not None:
            if len(self.list) > 0:
                return True
            else:
                return False
        else:
            return False

    def getLength(self) -> int:  # Will get the length of a list
        if self.list is not None:
            length = len(self.list)
            return length
        else:
            return 0

    def retrieve(self, index) -> tuple:  # Will retrieve an index from the list

        try:
            save = self.list.at(index)
        except:
            return [index, False]
        return [save, True]


    def delete(self, index) -> bool:  # Will delete an item from the list

        try:
            self.list.pop(index)
            return True
        except:
            return False



    def insert(self, index, data) -> bool:  # Will insert an item into the list
        if len(self.list) >= index - 1:
            self.list.insert(index, data)
            return True
        else:
            return False

    def load(self, readList):  # Will load a list
        self.list = readList
        return True

    def save(self):  # will save a list
        return self.list

l = LinkedChain()
print(l.isEmpty())
print(l.getLength())
print(l.retrieve(4)[1])
print(l.insert(4,500))
print(l.isEmpty())
print(l.insert(1,500))
print(l.retrieve(1)[0])
print(l.retrieve(1)[1])
print(l.save())
print(l.insert(1,600))
print(l.save())
l.load([10,-9,15])
l.insert(3,20)
print(l.delete(0))
print(l.save())
print(l.delete(1))
print(l.save())