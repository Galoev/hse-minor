def selection_sort(arr):
    n = len(arr)

    for j in range(n):
        min_idx = j
        for i in range(j + 1, n):
            if arr[i] < arr[min_idx]:
                min_idx = i

        arr[j], arr[min_idx] = arr[min_idx], arr[j]
    
    return arr

def bubble_sort(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        swap = False
        
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                swap_count += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        
        if not swap:
            break
    
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    

    return arr

# R = 3
# C = 3
# cells = [[r, c] for r in range(R) for c in range(C)]
# def dist(r1, c1, r2, c2):
#     return abs(r1 - r2) + abs(c1 - c2)


# arr = [42, 14, 26, 37, 8, 15]
# arr = [508, 675, 160, 957, 944]
# print("".join(bubble_sort(list("cledc"))))
# print("".join(bubble_sort(list("deccl"))))