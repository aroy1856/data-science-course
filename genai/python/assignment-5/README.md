# GenAI Assignment 5 - Modules & Packages

Basically learning how to split code into modules and a small package instead of dumping everything in one file. There's a math module, a string module, and a tiny `shop_package` for discounts / billing.

## How to run

From this folder:

```bash
python main.py
```

That's it — no extra installs.

## What's inside

**math_utils.py**  
Simple stuff: `add`, `subtract`, `square`.

**string_utils.py**  
`capitalize_words`, `reverse_string`, and `word_count`.

**shop_package/**  
- `discount.py` — percentage discount + a flat ₹50 off  
- `billing.py` — total of a list + 5% tax  
- `__init__.py` — re-exports the functions so you can import them from the package directly

**main.py**  
Imports everything a few different ways (`import module`, `from module import ...`, package imports) and prints some test calls.

## Folder structure

```
assignment-5/
├── main.py
├── math_utils.py
├── string_utils.py
├── shop_package/
│   ├── __init__.py
│   ├── discount.py
│   └── billing.py
└── README.md
```
