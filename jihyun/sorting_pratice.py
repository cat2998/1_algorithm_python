# 버블정렬 O(n^2)
def bubble_sort(l):
    for i in range(len(l) - 1):
        exchange = 0
        for j in range(len(l) - 1, i, -1):
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]
                exchange += 1
        if exchange == 0:
            break

# 단순삽입정렬 O(n^2)
def insertion_sort(l):
    for i in range(1, len(l)):
        j = i
        tmp = l[i]
        while tmp < l[j - 1] and j > 0:
            l[j] = l[j - 1]
            j -= 1
        l[j] = tmp

# 퀵정렬 O(nlogn)
def partition(l):
    n = len(l)
    pl = 0 # 왼쪽 커서
    pr = n - 1 # 오른쪽 커서
    pivot = l[n // 2]
    while pl <= pr:
        while l[pl] < pivot:
            pl += 1
        while l[pr] > pivot:
            pr -= 1
        if pl <= pr:
            l[pl], l[pr] = l[pr], l[pl]
            pl += 1
            pr -= 1

def qsort(l, left, right):
    pl = left
    pr = right
    pivot = l[(left + right) // 2]
    
    while pl <= pr:
        while l[pl] < pivot:
            pl += 1
        while pivot < l[pr]:
            pr -= 1
        if pl <= pr:
            l[pl], l[pr] = l[pr], l[pl]
            pl += 1
            pr -=1
    
    if left < pr:
        qsort(l, left, pr)
    if pl < right:
        qsort(l, pl, right)

# 병합정렬 O(nlogn)
def merge_sorted_list(a, b, c):
    pa = pb = pc = 0
    na, nb, nc = len(a), len(b), len(c)

    while pa < na and pb < nb:
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1
    
    while pa < na:
        c[pc] = a[pa]
        pa += 1
        pc += 1
    
    while pb < nb:
        c[pc] = b[pb]
        pb += 1
        pc += 1
    
    print(c)

def merge_sort(a):

    def _merge_sort(a, left, right):
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)
            _merge_sort(a, center + 1, right)

            a_comp_inx = left
            buff_goal_inx = 0
            while a_comp_inx <= center:
                buff[buff_goal_inx] = a[a_comp_inx]
                buff_goal_inx += 1
                a_comp_inx += 1
            
            a_inx = left
            j = 0
            while a_comp_inx <= right and j < buff_goal_inx:
                if buff[j] <= a[a_comp_inx]:
                    a[a_inx] = buff[j]
                    j += 1
                else:
                    a[a_inx] = a[a_comp_inx]
                    a_comp_inx += 1
                a_inx += 1
            
            while j < buff_goal_inx:
                a[a_inx] = buff[j]
                a_inx += 1
                j += 1
            
    n = len(a)
    buff = [None] * n
    _merge_sort(a, 0, n - 1)
    del buff
    print(a)


# l = list(map(int, input().split()))
# bubble_sort(l)
# insertion_sort(l)
# partition(l)
# qsort(l, 0, len(l) - 1)
# a = [1, 2, 3, 4, 7, 8]
# b = [1, 4, 5, 9, 10]
# merge_sorted_list(a, b, [None] * (len(a) + len(b)))
merge_sort([3, 6, 3, 2, 3, 5, 7, 2, 4, 7,2, 4, 5, 9, 4])
# print(l)
