# Binary search tree

class Node:  # Constructor for node
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def insert(self, newNode):  # Function to insert a node

        if self.key > newNode.key:  # If key of the new node is smaller than key of the current node (go to the subtree on the left)
            if self.left is None:
                self.left = newNode  # If left node is None, insert, else, recursive function
            else:
                self.left.insert(newNode)

        elif self.key < newNode.key:  # If key of the new node is greater than key of the current node (go to the subtree on the right)
            if self.right is None:
                self.right = newNode  # If right is None, insert, else, recursive function
            else:
                self.right.insert(newNode)

    def find(self, key) -> tuple:  # Function to find a node with a key
        if self.key == key:  # Base case to stop the recursion key is found
            if self is None:
                return [key, False]  # if node is None, return the key and False, key has not been found
            else:
                return [self.data, True]  # Else, return data of the node and True, key has been found
        elif self.key > key:
            if self.left is not None:
                self.left.find(key)  # Recursive function to the left side of the tree
            else:
                return [key, False]  # If left side is empty, then is the key not in the tree. Return key and False.
        elif self.key < key:
            if self.right is not None:
                self.right.find(key)  # Idem as line 31 (** in the right tree)
            else:
                return [key, False]  # Idem as line 34 (** in the right tree)

    def findSelf(self, key) -> object:  # Adjusted version of find, to return the object rather than a tuple with the data of the object
        # Same explanation as find(), just with other return
        if self.key == key:
            return self
        elif self.key > key:
            if self.left is not None:
                self.left.findSelf(key)
            else:
                return self
        elif self.key < key:
            if self.right is not None:
                self.right.findSelf(key)
            else:
                return self


    def delete(self, key):  # Function to delete a node given a key

        # One would notice that i didn't use self directly, but that I referred to self as self.right or self.left.
        # I did this so that the deletion of a node would be easier to do from its parent than from the node itself.

        if self.left is not None:  # If left subtree is not None
            if self.left.key == key:  # If key of left node is not None
                if self.left.left is None and self.left.right is None:  # If the node has no children
                    self.left = None  # Just delete the node
                else:
                    self.left.inorderTraverseSelf(False)  # Defined below
        if self.right is not None:  # Idem as left subtree
            if self.right.key == key:
                if self.right.left is None and self.right.right is None:
                    self.right = None
                else:
                    self.right.inorderTraverseSelf(False)

        if self.key > key:  # If our search key is smaller than the key of this node, search in the left tree
            if self.left is not None:
                self.left.delete(key)


        if self.key < key:  # If our search key is greater than the key of this node, search in the right tree
            if self.right is not None:
                self.right.delete(key)

        if self.key == key:  # If our search key equals the key of this node, delete with the function below
            self.inorderTraverseSelf(True)


    def inorderTraverseSelf(self, root):  # Gets the node with the wanted to delete key, for when the to delete node has children and ...
        # ... we need to switch nodes with a node more easy to delete

        # This function will search in the right subtree for the leftmost node
        # This node will be way easier to delete than a node somewhere in the tree

        temp = self.right  # searching in the right subtree (this whole function takes place in the right subtree)
        parent = self
        lastLeft = None
        lastLeftRightCheck = None

        while temp.left is not None:  # Looping till we found the needed node in the right-left subtree
            lastLeft = temp.left
            parent = temp
            temp = temp.right


        while temp.right is not None:   # Looping till we found the needed node in the right-right subtree
            lastLeftRightCheck = temp.left
            parent = temp
            temp = temp.right


        if lastLeft is None and lastLeftRightCheck is not None:  # If the lastLeft (so last node on the left) is None and lastLeftCheck, is there are no left nodes, lastLeftRightCheck will not me None
            self.data = lastLeftRightCheck.data  # lastLeftRight's data will become nodes data (because technically, lastLeftRight is the leftmost node
            lastLeftRightCheck = None
            del lastLeftRightCheck



        elif lastLeft is not None and lastLeftRightCheck is None:  # idem as lines before but with leftmost node an self.left
            self.data = lastLeft.data
            lastLeft = None
            del lastLeft


        elif temp.left is None:
            self.data = temp.data
            lastLeft = None
            del lastLeft
            parent.right = None


    def inorderTraverse(self):
        # Note: Someone helped me writing this Traverse function. I wrote the other ones myself (based on the inorderTraverse)

        if self:

            if self.left is not None:
                self.left.inorderTraverse()

            print(self.key)

            if self.right is not None:
                self.right.inorderTraverse()

    def postorderTraverse(self):  # Based on inorder

        if self:
            if self.left is not None:
                self.left.postorderTraverse()
            if self.right is not None:
                self.right.postorderTraverse()

            print(self.key)

    def preorderTraverse(self):  # Based on inorder

        if self:

            print(self.key)
            if self.left is not None:
                self.left.preorderTraverse()
            if self.right is not None:
                self.right.preorderTraverse()

    def emptyTree(self):  # Based on postorder, to empty the tree from the leaves to the root
        if self:

            if self.left is not None:
                self.left.emptyTree()
            if self.right is not None:
                self.right.emptyTree()


            self.left = None
            self.right = None
            self = None

    def save(self, noChildren):  # For the save function. Will print a tree out.

        if self.left is not None:


            toInsertLeft = self.left.save(False)  # Recursive, if left is not None, search in left
        else:
            toInsertLeft = None  # If the node is None

        if self.right is not None:

            toInsertRight = self.right.save(False)  # Recursive, if right is not None, search in right
        else:
            toInsertRight = None  # If the node is None

        savedTree = {'root': self.data}

        if self.left is None and self.right is None:  # Only makes noChildren = 1 if self has no children
            noChildren = True
        if self.left is None and self.right is None:  # Idem above
            noChildren = True

        if not noChildren:  # If the tree has 1 or 2 children, this part will be added.
            # Else the function will just create a root.
            savedTree.update({'children': [toInsertLeft, toInsertRight]})

        return savedTree




