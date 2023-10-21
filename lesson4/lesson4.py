# Сортировка выбором
def SelectionSort(A):
    for i in range(len(A)):
        min_idx = i

        for j in range(i + 1, len(A)):
            if A[j] < A[min_idx]:
                min_idx = j
        
        tmp = A[i]
        A[i] = A[min_idx]
        A[min_idx] = tmp
        
        # A[i], A[min_idx] = A[min_idx], A[i]
    return A

# Сортировка вставками
def InsertionSort(A):
    for i in range(1, len(A)):
        new_elem = A[i]
        j = i - 1

        while j >= 0 and A[j] > new_elem:
            A[j + 1] = A[j]
            j -= 1
        
        A[j + 1] = new_elem

# Cортировка пузырьком
def BubbleSort(A):
    for j in range(len(A) - 1, 0, -1):
        for i in range(j):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]

def BubbleSort2(A):
    j = len(A) - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(j):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                swapped = True
        j -= 1


if __name__ == "__main__":
    A = [4, 3, 6, 2, 1, 5]
    print(SelectionSort(A))