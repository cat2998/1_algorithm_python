import sys

n = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for i in range(n)]

def merge_sort(lst):

    def _merge_sort(a, left, right):
        if left < right:
            center = (left + right) // 2
            
            _merge_sort(a, left, center)
            _merge_sort(a, center + 1, right)

            i = left
            j = 0
            while i <= center:
                buff[j] = a[i]
                j += 1
                i += 1
            
            a_inx = left
            b = 0
            while i <= right and b < j:
                if buff[b] <= a[i]:
                    a[a_inx] = buff[b]
                    b += 1
                else:
                    a[a_inx] = a[i]
                    i += 1
                a_inx += 1
            
            while b < j:
                a[a_inx] = buff[b]
                b += 1
                a_inx += 1

    buff = [None] * len(lst)
    _merge_sort(lst, 0, len(lst) -1)
    del buff
    return lst

ll = merge_sort(l)
for i in ll:
    print(i)