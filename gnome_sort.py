# Filename: gnome_sort.py

def gnome_sort(arr: list[int]) -> list[int]:
    """
    Sorts a list using the Gnome Sort algorithm.
    """
    index = 0
    while index < len(arr):
        # If we are at the beginning or the current element is in the correct
        # place relative to the previous one, just move forward.
        if index == 0 or arr[index] >= arr[index - 1]:
            index += 1
        else:
            # If the current element is smaller than the previous one,
            # swap them and take one step back.
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
            
    return arr

# --- Example Usage ---
my_list = [34, 2, 10, -9, 5]
print(f"Original: {my_list}")
gnome_sort(my_list)
print(f"Sorted:   {my_list}")


another_list = [6, 1, 7, 3, 5, 8]
print(f"\nOriginal: {another_list}")
sorted_list = gnome_sort(another_list)
print(f"Sorted:   {sorted_list}")
