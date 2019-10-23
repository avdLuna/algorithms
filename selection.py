lista = [5,1,4,2,8]

def selection(arr):
  for i in range(len(arr)): 
 
    min_idx = i 
    for j in range(i+1, len(arr)): 
        if arr[min_idx] > arr[j]: 
            min_idx = j 
     
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

selection(lista)
print lista