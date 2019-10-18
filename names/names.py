import time

##### Method 1: Python Dictionary (wasnt against the rules!)- time under .01

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names1_dict = {}
duplicates = []
for name_1 in names_1:
    names1_dict[name_1] = None

for name_2 in names_2:
    if name_2 in names1_dict:
        duplicates.append(name_2)

end_time = time.time()
print('\n***** Python dictionary Method ***** \n')
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


#### Method 2: Binary Search Tree

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value, False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            return False if self.left is None else self.left.contains(target)
        else:
            return False if self.right is None else self.right.contains(target)

start_time = time.time()

duplicates = []

### Construct search tree w/ names_1:
#start w/ first name in names_1 as root:
tree = BinarySearchTree(names_1[0])

for name in names_1[1:]:
    tree.insert(name)
    
#search the tree for each name in names_2:
for name in names_2:
    if tree.contains(name):
        duplicates.append(name)

end_time = time.time()
print('\n***** Binary Search Tree Method ***** \n')
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")