import time

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value > value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif self.value < value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        elif self.right == None:
            self.right = BinarySearchTree(value)
        else:
            self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        elif self.value < target and self.right:
            return self.right.contains(target)
        elif self.value > target and self.left:
            return self.left.contains(target)
        else:
            return False

    def get_max(self):
        node = self
        while node.right is not None:
            node = node.right
        return node.value

    def for_each(self, cb):
        cb(self.value)
        if self.left is None and self.right is None:
            return
        else:
            if self.left is not None:
                self.left.for_each(cb)
            if self.right is not None:
                self.right.for_each(cb)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
tree = BinarySearchTree(names_1[0])
for index in range(1, len(names_1)):
    tree.insert(names_1[index])

for name in names_2:
    if tree.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
