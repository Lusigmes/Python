def insertion_sort(lista):
    for i in range(1,len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = key
                                         
insertion = [8658,32,6,62,2,99,23,48,14,58,121]
print("Normal:", insertion)
insertion_sort(insertion)
print("Insertion Sort:", insertion)