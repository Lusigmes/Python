def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        left = lista[:meio]
        right = lista[meio:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1

merge = [78,45,1,4,75,62,33,12,351]
print("Normal:", merge)
merge_sort(merge)
print("Merge Sort:", merge)