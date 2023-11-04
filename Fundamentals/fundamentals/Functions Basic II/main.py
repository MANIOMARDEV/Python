# Countdown
def countdown(number):
    result = []
    for i in range(number, -1, -1):
        result.append(i)
    return result
countdown_list = countdown(5)
print(countdown_list)
def print_and_return(lst):
    # Check if the list has at least two elements
    if len(lst) >= 2:
        print(lst[0])  # Print the first value
        return lst[1]  # Return the second value
    else:
        return None  # Return None or raise an error if the list doesn't have two elements

# Example usage:
result = print_and_return([1, 2])
print(result)
def first_plus_length(lst):
    # Check if the list is not empty
    if len(lst) > 0:
        return lst[0] + len(lst)
    else:
        return None  # Return None or raise an error if the list is empty

# Example usage:
result = first_plus_length([1, 2, 3, 4, 5])
print(result)
def values_greater_than_second(lst):
    # Check if the list has at least 2 elements
    if len(lst) < 2:
        return False

    second_value = lst[1]
    new_list = [value for value in lst if value > second_value]

    count = len(new_list)  # Count the number of values greater than the second

    print(count)  # Print the count of values greater than the second
    return new_list  # Return the new list

# Example usages:
result1 = values_greater_than_second([5, 2, 3, 2, 1, 4])
print(result1)

result2 = values_greater_than_second([3])
print(result2)
def length_and_value(size, value):
    # Create and return a list with the specified size and value
    return [value] * size

# Example usages:
result1 = length_and_value(4, 7)
print(result1)

result2 = length_and_value(6, 2)
print(result2)