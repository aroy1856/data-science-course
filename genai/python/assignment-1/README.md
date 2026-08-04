# GenAI Assignment 1 - Python Data Structures

This notebook is basically me practicing the usual Python collections — lists, tuples, sets, and dictionaries — using a small product/store kind of example.

## How to run

Just open `data_structure.ipynb` and run all the cells \

## What's inside

**Task 1 - Lists & Tuples**  
Made a `products` list, a `sample_product` tuple, printed a few items, appended stuff, and also tried converting the tuple to a list so I could change the price.

**Task 2 - Sets**  
Built a `categories_set` from a categories list. Added a duplicate on purpose to show sets ignore it, and checked if a category exists with `in`.

**Task 3 - Dictionaries**  
`price_dict` maps product name → price. Added/updated products, removed one with `.pop()` so it doesn't crash if the name isn't there, then calculated average / max / min price.

**Task 4 - Putting it together**  
Combined products + prices + categories into a `catalog` (list of tuples). From that I made `category_to_products`, then printed whichever category has the most products.

## Files

- `data_structure.ipynb` — all the code
- `README.md` — this file
