# GenAI Assignment 7 - OOP

Going through the usual OOP stuff in Python — classes, inheritance, polymorphism, abstract classes, and a tiny store/inventory mini project at the end. All based around products again.

## How to run

Open `oop.ipynb` and run cells

No extra packages needed (just the built-in `abc` module for the abstract class task).

## What's inside

**Task 1 - Basic class**  
`Product` with name / price / category, plus `get_info()` and an optional `apply_discount()`.

**Task 2 - Encapsulation**  
Made price private (`__price`) with `get_price()` / `set_price()` so you can't set a negative price.

**Task 3 - Inheritance**  
`ElectronicProduct` inherits from `Product`, adds warranty years, and overrides `get_info()`.

**Task 4 - Polymorphism**  
`Laptop` and `Mobile` both override `get_info()` differently, then loop over a mixed list and call the same method.

**Task 5 - Abstraction**  
Abstract `Payment` class with `process_payment()`, then `CreditCardPayment` and `UPIPayment` implementations.

**Task 6 - Magic methods**  
Added `__str__` and `__add__` so you can print a product nicely and do `product1 + product2` for total price.

**Task 7 - Mini inventory**  
`Inventory` (add / remove / total value / show all) and `Store` wrapping it. Added a few products, showed summary, removed one, etc.

## Files

- `oop.ipynb` — all the code
- `README.md` — this file
