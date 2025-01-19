# finding largest element from array
arr = [1, 2, 3, 4, 5, 6]
largest = arr[0]
for i in arr:
    if i > largest:
        largest = i
print(largest)


# another method
def largest(arr, n):
    max = arr[0]

    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
answer = largest(arr, n)
print("Largest number is :", answer)

# sorting an array in ascending
# price = [10, 12, 16, 9, 8, 3, 20, 45, 3, 7]
# price.sort(reverse=False)
# print(price)

# finding second largest element from array

price = [10, 12, 16, 9, 8, 3, 20, 45, 45, 3, 7]


def secLargest(price, p):
    price.sort(reverse=True)
    print(price)
    for a in range(1, n):
        if price[a] != price[0]:
            sec_larg = price[a]
            break
    return sec_larg


p = len(price)
ans = secLargest(price, p)
print(ans)
