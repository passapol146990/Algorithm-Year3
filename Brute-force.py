def Search_miss(arr, n):
    for i in range(1, n + 1):
        if i not in arr:
            return i

a = [5,3,2,4]
x = Search_miss(a,5)
print(x)
