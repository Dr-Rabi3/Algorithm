import array as arr
from operator import length_hint
def prefix_max(A, i):
    if i > 0:
        j = prefix_max(A, i - 1)
        if A[i] < A[j] :
            return j
    return i;

def Selection_Sort(A, i = None):
    if i is None: i = length_hint(A) - 1
    if i > 0:
        j = prefix_max(A, i)
        A[i] , A[j] = A[j] , A[i]
        Selection_Sort(A,i - 1)

a = int(input())
n = list(map(int, input().strip().split()))
Selection_Sort(n)
print(n)
