import array as arr
from operator import length_hint
# Time Complexity: O(N log N)
# Auxiliary Space: O(1)
def Heapify(A, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    mx = i
    if l < n and A[l] > A[mx]:
        mx = l
    if r < n and A[r] > A[mx]:
        mx = r
    if mx != i:
        tamp = A[i]
        A[i] = A[mx]
        A[mx] = tamp
        Heapify(A , n, mx)

def buildHeap(A ,n):
    for i in range(n//2 - 1, -1, -1):
        Heapify(A , n, i)

def HeapSort(A, n):
    buildHeap(A, n)
    for i in range(n - 1, -1, -1):
        tamp = A[i]
        A[i] = A[0]
        A[0] = tamp
        Heapify(A, i, 0)

a = int(input())
n = list(map(int, input().strip().split()))
HeapSort(n, a)
print(n)


# a=[]
# n=int(input("Number of elements in array:"))
# for i in range(0,n):
#    l=int(input())
#    a.append(l)
# print(a)
