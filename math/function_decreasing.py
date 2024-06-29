from sympy import is_increasing
from sympy.abc import x, y
from sympy import Interval, oo

expr_1 = -x ** 2
print(is_increasing(expr_1, Interval(-oo, 0)))
print(is_increasing(expr_1, Interval(0, oo)))

expr_2 = -x**2 + y
print(is_increasing(expr_2, Interval(-1, 2), x))