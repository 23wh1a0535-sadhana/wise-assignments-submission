arr = [5, 9, 1, 10, 3, 8, 4, 2, 7, 6]
temp = 0
max_size = len(arr)
print("The elements of the array before sorting: ");
for i in range(0, max_size):
   print(arr[i], end=" ")

print()
for i in range(0, max_size):
   for j in range(i+1, len(arr)):
      if(arr[i] > arr[j]):
         temp = arr[i]
         arr[i] = arr[j]
         arr[j] = temp
print("The elements of the array after sorting: ")

for i in range(0, max_size):
   print(arr[i], end=" ")