import array as arr
from operator import length_hint

# Worst Case Complexity: O(n+k) , n = array size , k = max element in array
def Counting_sort(A, place):
    size = len(A)
    Ans = [0] * size
    frq = [0] * 10
    for i in range(0, size):
        index = A[i] // place
        frq[index % 10] += 1

    for i in range(1 ,10):
        frq[i] += frq[i - 1]

    i = size - 1
    while i >= 0:
        index = A[i] // place
        Ans[frq[index % 10] - 1] = A[i]
        frq[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        A[i] = Ans[i]

def Radix_sort(A):
    maxEle = max(A)
    place = 1
    while maxEle // place > 0:
        Counting_sort(A, place)
        place *= 10
a = int(input())
n = list(map(int, input().strip().split()))
Radix_sort(n)
print(n)
