def mergeSort(array):
    
    length = len(array)

    if length == 1:
        return array

    mid = length // 2

    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])

    return merge(left, right)

def merge(left, right):

    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else: 
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])

    return output
    
if __name__ == "__main__":
    print("Merge Sort Algorithm")
    array = [1,5,7,3,5,4,7,8,3,3,2]
    print(f"Array: {array}")
    result = mergeSort(array)
    print(f"Result: {result}")
