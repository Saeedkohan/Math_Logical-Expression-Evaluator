
from itertools import product

input_expr = "A^(BvC)^D"

variables = sorted(set(x for x in input_expr if x.isalpha() and x.isupper()))
def generate_truth_values(var_count):
    return [list(values) for values in product([True, False], repeat=var_count)]

def evaluate_expression(expr, values):
    for var in values:
        
        expr = expr.replace(var, str(values[var]))
    expr = expr.replace("^", " and ").replace("v", " or ")

    return eval(expr)

truth_values = generate_truth_values(len(variables))
evaluated_results = []

for values in truth_values:

    values_dict = dict(zip(variables, values))
    result = evaluate_expression(input_expr, values_dict)
    evaluated_results.append(result)

header = " | ".join(f"{var:<7}" for var in variables) + f" | {input_expr}"
print(header)
print("-" * len(header))
for i, value in enumerate(truth_values):
    row = " | ".join(f"{str(val):<7}" for val in value)
    print(f"{row} | {str(evaluated_results[i]):<7}")
