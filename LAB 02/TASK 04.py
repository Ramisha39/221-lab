file = open("input problem 04.txt")

x = file.read()

temp = x.split("\n")

t = temp[1].split(" ")

arr = []
for k in t:
    k = int(k)
    arr.append(k)


def merge(l, r, A):
    n1 = len(l)
    n2 = len(r)
    i = j = k = 0

    while i < n1 and j < n2:
        if l[i] <= r[j]:
            A[k] = l[i]
            k += 1
            i += 1
        else:
            A[k] = r[j]
            k += 1
            j += 1

    while i < n1:
        A[k] = l[i]
        k += 1
        i += 1
    while j < n2:
        A[k] = r[j]
        k += 1
        j += 1


def merge_sort(A):
    n = len(A)

    if len(A) < 2:
        return
    mid = n//2
    left = [0]*mid
    right = [0]*(n - mid)
    for i in range(mid):
        left[i] = A[i]
    for i in range(mid, n):
        right[i-mid] = A[i]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, A)


call = merge_sort(arr)

output = open("output problem 04.txt", "w")
string = ""
for i in range(len(arr)):
    string += str(arr[i]) + " "

output.write(string)

