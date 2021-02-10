# Doubly linked chain
# Is linked by self.next, self.prev and so on, like the binairy search tree
import types


class Node:
    def __init__(self, data):
        self.index = None
        self.data = data
        self.prev = None
        self.next = None

    def insert(self, index, data):

        if isinstance(self, DummyNode):
            return [2, False]

        elif self.index == index - 1 and isinstance(self.next, DummyNode):
            newNode = Node(data)
            newNode.index = index
            newNode.next = self.next
            newNode.prev = self
            self.next.prev = newNode
            self.next = newNode
            return [1, True]


        elif self.index == index:
            newNode = Node(data)
            newNode.index = self.index
            self.indexPlusOne()
            newNode.prev = self.prev
            self.prev.next = newNode
            newNode.next = self
            self.prev = newNode
            return [0, True]


        elif self.index < index:
            if isinstance(self.next, DummyNode) is False:
                returnValue = self.next.insert(index, data)
                return returnValue

        elif self.index > index:
            if isinstance(self.prev.prev, DummyNode) is False:
                returnValue = self.prev.prev.insert(index, data)
                return returnValue

        else:
            return [2, False]

    def indexPlusOne(self):

        if isinstance(self, DummyNode) is False:
            self.index = self.index + 1
            if isinstance(self.next, DummyNode) is False:
                self.next.indexPlusOne()

    def indexMinusOne(self):
        if isinstance(self, DummyNode) is False:
            self.index = self.index - 1
            if isinstance(self.next, DummyNode) is False:
                self.next.indexMinusOne()

    def delete(self):
        self.indexMinusOne()
        self.prev.next = self.next
        self.next.prev = self.prev



    def deleteFind(self, index):
        if isinstance(self, DummyNode):
            return False

        elif self.index == index:

            # item = self.data # Item can be returned but it's return was not in the ADT
            self.delete()
            return True


        elif self.index < index:
            if isinstance(self.next, DummyNode) is False:
                returnValue = self.next.deleteFind(index)
                return returnValue



        else:
            return False

    def emptyChain(self):


        if isinstance(self, DummyNode) is False:

            # item = self.data # Item can be returned but it's return was not in the ADT
            self.delete()



        if isinstance(self.next, DummyNode) is False:
            self.next.emptyChain()






class DummyNode:
    def __init__(self):
        self.index = 0
        self.next = None
        self.prev = None



class LinkedChain:
    def __init__(self):
        self.front = DummyNode()
        self.back = self.front
        self.back.next = self.front
        self.front.prev = self.back
        self.back.prev = self.front
        # self.back.next = self.front
        # self.front.prev = self.back

    def createList(self):
        self.front = DummyNode()  # Will never be changed = The dummy head node
        self.back = self.front
        self.front.index = 0
        self.back.next = self.front
        self.front.prev = self.back
        self.back.prev = self.front
        return True



    def destroyList(self):
        del self
        return True



    def isEmpty(self) -> bool:  # Checks if the chain is empty
        if isinstance(self.front.next, DummyNode):  # If the front is empty than the chain is empty
            return True
        else:
            return False



    def getLength(self) -> int:  # Will count to an int
        count = 0
        countNode = self.front

        if self.front.next is not None:

            while countNode != self.back:  # While we are not at the end of the chain, keep on counting
                count += 1
                countNode = self.front.next


        return count


    def delete(self, index) -> bool:

        if index != 0 and self.retrieve(index)[1] is True:

           if self.front.next is not None:  # If we have no nodes, can't delete anything

               returnValue = self.front.next.deleteFind(index)

               return returnValue


        return False

    def retrieve(self, index) -> tuple:

        if self.front.next is not None:
            curr = self.front.next

            while isinstance(curr.next, DummyNode) is False:

                if curr.index == index:
                    return [curr.data, True]

                curr = curr.next

            if curr.index == index:
                return [curr.data, True]
            else:
                return [index, False]

        else:
            return [index, False]


    def insert(self, index, data) -> bool:

        if isinstance(self.front.next, DummyNode) is True and index == 1:
            self.front.next = Node(data)
            self.back = self.front.next
            self.front.next.prev = self.front
            self.front.next.next = self.front
            self.front.next.index = self.front.index + 1
            self.front.prev = self.front.next
            return True


        elif isinstance(self.front.next, DummyNode) is False:
            returnResult = self.front.next.insert(index, data)

            if returnResult[0] == 1:
                # Code for when self.back needs to be linked to a new node (we inserted at the back of the chain)
                curr = self.front

                if isinstance(self.front.next, DummyNode) is False:
                    curr = self.front.next
                    while isinstance(curr.next, DummyNode) is False:
                        curr = curr.next

                self.back = curr

            return returnResult[1]


        else:
            return False

    def save(self) -> print:

        output = []

        if self.front.next is not None:
            curr = self.front.next

            output.append(self.front.next.data)

            while isinstance(curr.next, DummyNode) is False:
                curr = curr.next
                output.append(curr.data)

        return output


    def load(self, list) -> bool:

        if self.front.next is not None:  # Making the tree empty
            self.front.next.emptyChain()
            self.back = self.front

        for dataElements in list:
            self.insert(list.index(dataElements) + 1, dataElements)


if __name__ == "__main__":
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