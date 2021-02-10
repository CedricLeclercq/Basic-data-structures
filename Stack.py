"""
Comment for lines -> [19,25,35,45,58]:
Could have used isEmpty, preferred writing it again myself for visibility. Easily changeable if needed.
"""

# TODO 1: Fix popItem
# TODO 2: Test if other functions work

class Node:  # Constructor: Node
    def __init__(self, data):
        self.data = data
        self.after = None


class Stack:
    def __init__(self):  # Constructor: Stack
        self.top = None

    def isEmpty(self) -> bool:  # Method: Check if stack is empty
        if self.top is None:
            return True
        else:
            return False

    def push(self, data) -> bool:  # Method: Push an element at the first position of the stack
        if self.top is None:
            self.top = Node(data)
            return True
        else:
            # NOTE: these three lines are inspired from https://www.geeksforgeeks.org/implement-a-stack-using-singly-linked-list/
            # The rest, so except these three lines, has been made my me.
            # This note also applies for the Stack, but I already submitted that to ING.
            new_node = Node(data)  # Creating a new node with the constructor
            new_node.after = self.top  # Placing data on the first place in the queue
            self.top = new_node  # Placing what was the first element on the next node (following the LIFO principal)
            return True

    def popTop(self):  # Method: Remove the first element in the stack
        self.top = self.top.after

        def recursionShift(self):
            self.top = self.top.after
            if self.top.after is not None:
                recursionShift(self.top.after)
            elif self.top.after is None:
                return True


    def pop(self) -> [int, bool]:  # Method: Remove a given element form the stack
        if self.top is None:  # Base model for recursion later
            return [None, False]
            # print("Can't remove what's not there!")
            # print("(This stack is empty, it doesn't have a first element.)")
        else:
            save = self.top.keyAndData
            self.popTop()
            return [save, True]



    def getTop(self) -> [bool, int]:  # Method: Returns the first element of the stack
        if self.top is None:
            return [None, False]
        else:
            return [self.top.keyAndData, True]

    def load(self, list) -> bool:

        def saveDeleteRecursion(self):
            if self.top is not None:
                self.popTop()
                saveDeleteRecursion(self)

        saveDeleteRecursion(self)

        for i in list:
            self.push(i)

    def save(self) -> list:

        outputList = []

        def saveRecursion(self):
            if self is not None:
                outputList.append(self.keyAndData)
                saveRecursion(self.after)


        saveRecursion(self.top)
        return outputList[::-1]  # IMPORTANT NOTE: my stack represents its number with the top to the right, contrary to the left in ING.
        # I used this trick to get the correct output for the print of the stack on ING,
        # this depends on the way that one would create their print function their stack.


    def display(self) -> None:
        iterNode = self.top
        if self.isEmpty():
            print("Stack overflow")

        else:
            while iterNode is not None:
                print(iterNode.keyAndData, "->", end=" ")
                iterNode = iterNode.after

            return 0


s = Stack()

"""
print(s.isEmpty())
print(s.getTop()[1])
print(s.pop()[1])
print(s.push(2))
print(s.push(4))
print(s.isEmpty())
print(s.pop()[0])
s.push(5)
# print(s.save())
"""

s.load(['a','b','c'])
print(s.save())
print(s.pop()[0])
print(s.save())
print(s.getTop()[0])
print(s.save())



"""
stack = Stack()

stack.push(11)
stack.push(12)
stack.push(34)
stack.push(45)
stack.push(3)
stack.pop()

stack.pop()
print(stack.getTop())
stack.display()
"""