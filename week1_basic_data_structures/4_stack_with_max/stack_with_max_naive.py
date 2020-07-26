#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max_stack = []

    def Push(self, a):
        self.__stack.append(a)
        if not self.max_stack:
            self.max_stack.append(a)
        elif a >= self.max_stack[-1]:
            self.max_stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        x = self.__stack.pop()
        if x == self.max_stack[-1]:
            self.max_stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.max_stack[-1] if self.max_stack else ''


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
