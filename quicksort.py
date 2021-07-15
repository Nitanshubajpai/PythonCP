def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i<=pivot]
        more = [i for i in array[1:] if i>pivot]
        return quicksort(less) + [pivot] + quicksort(more)

def binarysearch(array, low, high, number):
    if high>=low:
        mid = (high+low)//2
        if array[mid] == number:
            return mid
        elif array[mid] > number:
            return binarysearch(array, low, mid - 1, number)
        else:
            return binarysearch(array, mid + 1, high, number)
    else:
        return -1
        
def main():
    array = list(map(int,input().split(',')))
    sorted = quicksort(array)
    number = int(input())
    print(sorted)
    print("index of number:",binarysearch(sorted,0, len(array)-1, number))

main()

