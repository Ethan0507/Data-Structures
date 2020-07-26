# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c


  def getInOrder(self, node):
    if node == -1:
        return
    self.getInOrder(self.left[node])
    self.result.append(self.key[node])
    self.getInOrder(self.right[node])

  def inOrder(self):
    self.result = []
    self.getInOrder(0)
    return self.result


  def getPreOrder(self, node):
    if node == -1:
        return
    self.result.append(self.key[node])
    self.getPreOrder(self.left[node])
    self.getPreOrder(self.right[node])

  def preOrder(self):
    self.result = []
    self.getPreOrder(0)
    return self.result

  def getPostOrder(self, node):
    if node == -1:
        return
    self.getPostOrder(self.left[node])
    self.getPostOrder(self.right[node])
    self.result.append(self.key[node])

  def postOrder(self):
    self.result = []
    self.getPostOrder(0)
    return self.result

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
