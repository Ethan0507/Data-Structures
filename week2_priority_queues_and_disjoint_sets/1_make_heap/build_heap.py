
 # python3
swaps = []


def left(i):
    return (i * 2) + 1


def right(i):
    return (i * 2) + 2


def shiftDown(index, tree):
    global swaps
    min_index = index
    if left(index) < len(tree) and tree[min_index] > tree[left(index)]:
        min_index = left(index)
    if right(index) < len(tree) and tree[min_index] > tree[right(index)]:
        min_index = right(index)
    if index == min_index:
        return
    tree[index], tree[min_index] = tree[min_index], tree[index]
    swaps.append((index, min_index))
    shiftDown(min_index, tree)


def build_heap(data):
    global swaps
    for i in range(len(data) // 2, -1, -1):
        shiftDown(i, data)
    return swaps
    # # TODO: replace by a more efficient implementation
    # swaps = []
    # for i in range(len(data)):
    #     for j in range(i + 1, len(data)):
    #         if data[i] > data[j]:
    #             swaps.append((i, j))
    #             data[i], data[j] = data[j], data[i]
    # return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
