# put help statment here

# import for testing
import pytest
# imports for code
import operator

def arithmetic_arranger(problems, solve=False):
  # check if there are "too many problems" supplied to the function
  if len(problems) > 5: 
    return "Error: Too many problems."
  
  processed_problems = {}
  problem_num = 0
  arranged_row_1 = []
  arranged_row_2 = []
  arranged_row_3 = []
  arranged_row_4 = []
  
  # take each problem and break it up into its top, operand, and lower then store all problems together 
  for problem in problems:
    # find what operator the problem uses and if not + or - return error
    if "+" in problem:
      problem_operator = "+"
    elif "-" in problem:
      problem_operator = "-"
    else:
      return "Error: Operator must be '+' or '-'."
    
    # break up problem so have just the numbers then clean
    first_item, second_item = problem.split(problem_operator)
    first_item = first_item.strip()
    second_item = second_item.strip()

    # check if numbers are integers and if they are to long, i.e. to many digits 
    if not first_item.isnumeric() or not second_item.isnumeric():
      return "Error: Numbers must only contain digits."
    if len(first_item) > 4 or len(second_item) > 4:
      return "Error: Numbers cannot be more than four digits."

    # store broken up problem by number (i.e. "problem1"), with each of its constituent parts (i.e. numbers and operators)
    # note that the parts are still strings and are striped of any unnecessary characters 
    problem_num += 1
    problem_name = "problem" + str(problem_num)
    processed_problems[problem_name] = {"top_value": first_item, "operator": problem_operator, "bottom_value": second_item}

  # formating problem
  for problem in processed_problems:
    # find spacing for bottom line between operand and operator by finding length differnce
    if len(processed_problems[problem]["top_value"]) > len(processed_problems[problem]["bottom_value"]):
      bottom_row_spacing = len(processed_problems[problem]["top_value"]) - len(processed_problems[problem]["bottom_value"]) + 1
    else:
      bottom_row_spacing = 1
    # create each problem's full items for each line of the arithmetic format 
    problem_bottom_row = processed_problems[problem]["operator"] + (" " * bottom_row_spacing) + processed_problems[problem]["bottom_value"]
    problem_bottom_line = "-" * len(problem_bottom_row)
    # formating elements for each problem and between
    in_problem_spacing = "{:>" + str(len(problem_bottom_row)) + "}" 
    # build rows by formating in item
    arranged_row_1.append(in_problem_spacing.format(processed_problems[problem]["top_value"]))
    arranged_row_2.append(in_problem_spacing.format(problem_bottom_row))
    arranged_row_3.append(in_problem_spacing.format(problem_bottom_line))

    # solve each problem and format solution row
    if solve == True: 
      # lookup table for operator 
      operator_lookup_table = {"+": operator.add, "-": operator.sub}
      problem_solution = operator_lookup_table[processed_problems[problem]["operator"]](int(processed_problems[problem]["top_value"]), int(processed_problems[problem]["bottom_value"]))
      arranged_row_4.append(in_problem_spacing.format(problem_solution))
  
  # build final return from rows
  between_problem_spacing = " " * 4
  if solve == True:
    arranged_problems = between_problem_spacing.join(arranged_row_1) + "\n" + between_problem_spacing.join(arranged_row_2) + "\n" + between_problem_spacing.join(arranged_row_3) + "\n" + between_problem_spacing.join(arranged_row_4)
  else:
    arranged_problems = between_problem_spacing.join(arranged_row_1) + "\n" + between_problem_spacing.join(arranged_row_2) + "\n" + between_problem_spacing.join(arranged_row_3)
  return arranged_problems
   

if __name__ == "__main__":
  # testing is copied from freeCodeCamp test code for this project
  print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
  pytest.main()
