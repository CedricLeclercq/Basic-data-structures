class Node:  # Constructor: Node
    def __init__(self, data):
        self.data = data
        self.after = None


class Queue:
    def __init__(self):  # Constructor: Queue
        self.top = None
        self.end = None

    def isEmpty(self) -> bool:  # Method: Check if stack is empty
        if self.top is None:
            return True
        else:
            return False


    def createQueue(self) -> bool:  # Create a new queue
        self.top = self.end = None
        return True

    def destroyQueue(self) -> bool:  # delete the queue
        del self
        return True

    def enqueue(self, data) -> bool:
        if not self.isEmpty():
            new_node = Node(data)


            def recursionEnqueue(self):
                if self.after is None:
                    self.after = new_node

                else:
                    recursionEnqueue(self.after)

            recursionEnqueue(self.top)

            return True




        else:
            self.top = Node(data)
            return True






    def dequeueTop(self):  # Method: Remove the first element in the queue
        self.top = self.top.after

        def recursionShift(self):
            self.top = self.top.after
            if self.top.after is not self.end:
                recursionShift(self.top.after)
            elif self.top.after is None:
                return True


    def dequeue(self) -> [int, bool]:  # Method: Remove a given element form the queue
        if self.top is None:  # Base model for recursion later
            return [None, False]
            # print("Can't remove what's not there!")
            # print("(This stack is empty, it doesn't have a first element.)")
        else:
            save = self.top.keyAndData
            self.dequeueTop()
            return [save, True]

    def getFront(self) -> [int, bool]:  # Method: Returns the first element of the queue
        if self.top is None:
            return [None, False]
        else:
            return [self.top.keyAndData, True]


    def load(self, list) -> bool:
        def saveDeleteRecursion(self):
            if self.top is not None:
                self.dequeue()
                saveDeleteRecursion(self)

        saveDeleteRecursion(self)

        for i in reversed(list):
            self.enqueue(i)


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

q = Queue()
print(q.isEmpty())
print(q.getFront()[1])
print(q.dequeue()[1])
print(q.enqueue(2))
print(q.enqueue(4))
print(q.isEmpty())
print(q.dequeue()[0])
q.enqueue(5)
print(q.save())

q.load(['a', 'b', 'c'])
print(q.save())
print(q.dequeue()[0])
print(q.save())
print(q.getFront()[0])
print(q.save())
















