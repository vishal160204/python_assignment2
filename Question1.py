"""
1.Turn the following snippet into a function:
numbers = [1,2,3,4,5]
squares = []
for n in numbers:
squares.append(n*n)
print(squares)
"""





def calculate_aquare(nums:list[int])->list[int]:
    return [n * n for n in nums]
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    squares = calculate_aquare(numbers)
    print(squares)