lista = [5,1,4,2,8]

def swap(arr,i,j):
  arr[j], arr[j+1] = arr[j+1], arr[j]

def bubble(arr):
  for i in range(len(arr)):
    for j in range(len(arr) -1):
      if arr[j] > arr[j+1]:
        swap(arr,i,j)

bubble(lista)
print lista