def heapsort(list_of_num):
    build_max_heap(list_of_num)
    for i in range(len(list_of_num) - 1, 0, -1):
        list_of_num[0], list_of_num[i] = list_of_num[i], list_of_num[0]
        max_heapify(list_of_num, index=0, size=i)


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def build_max_heap(list_of_num):
    length = len(list_of_num)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(list_of_num, index=start, size=length)
        start = start - 1


def max_heapify(list_of_num, index, size):
    left_side = left(index)
    right_side = right(index)
    if left_side < size and list_of_num[left_side] > list_of_num[index]:
        largest = left_side
    else:
        largest = index
    if right_side < size and list_of_num[right_side] > list_of_num[largest]:
        largest = right_side
    if largest != index:
        list_of_num[largest], list_of_num[index] = list_of_num[index], list_of_num[largest]
        max_heapify(list_of_num, largest, size)


'''
:arg list_of_num: list of numbers to be sorted
:arg index: starting index of the heap
:arg size: size of the heap
'''

while True:
    # noinspection PyBroadException
    try:
        list_of_num = input('Enter a list of numbers: ').split()
        list_of_num = [int(x) for x in list_of_num]
        heapsort(list_of_num)
        print('Sorted list: ', end='')
        print(list_of_num)
        break
    except Exception as e:
        print('Invalid input')
