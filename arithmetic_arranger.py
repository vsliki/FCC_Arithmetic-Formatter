def arithmetic_arranger(problems, arg=False):
  #New empty matrices
  sign = ['+', '-']
  prob = []
  op = []
  firstLine = []
  secondLine = []
  sol = []
  arr_first = ""
  arr_second = ""
  aff = ""
  arr_sol = ""

  #Error for prob too long: OK
  if len(problems) > 5:
    solution = "Error: Too many problems."
    return solution

  #Separate problems into 1st dig, op, 2nd dig
  for problem in problems:
    prob.append(problem.split())
  #print(prob)

# ----------------- OPERATORS-------------
#Separate operations
  for operation in prob:
    op.append(operation[1])

  #Error for operator not + or -:
  for i in op:
    if i not in sign:
      return "Error: Operator must be '+' or '-'."
# -------------------------------------

# ----------------- 1st & 2nd LINES -------------
#Separate each line
  for digit in prob:
    firstLine.append(digit[0])
    secondLine.append(digit[2])
  #print(firstLine)
  #print(secondLine)

  #Errors in digits and length
  for j in firstLine:
    if not j.isdigit():
      return "Error: Numbers must only contain digits."
    elif len(j) > 4:
      return "Error: Numbers cannot be more than four digits."

  for k in secondLine:
    if not k.isdigit():
      return "Error: Numbers must only contain digits."
    elif len(k) > 4:
      return "Error: Numbers cannot be more than four digits."
# -------------------------------------

# ---------- COMPUTING SOLUTIONS -------------
  for l in range(len(firstLine)):
    if op[l] == sign[0]:
      sol.append(int(firstLine[l]) + int(secondLine[l]))
    else:
      sol.append(int(firstLine[l]) - int(secondLine[l]))
  #if arg == True:
  #print(sol)


# -------------------------------------

# -------------- PRINTING -----------------------

  for m in range(len(firstLine)):
    lenmax = max(len(firstLine[m]), len(secondLine[m]))
    #print(lenmax)

    arr_first = arr_first + f"{firstLine[m].rjust(lenmax+2)}    "
    arr_second = arr_second + f"{op[m]}{secondLine[m].rjust(lenmax+1)}    "
    aff = aff + f"--{'-' * (lenmax)}    "

    arr_sol = arr_sol + f"{str(sol[m]).rjust(lenmax+2)}    "

  #print(arr_first)
  #print(arr_second)
  #print(aff)

  if arg == True:
    arranged_problems = arr_first + "\n" + arr_second + "\n" + aff + "\n" + arr_sol
  else:
    arranged_problems = arr_first + "\n" + arr_second + "\n" + aff

  return arranged_problems
