def bubble_sort(lista):
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(0, tam - i -1):
            if(lista[j] > lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
                
buble = [1557,14,51,54,166,845,23,74,523]
print("Normal:", buble)
bubble_sort(buble)
print("Bubble Sort:", buble)