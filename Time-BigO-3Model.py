import time
import random
import matplotlib.pyplot as plt

class QuickSort:
    def swapArray(data, swap1, swap2):
        data[swap1], data[swap2] = data[swap2], data[swap1]

    def sort(data, start, end):
        f, r = start, end
        if end > start:
            pivot = data[end]
            while r > f:
                while f < end and data[f] < pivot and r > f:
                    f += 1
                while r > start and data[r] >= pivot and r >= f:
                    r -= 1
                if r > f:
                    QuickSort.swapArray(data, f, r)
            QuickSort.swapArray(data, f, end)
            QuickSort.sort(data, start, f -1)
            QuickSort.sort(data, f + 1, end)

class RadixSort:
    def getMax(arr):
        return max(arr)
    
    def counting(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            digit = (arr[i] // exp) % 10
            count[digit] += 1
        for i in range(1,10):
            count[i] += count[i-1]
        for i in range(n-1, -1, -1):
            digit = (arr[i] // exp) % 10
            output[count[digit] - 1] = arr[i]
            count[digit] -= 1
        for i in range(n):
            arr[i] = output[i]
    
    def sort(arr):
        start = time.perf_counter()
        max = RadixSort.getMax(arr)
        exp = 1
        while max // exp > 0:
            RadixSort.counting(arr, exp)
            exp *= 10
        end = time.perf_counter()
        return end - start

class SelectSort:
    def sort(arr):
        start = time.perf_counter()
        n = len(arr)
        for i in range(n - 1):
            min = i
            for j in range(i + 1, n):
                if arr[j] > arr[min]:
                    min = j
            arr[min], arr[i] = arr[i], arr[min]
        end = time.perf_counter()
        return end - start

x = [10,20,30,40,50]
y1,y2,y3 = [],[],[]

for size in x:
    arr = [random.randint(1,100) for _ in range(size)]
    y1.append(SelectSort.sort(arr)*1000)
    y2.append(RadixSort.sort(arr)*1000)
    start = time.perf_counter()
    QuickSort.sort(arr,0,len(arr)-1)
    end = time.perf_counter()
    y3.append((end-start)*1000)

print(y1)
print(y2)
print(y3)


plt.plot(x, y1, label='Select Sort', marker='o', color='blue')
plt.plot(x, y2, label='Radix Sort', marker='o', color='green')
plt.plot(x, y3, label='Quick Sort', marker='o', color='red')

plt.title('Graph')
plt.xlabel('X (Lenght of Array) ')
plt.ylabel('Y (Time) ms ')
center_x = sum(x) / len(x) 
top_y = max(y1 + y2 + y3)   
balance = 0.006
font = 9
plt.text(x[len(x)-1]-2, y1[len(y1)-1] - balance, 'Select', color='blue', fontsize=font)
plt.text(x[len(x)-1]-2,     y2[len(y2)-1] - balance, 'Radix',  color='green', fontsize=font)
plt.text(x[len(x)-1]-2, y3[len(y3)-1] - balance, 'Quick',  color='red', fontsize=font)

plt.show()