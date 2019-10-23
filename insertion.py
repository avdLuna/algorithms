lista = [5,1,4,2,8]

def insertion(arr): 
 
    for i in range(1, len(arr)):  
        ind = arr[i] 
        j = i-1
        while j >= 0 and ind < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = ind 

insertion(lista)
print lista