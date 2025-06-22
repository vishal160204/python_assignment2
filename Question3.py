"""
3. Build a small command-line app to track quiz scores,
stored in a CSV file.
Functions Breakdown
def load_scores(path: str) -> list[tuple[str,int]]
def add_score(records: list[tuple[str,int]], name: str, score: int) ->
None
def save_scores(path: str, records: list[tuple[str,int]]) -> None
def top_n(records: list[tuple[str,int]], n: int) -> list[tuple[str,int]]
File Handling
Store records in scores.csv (each line: name,score)
On start, call load_scores; if file missing, start with empty list
After each new score, call save_scores (overwrite mode)
User Interaction Loop
Menu:
Show Top N Scores
Add New Score
Exit
Validate menu choice (catch non-ints / out-of-range)
For “Top N”, prompt for N, display the top N entries sorted by score
For “Add New Score”, prompt name and score (catch bad ints)
Exception Handling
Gracefully handle:
Missing or corrupted scores.csv (e.g. bad format)
Invalid user inputs anywhere
Stretch (Optional)
Add a “Delete All Scores” option, with a confirmation prompt
Allow loading/saving in JSON as well as CSV (detect by file
extension)
Imagine the “Score Keeper” app as a little helper that keeps track of quiz
scores in a simple text file. Here’s how it flows, step by step, in everyday
language:
Start Up & Load
When you run the program, it looks for a file called scores.csv.
If that file exists, it reads each line (like “Alice, 85”) and turns it into a
list of name+score pairs.
If the file isn’t there yet, it just starts with an empty list—like an empty
scoreboard.
Show You a Menu
You see three simple choices on screen:
Show the top N scores
Add a new score
Exit
Option 1: Show Top N Scores
You type in a number (for example, 3).
The program looks at all the stored scores, sorts them from highest
to lowest, and then shows you the top 3 names and their scores.
It’s like asking, “Who got the best grades?” and it quickly lists them
for you."""


import csv
from typing import List , Tuple

def load_scores(path:str) -> List[Tuple[str, int ]]:
    try:
        with open(path, "r") as file:
            reader = csv.reader(file)
            return [(row[0], int(row[1])) for row in reader if len(row) == 2]
    except FileNotFoundError:
        print(f"File '{path}' not found. Starting with an empty score list.")
        return []
    except ValueError as e:
        print(f"Error reading scores: {e}")
        return []
    

def add_score(records: List[Tuple[str, int]], name: str, score: int) -> None:
    records.append((name, score))       
def save_scores(path: str, records: List[Tuple[str, int]]) -> None:
    with open(path, "w", newline='') as file:
        writer = csv.writer(file)
        for record in records:
            writer.writerow(record)
def top_n(records: List[Tuple[str, int]], n: int) -> List[Tuple[str, int]]:
    sorted_records = sorted(records, key=lambda x: x[1], reverse=True)
    return sorted_records[:n]
def menu():
    print("Menu:")
    print("1. Show Top N Scores")
    print("2. Add New Score")
    print("3. Exit")
def main():
    path = "scores.csv"
    records = load_scores(path)
    
    while True:
        menu()
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            try:
                n = int(input("Enter the number of top scores to show: "))
                if n <= 0:
                    print("Please enter a positive integer.")
                    continue
                top_scores = top_n(records, n)
                print("Top Scores:")
                for name, score in top_scores:
                    print(f"{name}: {score}")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        
        elif choice == '2':
            name = input("Enter the name: ")
            try:
                score = int(input("Enter the score: "))
                add_score(records, name, score)
                save_scores(path, records)
                print(f"Score for {name} added successfully.")
            except ValueError:
                print("Invalid score. Please enter a valid integer.")
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()