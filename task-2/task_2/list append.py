numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

numbers.append(60)
print("After appending 60:", numbers)
numbers.remove(30)
print("After removing 30:", numbers)

removed_element = numbers.pop(2)
print(f"After popping element at index 2 ({removed_element}):", numbers)
