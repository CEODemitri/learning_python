# for loop
# best for iteration through colelctions
colors = ["red", "yellow", "green"]
for color in colors:
    print("I need a tube of " + color + ".")

# WHAT IS WRONG? WHY A TYPE ERROR 
# for color in colors:
#     new_color = str(color)
#     print("I need a tube of " + new_color + ".")


# USE-CASE :: COUNTER
for number in range(1, 11, 1):
    print(number)

for number in range(20):
    print(number * 2)


#
letters = ['a', 'b', 'c', 'd']
for index, letter in enumerate(letters):
    print(f"At position {index}, I found a {letter}")


# 
# while loop
i = 0
while i <= 11:
    print(i)
    i += 1


p = 10
while p >= 1:
    letter = str(p)
    print("p is " + letter)
    p -= 1

# 
# the loop flow
# 0. initialization
# 1. condition
# 2. execution
# 3. update
# 4. repeat

# 
# when to use each
# for loops :: use loops when you know the number of iterations in advance and want to process each element in a sequence. best suited for iteration over collections and sequences where the length is known.
# 
# while loops :: use while loops when need to perform a task repeatedly as long as a certain condition holds true. while loops are useful in situations where the number of iterations is uncertain or where waiting for a specific condition to be met. 
