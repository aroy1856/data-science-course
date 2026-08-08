# GenAI Assignment 3 - Functions

Just going through functions in Python — normal ones, recursion, lambdas, and then map/filter. All of it is based around prices / discounts so it feels a bit more real than random math examples.

## How to run

Open `function.ipynb` and run the cells top to bottom. For Task 7 (the menu), you'll need to type in the input box when it asks — press `q` to quit.

No extra packages needed.

## What's inside

**Task 1 - Discount function**  
`apply_discount(price, discount_percent)` with a default 5% discount. Also capped it so discount can't go above 60%.

**Task 2 - Factorial (recursive)**  
Recursive `factorial(n)`. Handles 0 and 1, and prints a message if you pass a negative number.

**Task 3 - GST lambda**  
Simple lambda that adds 18% GST. Also made another one that does discount + GST together.

**Task 4 - map()**  
Took a list of prices and used `map` with the gst lambda to get prices after GST.

**Task 5 - filter()**  
Split prices into expensive (> 500) and cheap (<= 500) using `filter`.

**Task 6 - Combined**  
`process_prices` applies a 10% discount with map, then filters out anything that isn't above 300 after discount.

**Task 7 - Mini menu**  
Three small helpers (add price, average, max) and a loop-based menu so you can pick options until you quit.

## Files

- `function.ipynb` — all the code
- `README.md` — this file
