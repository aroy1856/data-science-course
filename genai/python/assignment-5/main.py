from math_utils import square
import math_utils
from string_utils import capitalize_words, reverse_string, word_count

from shop_package import apply_discount, flat_discount
from shop_package import billing

print(math_utils.add(1, 2))
print(math_utils.subtract(10, 2))
print(square(3))

print(capitalize_words("hello world"))
print(reverse_string("hello world"))
print(word_count("hello world"))

print(apply_discount(100, 10))
print(flat_discount(100))
print(billing.calculate_total([100, 200, 300]))
print(billing.apply_tax(100))