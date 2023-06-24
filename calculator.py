# Calculator Project By Ilay Wischnevsky Shlush

# Intro
msg = "Welcome to the IWSC - Easy to use, mathematically correct calculator!\nEnter a math expression using spaces after every number, parantheses or operator except the last one.\n"

expr = input(msg)


expr = expr.split(" ")
print(expr)

# Check if string is a number
def isNumber(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
  
def removeIndexes(l, start, end):
  for i in range(start, end+1, 1):
    l.pop(start)
  return l


# Find all parantheses and calculate their value
def findParantheses():
  global expr
  for i in range(len(expr)):
    # Start parantheses
    if (expr[i] == '('):
      beginPar = i
      endPar = i
      while (expr[endPar] != ')'):
        endPar += 1 
      # Switch parantheses with value
      calculatedPar = calculateByOrder(expr[beginPar+1:endPar])
      expr = removeIndexes(expr, beginPar, endPar)
      expr.insert(beginPar, calculatedPar[0])

      print(expr)
      return

# Calculate Single Operator By Order
def calculateSingular(l):
  for i in range(len(l)): # ^
    if (isNumber(l[i])):
      l[i] = float(l[i])

    if (l[i] == "^"):
      l[i-1] = l[i-1]**float(l[i+1])
      l = removeIndexes(l, i, i+1)
      return l
  for i in range(len(l)): # /*
    if (l[i] == "/"):
      l[i-1] = l[i-1] / float(l[i+1])
      l = removeIndexes(l, i, i+1)
      return l
    if (l[i] == "*"):
      l[i-1] = l[i-1] * float(l[i+1])
      l = removeIndexes(l, i, i+1)
      return l
  for i in range(len(l)): # +-
    if (l[i] == "+"):
      l[i-1] = l[i-1] + float(l[i+1])
      l = removeIndexes(l, i, i+1)
      return l
    if (l[i] == "-"):
      l[i-1] = l[i-1] - float(l[i+1])
      l = removeIndexes(l, i, i+1)
      return l
  return l

# Loop Calculation on Every Operator
def calculateByOrder(l):
  while (len(l) > 2):
    l = calculateSingular(l)
  return l

def run():
    global expr
    while ("(" in expr): 
        findParantheses()
    expr = calculateByOrder(expr)
    return expr


result = run()[0]
print(result)