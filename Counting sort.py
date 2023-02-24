import array as arr
from operator import length_hint

# Worst Case Complexity: O(n+k) , n = array size , k = max element in array
def Counting_sort(A):
    size = len(A)
    Ans = [0] * size
    frq = [0] * 10
    for i in range(0, size):
        frq[A[i]] += 1

    for i in range(1 ,10):
        frq[i] += frq[i - 1]

    i = size - 1
    while i >= 0:
        Ans[frq[A[i]] - 1] = A[i]
        frq[A[i]] -= 1
        i -= 1

    for i in range(0, size):
        A[i] = Ans[i]

a = int(input())
n = list(map(int, input().strip().split()))
Counting_sort(n)
print(n)
