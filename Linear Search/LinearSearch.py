def linearSearch(array, x):
    for i in range(len(array)):
        if x == array[i]:
            return i
    return -1

if __name__ == "__main__":
    print("Linear Search Algorithm")
    array = [1,5,7,3,5,4,7,8,3,3,2]
    print(f"Array: {array}")
    target = 4
    print(f"Target: {target}")
    result = linearSearch(array, target)
    print(f"Result: {result}")
    print(f"Element's occurence is at {result}")