class BST:
    def __init__(self):
        self.root = None


    def createSearchTree(self) -> bool:  # Will create a BST
        self.root = None
        return True

    def destroySearchTree(self) -> bool:  # Will delete a BST
        del self
        return True

    def isEmpty(self) -> bool:  # Will check if a BST is empty by seeing if the root is empty
        if self.root is None:
            return True
        else:
            return False


    def searchTreeInsert(self, newItem) -> bool:  # Will insert a new node (= newItem) in the BST
        # If needed calls the insert function in the node class above
        if self.root is None:
            self.root = newItem
            return True
        else:
            # Looking on the left side of the tree
            if self.root.key > newItem.key:
                # If the left place of the root is indeed free. Else we can't insert there
                if self.root.left is None:
                    # If this place is free, insert
                    self.root.left = newItem
                    return True

                else:
                    self.root.left.insert(newItem)
                    return True

            # Looking on the right side of the tree
            if self.root.key < newItem.key:
                # If the right place of the root is free, insert here
                if self.root.right is None:
                    # If this place is free, insert
                    self.root.right = newItem
                    return True
                else:
                    self.root.right.insert(newItem)
                    return True



    def searchTreeDelete(self, searchKey) -> bool:  # Will delete a node in the BST
        #  Calls the function in the node class above
        if self.searchTreeRetrieve(searchKey)[1]:
            self.root.delete(searchKey)
            return True
        else:
            return False


    def searchTreeRetrieve(self, searchKey) -> tuple:  # Will search for a node in the BST
        # Will use the function find in the node class above

        resultTuple = tuple  # Defining the type of resultTuple


        if self.root.key > searchKey:  # If key is smaller than root key, search in the left subtree
            if self.root.left is not None:
                resultTuple = self.root.left.find(searchKey)


        # Looking on the right side of the tree
        elif self.root.key < searchKey:  # If key is greater than root key, search in the right subtree
            if self.root.right is not None:
                resultTuple = self.root.right.find(searchKey)

        elif self.root.key == searchKey:  # If the root search key is the key, return the roots data
            resultTuple = [self.root.key, True]

        if resultTuple is None:  # If we didn't find anything, return ... (try if this one can be deleted)
            resultTuple = [searchKey, False]

        if resultTuple == tuple:  # If we didn't find anything case 2.0, return ...
            return [searchKey, False]
        return resultTuple


    def preorderTraverse(self, visit) -> print:  # Speaks for itself, explained more thoroughly in the node class function

        # Calls a function in the node class
        if visit == print:
            self.root.preorderTraverse()


    def inorderTraverse(self, visit) -> print:  # Speaks for itself, explained more thoroughly in the node class function

        # Calls a function in the node class
        if visit == print:
            self.root.inorderTraverse()

    def postorderTraverse(self, visit) -> print:  # Speaks for itself, explained more thoroughly in the node class function

        # Calls a function in the node class
        if visit == print:
            self.root.postorderTraverse()


    def load(self, tree):  # Will load a BST in a correct structure


        if self.root is not None:
            self.root.emptyTree()
        self.root = None


        def recursionTreeDict(tree):

            if tree is not None:
                if tree['root'] is not None:

                    newNode = createTreeItem(tree['root'], tree['root'])
                    self.searchTreeInsert(newNode)

                if tree.get('children') is not None:

                    recursionTreeDict(tree['children'][0])
                    recursionTreeDict(tree['children'][1])



        recursionTreeDict(tree)  # Calling the recursion function to fix the children



    def load3(self, tree):  # Will load a BST in a correct structure


        if self.root is not None:
            self.root.emptyTree()
        self.root = None

        def recursionTreeDict(tree):
            if tree[0] is not None:  # if first item in the children list is not None ( so for the left nodes
                newNode = Node(tree[0]["root"], tree[0]["root"])  # Create a new node and insert
                self.searchTreeInsert(newNode)
                if "children" in tree[0]:
                    recursionTreeDict(tree[0]['children'])  # If that node also has children, insert them as well with a recursion function
            if tree[1] is not None:  # Idem, but for the right nodes
                newNode = Node(tree[1]["root"], tree[1]["root"])
                self.searchTreeInsert(newNode)
                if "children" in tree[1]:
                    recursionTreeDict(tree[0]["children"])


        if tree["root"] is not None:  # Creating the root first
            self.searchTreeInsert(Node(tree["root"], tree["root"]))

        recursionTreeDict(tree["children"])  # Calling the recursion function to fix the children


    def save(self):

        # Calls a function in the node class
        if self.root is not None:
            return self.root.save(False)





