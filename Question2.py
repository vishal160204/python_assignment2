"""
2.Write a function that reads a text file and returns its
lines.
Requirements:
Create def compute_squares(nums: list[int]) -> list[int]
Add a docstring and type hints
Call it on at least two different lists
Use with open(...) as f:
Catch and handle FileNotFoundError with a user-friendly message.
From main(), prompt user for file name, call read_lines, then print line
count

"""


def read_lines(file_name: str) -> list[str]:
 try:
    with open(file_name,"r") as f:
        return f.readlines()
 except FileNotFoundError:
    print("file '{file_name}' not found .")
    return []

if __name__== "__main__":
    file_name=input("Enter the file name: ")
    lines=read_lines(file_name)
    print(f"number of the lines in the file '{file_name}' is {len(lines)}")
    