flag = -1
n = int(input("Enter the size of elements:"))
lst = []
for i in range(n):
    lst.append(int(input()))
search = int(input("Enter the search element:"))
low = 0
high = n - 1

while low <= high:
    mid = (low + high) // 2 
    if lst[mid] == search:
        flag = mid
        break
    elif lst[mid] < search:
        low = mid + 1
    else:
        high = mid - 1
if flag != -1:
    print(f"Element found at index {flag}")
else:
    print("Element not found")
