def selection_sort(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]                        
                
selection = [634,11,8,516,25,66,12,44,14,55,88,124,62]
print("Normal:", selection)
selection_sort(selection)
print("Selection Sort:", selection)