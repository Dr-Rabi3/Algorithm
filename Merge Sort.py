import array as arr
from operator import length_hint

def merge(L , R , A , i , j , a , b ):
    if a < b:
        if (j <= 0) or (i > 0 and L[i - 1] > R[j - 1]):
            A[b - 1] = L[i - 1]
            i = i - 1
        else:
            A[b - 1] = R[j - 1]
            j = j - 1
        merge(L , R , A , i , j , a , b - 1)

def Merge_Sort(A,a = 0, b = None):
    if b is None: b = length_hint(A)
    if 1 < b - a:
        c = (a + b + 1) // 2
        Merge_Sort(A, a, c)
        Merge_Sort(A, c, b)
        L, R = A[a:c] , A[c:b]
        merge(L, R, A, length_hint(L), length_hint(R), a, b)

a = int(input())
n = list(map(int, input().strip().split()))
Merge_Sort(n)
print(n)
