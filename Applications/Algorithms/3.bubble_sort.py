"""Implement a function for a bubble sort."""

def bubble_sort(l, reverse = False):
    arrange_flag = True
    while arrange_flag:
        arrange_flag = False
        for i in range(len(l)-1):
            if ((l[i] > l[i+1]) and not reverse) or ((l[i] < l[i+1]) and reverse):
                arrange_flag = True
                l[i+1], l[i] = l[i], l[i+1]
    return l

# Test cases
if __name__ == '__main__':
    print(bubble_sort([3, 2, 1, -1, 0, 0]))
    print(bubble_sort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))
    print(bubble_sort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14], reverse= True))
    test_list = [1 , 16, -12, 25]
    print('list before bubble sort: ', test_list)
    bubble_sort(test_list)
    print('list after bubble sort:  ', test_list)
