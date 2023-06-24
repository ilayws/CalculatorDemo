from typing import List

numbers = "0123456789."
operators = "^*/+-"

# Replace items in list with single item (val)
def replace(expr:List, i_start:int, i_end:int, val:float) -> List:
    if i_end > len(expr):
        i_end = len(expr)
    for i in range(i_start,i_end-1):
        expr.pop(i_start)
    expr[i_start] = val
    return expr

# Takes list and "(" index and finds ")" index
def match_parantheses(expr:List, i_start:int) -> int:
    i_end = i_start+1
    counter = 1
    while True: 
        if expr[i_end] == "(":
            counter += 1
        elif expr[i_end] == ")":
            counter -= 1
        if counter == 0:
            break
        i_end += 1
    return i_end

# Identify numbers and cast to float
def numbers2floats(expr:List) -> List:
    i_start = 0
    while i_start < len(expr):
        if type(expr[i_start]) is float:
            pass
        elif expr[i_start] in numbers:
            number_string = expr[i_start]
            i_end = i_start+1
            try:
                while expr[i_end] in numbers:
                    number_string += expr[i_end]
                    i_end += 1
            except:
                pass
            expr = replace(expr, i_start, i_end, float(number_string))
        i_start += 1
    return expr

# Solve all calculations of a certain operator in an expression
def handle_operations(expr:List, ops:str, val) -> List:
    i = 0
    while i < len(expr)-1:
        for j,op in enumerate(ops):
            if expr[i] == op:
                sub_output = val[j](expr[i-1], expr[i+1])
                expr = replace(expr, i-1, i+2, sub_output)
                i -= 1
        i += 1
    return expr

# Solve a mathematical expression
def solve_expression(expr:List) -> List:
    '''
    1. Handle parantheses recursively
    2. Cast numbers to float
    3. Calculate operations according to PEMDAS
    '''
    # Handle paranthese
    while "(" in expr:
        
        # Find parantheses
        i_start = expr.index("(")
        i_end = match_parantheses(expr, i_start)
        
        # Replace sub-expression with its solution
        sub_expr = expr[i_start+1:i_end]
        sub_output = solve_expression(sub_expr)[0]
        expr = replace(expr, i_start, i_end+1, sub_output)

    # Cast numbers to float
    expr = numbers2floats(expr)

    # Handle single operators with PEMDAS
    expr = handle_operations(expr, "^", [lambda a,b: pow(a,b)])
    expr = handle_operations(expr, "*/", [lambda a,b: a*b, lambda a,b: a/b])
    expr = handle_operations(expr, "+-", [lambda a,b: a+b,lambda a,b: a-b])

    return expr


# Main loop
while True:
    input_text = [c for c in input("Meow?\n") if c != " "]
    input_expr = []
    # Handle negative numbers
    for i,char in enumerate(input_text):
        if not char in "0123456789.()^*/+-":
            continue
        not_number = not input_text[i-1] in numbers or i==0
        if char == "-" and not_number:
            input_expr.append("0")
        input_expr.append(char)
    
    try:
        output = solve_expression(input_expr)
        print(output[0])
    except:
        print("Invalid expression.")
    if input("Continue or sadge (Y for yes)").upper() != "Y":
        break

print("G'bye dude/dudette")