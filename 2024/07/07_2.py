from itertools import product

# def check_combinations(nums, target):
#     if not nums or len(nums) < 2:
#         return False  # At least two numbers are required

#     n = len(nums)
#     operators = ['+', '*']
#     all_combinations = product(operators, repeat=n-1)
    
#     for ops in all_combinations:
#         expression = str(nums[0])  # Start with the first number
#         for i, op in enumerate(ops):
#             expression += f" {op} {nums[i+1]}"
#         # Evaluate the expression and compare with target
#         if int(eval(expression)) == int(target):
#             return True, expression  # Return True and the matching expression
#     return False, None  # No combination matched the target

def left_to_right_evaluation(nums, target):
    if not nums or len(nums) < 2:
        return False, None  # At least two numbers are required

    n = len(nums)
    operators = ['+', '*', 'X']
    all_combinations = product(operators, repeat=n-1)
    
    for ops in all_combinations:
        # Perform left-to-right evaluation
        result = nums[0]  # Start with the first number
        expression = str(nums[0])  # Build the expression string
        for i, op in enumerate(ops):
            if op == '+':
                result += nums[i+1]
            elif op == '*':
                result *= nums[i+1]
            elif op == 'X':
                result = int(str(result) + str(nums[i+1]))
            expression += f" {op} {nums[i+1]}"
            #print(f"Expression: {expression} = {result}")
        
        # Compare with the target
        if result == int(target):
            return True, expression  # Return True and the matching expression
    return False, None  # No combination matched the target

with open('2024/07/input.txt', 'r') as file:
    lines = file.read().splitlines()

true_statements = []
all_len = []
for line in lines:
    outcome = line.split(': ')[0]
    numbers = line.split(': ')[1].split(' ')

    # make sure all numbers are integers
    numbers = [int(num) for num in numbers]

    amount_of_numbers = len(numbers)

    result, expression = left_to_right_evaluation(numbers, outcome)
    if result:
        print(f"Found a match: {expression} = {outcome}")
        true_statements.append(outcome)
    else:
        print("No combination found.")

# make sure all true_statements are integers
true_statements = [int(statement) for statement in true_statements]
# get the sum of all numbers in true_statements
print(sum(true_statements))




        # else:
        #     for i in range(amount_of_numbers):
        #         if i == 0:
        #             interims_result = int(numbers[i])
        #         elif interims_result <= outcome:
        #             interims_result *= int(numbers[i])

        #         if interims_result == outcome and i == amount_of_numbers - 1:
        #             true_statements.append(outcome)
        #             break
    #all_len.append(amount_of_numbers)

#get max of all_len
#print(true_statements)
