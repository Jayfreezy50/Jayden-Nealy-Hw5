from collections import deque
arr = [10, 20, 30, 40, 50]

def reversedArray(arr):
    queue = deque()
    for i in arr:
        queue.append(i)

    # Dequeue elements to get them in reverse order
    reversed_array = []
    while queue:
        reversed_array.append(queue.pop())  # Pop from the right end to reverse
    return reversed_array


# Step 3: Get the reversed array and print it
reversed_arr = reversedArray(arr)
print("Reversed array:", end=' ')
for num in reversed_arr:
    print(num, end=' ')