def createTreeItem(key, val) -> object:
    newNode = Node(key, val)
    return newNode



t = BST()

print(t.isEmpty())
print(t.searchTreeInsert(createTreeItem(8, 8)))
print(t.searchTreeInsert(createTreeItem(5, 3)))
print(t.searchTreeInsert(createTreeItem(7, 4)))
print(t.searchTreeInsert(createTreeItem(2, 7)))
print(t.searchTreeInsert(createTreeItem(9, 9)))
print(t.searchTreeInsert(createTreeItem(11, 11)))
print(t.searchTreeInsert(createTreeItem(12, 12)))
print(t.searchTreeInsert(createTreeItem(8, 8)))
print(t.searchTreeInsert(createTreeItem(5, 3)))
print(t.searchTreeInsert(createTreeItem(7, 4)))
print(t.searchTreeInsert(createTreeItem(2, 7)))
print(t.searchTreeInsert(createTreeItem(9, 9)))
print(t.searchTreeInsert(createTreeItem(11, 11)))
print(t.searchTreeInsert(createTreeItem(12, 12)))
print(t.searchTreeInsert(createTreeItem(8, 8)))
print(t.searchTreeInsert(createTreeItem(5, 3)))
print(t.searchTreeInsert(createTreeItem(7, 4)))
print(t.searchTreeInsert(createTreeItem(2, 7)))
print(t.searchTreeInsert(createTreeItem(9, 9)))
print(t.searchTreeInsert(createTreeItem(11, 11)))
print(t.searchTreeInsert(createTreeItem(12, 12)))
print(t.searchTreeInsert(createTreeItem(8, 8)))
print(t.searchTreeInsert(createTreeItem(5, 3)))
print(t.searchTreeInsert(createTreeItem(7, 4)))
print(t.searchTreeInsert(createTreeItem(2, 7)))
print(t.searchTreeInsert(createTreeItem(9, 9)))
print(t.searchTreeInsert(createTreeItem(11, 11)))
print(t.searchTreeInsert(createTreeItem(12, 12)))
print(t.searchTreeInsert(createTreeItem(8, 8)))
print(t.searchTreeInsert(createTreeItem(5, 3)))
print(t.searchTreeInsert(createTreeItem(7, 4)))
print(t.searchTreeInsert(createTreeItem(2, 7)))
print(t.searchTreeInsert(createTreeItem(9, 9)))
print(t.searchTreeInsert(createTreeItem(11, 11)))
print(t.searchTreeInsert(createTreeItem(13, 12)))

#for i in range(0,100):
    #print(t.searchTreeInsert(createTreeItem(i,"test")))


print(t.isEmpty())
print(t.searchTreeRetrieve(8)[0])
print(t.searchTreeRetrieve(5)[1])
print(t.searchTreeDelete(7))
print(t.searchTreeRetrieve(7)[0])
print(" ")
t.inorderTraverse(print)
print(t.save())


t.load({'root': 8, 'children': [{'root': 3, 'children': [{'root': 7}, {'root': 4}]}, {'root': 9, 'children': [None, {'root': 11, 'children': [None, {'root': 12, 'children': [None, {'root': 12}]}]}]}]})
# dict(iets:int , children:list, repeat check
for i in range(0, 3):
    print(" ")

t.searchTreeInsert(createTreeItem(15,15))
print(t.searchTreeDelete(0))
print(t.save())
print(t.searchTreeDelete(10))
print(t.save())