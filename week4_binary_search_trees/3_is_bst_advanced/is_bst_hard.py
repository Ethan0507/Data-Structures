#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


result = []


def getInOrder(node, tree):
    global result
    if node == -1:
        return
    if tree[node][1] != -1:
      getInOrder(tree[node][1], tree)
    if result and tree[node][0] < result[-1]:
      result[0] = float("inf")
    elif result and tree[node][0] == result[-1] and tree[node][1] != -1:
      result[0] = float("inf")
    else:
      result.append(tree[node][0])
    if tree[node][2] != -1:
      getInOrder(tree[node][2], tree)


def IsBinarySearchTree(tree):
    global result
    result = []
    if tree:
        getInOrder(0, tree)
        if result[0] == float("inf"):
            return False
    return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
