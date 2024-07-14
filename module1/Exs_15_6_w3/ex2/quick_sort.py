# Function to find the partition position
def partition(person_list, low, high):
    # Choose the rightmost element as pivot
    pivot = person_list[high].yob

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if person_list[j].yob <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (person_list[i], person_list[j]) = (person_list[j], person_list[i])

    # Swap the pivot element with
    # the greater element specified by i
    (person_list[i + 1], person_list[high]
     ) = (person_list[high], person_list[i + 1])

    # Return the position from where partition is done
    return i + 1


# Function to perform quicksort
def quicksort(person_list, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(person_list, low, high)

        # Recursive call on the left of pivot
        quicksort(person_list, low, pi - 1)

        # Recursive call on the right of pivot
        quicksort(person_list, pi + 1, high)
        
