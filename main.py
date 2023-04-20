#!/usr/bin/python3
from copy import deepcopy
from libs.translate import *
from libs.functions import *


def main():
	math_expr = interpret([input("Enter your formula: ")])
	args = {}
	args_errs = {}
	for var in math_expr.variables:
		args[var] = float(input(f"Enter value of {var} variable: "))
		args_errs[var] = float(input(f"Enter value of {var}'s error: "))
	res = []
	print("Значение величины: ", math_expr.value(args))
	for var in math_expr.variables:
		math_expr_deriv = deepcopy(math_expr)
		math_expr_deriv.differentiate(var)
		res.append((args_errs[var]*math_expr_deriv.value(args))**2)
	print("Ее погрешность", sum(res)**0.5)

main()
