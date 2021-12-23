class Node:
   def __init__(self, value):
      self.left = None
      self.right = None
      self.data = value

class Tree:
   def __init__(self):
      self.root = None

# Create an add(val) method on the BST object to add new value to the tree. 
# This entails creating a BTNode with this value and connecting it at the 
# appropriate place in the tree. Unless specified otherwise, BSTs can contain duplicate values. 
   def add(self, data):
      newNode = Node(data)
      runner = self.root
      walker = None

      # run through BST with runner and let walker = the last node
      while runner != None:
         walker = runner
         if data <= runner.data:
            runner = runner.left
         else:
            runner = runner.right

      # add newNode to correct location
      if walker == None:
         walker = newNode
      elif data <= walker.data:
         walker.left = newNode
      else:
         walker.right = newNode
      
      return walker #, texas ranger

# Create a contains(val) method on BST that returns whether the tree contains a given value. 
# Take advantage of the BST structure to make this a much more rapid operation than SList.contains() would be. 
   def contains(self, data):
      success = "Tree contains" + str(data)
      fail = "Tree does not contain" + str(data)
      runner = self.root

      # if there is a root, go through the tree looking for a value match
      while runner != None:
         if runner.data == data:
            return success
         if data < runner.data:
            runner = runner.left
         else:
            runner = runner.right
         
      # If no root or no match, return fail:
         return fail
      
# Create a min() method on the BST class that returns the smallest value found in the BST. 
   def min(self):
      runner = self.root
      walker = None
      
      while runner != None:
         walker = runner
         runner = runner.left
      
      return walker.data

# Create a max() BST method that returns the largest value contained in the binary search tree. 
   def max(self):
      runner = self.root
      walker = None
      
      while runner != None:
         walker = runner
         runner = runner.right
      
      return walker.data

# BONUS Write a size() method that returns the number of nodes (values) contained in the tree. 
   def size(self):
      x = 0
      if self != None:
         x += 1
         if self._left != None:
            x += self._left.size()
         if self._right != None:
            x += self._rightchild.size()
      return x

# BONUS Create an isEmpty() method to return whether the BST is empty (whether it contains no values).

   def isEmpty(self):
      if self.root == None:
         return True
      else:
         return False