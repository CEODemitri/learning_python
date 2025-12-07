read = open("questions.txt", "r")
questions = [line.strip() for line in read]
read.close()

# print(questions)
# successfully pull each line as item in a list

score = 0
total = len(questions)

for line in questions:
    q, a = line.split("=")

    # print the answer and wait user input for answer
    ans = input(f"{q}=")

    if a == ans:
        score += 1

result = open("result.txt", "w")
result.write(f"Your score is now {score}/{total}")
result.close()

# FOR THE COORECT ANSWER< MUST USE A SPACE BEFORE ADDING ANSWER
# line is a string AND by default input is a string so no need to convert