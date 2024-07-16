# This program is going to provide 10 separate simple math problems to be solved by the user
# If the user does not get any of the question of the question correct he will be prompted to answer it again until it is got right
# At the end of the program the user will shown the time spent in answering the question in seconds
import random
import time

# Constant variable
OPERATORS = ["+", "-", "*"]
MIN_VALUE = 2
MAX_VALUE = 10
NUMBER_OF_QUESTIONS = 10
# define function for calculation
def get_calc():
    left = random.randint(MIN_VALUE,MAX_VALUE)
    right = random.randint(MIN_VALUE,MAX_VALUE)
    operator = random.choice(OPERATORS)

    expr = f"{left} {operator} {right}"
    answer = eval(expr)
    
    return expr, answer
        

# loop through to get the questions
start_time = time.time()
for i in range(NUMBER_OF_QUESTIONS):
    expr, answer = get_calc()

    while True:
        your_answer = input(f"Q.{i+1}) {expr} = ")
        if your_answer == str(answer):
            break
        else:
            print("wrong answer")
end_time = time.time()

total_time = round((end_time - start_time), 2)

print(f"You finished in {total_time} seconds")