# GenAI Assignment 6 - Error Handling

Playing around with try / except / finally — catching bad input, division by zero, weird prices in a list, missing files, that kind of stuff.

## How to run

Open `error-handling.ipynb` and run the cells top to bottom.

## What's inside

**Task 1 - Safe division**  
Takes two numbers, divides them, and catches `ValueError` / `ZeroDivisionError`. Always prints "Operation Complete" in `finally`.

**Task 2 - Bill calculator**  
Walks through a messy prices list (`'abc'`, negatives, etc.), skips the bad ones, and keeps a running total.

**Task 3 - Age check**  
`check_age` raises an error if age isn't between 1 and 120. Main code just catches it and prints the message.

**Task 4 - File reader**  
Ask for a filename, try to read it, handle `FileNotFoundError` / `PermissionError`, print the first 3 lines if it works. `finally` says the operation was attempted. Also wrote a sample `prices.txt` to test with.

**Task 5 - Shopping cart loop**  
Keep entering prices until you type `q`. Invalid / negative values get caught, then it prints item count and total bill at the end.

## Files

- `error-handling.ipynb` — all the code
- `prices.txt` — sample file used in the file-reader task
- `README.md` — this file
