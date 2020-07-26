# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    tracker = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            tracker.append(i)

        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            elif not are_matching(opening_brackets_stack.pop(), next):
                return i + 1
            else:
                tracker.pop()
    if opening_brackets_stack:
        return tracker[0] + 1
    return 0


def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == 0:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
