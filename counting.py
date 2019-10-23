lista = [5,1,4,2,8]

def counting(arr): 
  maior = arr[0]
  menor = arr[0]

  for i in range(len(arr)):
    if arr[i] > maior:
      maior = arr[i]
    if arr[i] < menor:
      menor = arr[i]

  aux = [0*x for x in range(maior - menor + 1)]

  for i in range(len(arr)):
    aux[arr[i] - menor] += 1

  for i in range(1, len(arr)):
    aux[i] += aux[i - 1]
  
  resp = [0*x for x in range(len(arr))]

  for i in range(len(arr) - 1, 0, -1):
    resp[aux[arr[i] - menor] - 1] = arr[i]
    aux[arr[i] - menor] -= 1

  for i in range(len(arr)):
    arr[i] = resp[i]

counting(lista)
print lista