# GenAI Assignment 4 - File Handling

Practicing reading and writing files in Python — sales numbers, product lists, that kind of thing. Mostly just open / write / append / read, nothing too fancy.

## How to run

Open `file_handling.ipynb` and run cells from the top.

The notebook creates a few `.txt` files in this folder while it runs.

## What's inside

**Task 1 - Write sales to a file**  
Wrote a list of sales into `sales_data.txt` (one per line). Also made a comma-separated version just for fun.

**Task 2 - Different ways to read**  
Tried `.read()`, `.readline()`, and `.readlines()`, then cleaned up the newlines and turned the values into ints.

**Task 3 - Append**  
Added a few more sales to the same file and printed the updated content.

**Task 4 - Summary from file**  
Read everything back and printed total, highest, lowest, and average sale.

**Task 5 - Products from user input**  
Asked for 3 products + prices and saved them as `ProductName | Price` in `products.txt`.

**Task 6 - Check before opening**  
Ask for a filename, use `os.path.exists()` so it doesn't blow up if the file isn't there.

**Task 7 - Discount report**  
Took a prices dict, applied a discount the user enters, wrote it to `discount.txt`, then appended a tiny summary at the end.

## Files

- `file_handling.ipynb` — all the code
- `sales_data.txt` / `sales_data_comma.txt` / `products.txt` / `discount.txt` — generated while running
- `README.md` — this file
