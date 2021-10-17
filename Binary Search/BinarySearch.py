def binarySearch(array, x, start, end):

    array.sort()
    if start > end:
        return -1
    
    mid = (start + end) // 2
    if x == array[mid]:
        return mid

    if x < array[mid]:
        return binarySearch(array, x, start, mid - 1)
    else:
        return binarySearch(array, x, mid + 1, end)

if __name__ == "__main__":
    print("Binary Search Algorithm")
    array = [1,5,7,3,5,4,7,8,3,3,2]
    print(f"Array: {array}")
    target = 4
    print(f"Target: {target}")
    result = binarySearch(array, target, 0, len(array))
    print(f"Result: {result}")
    print(f"Element's occurence is at {result}")
