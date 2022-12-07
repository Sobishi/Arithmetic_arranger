import re

def arithmetic_arranger(problems, solve = False):

    if len(problems) > 5:
        return "Error: Too many problems"

    firstplace = ""
    secondplace = ""
    lines = ""
    sumrange = ""
    string = ""
    for problem in problems:
        if (re.search("[^\s0-9.+-]",problem)):
            return "Error: Number must only contain digits."
        if (re.search("[/]", problem) or re.search("[*]", problem)):
            return "Error: Operator must be '+' or '-'."

        firstcase = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        secondcase = problem.split(" ")[2]

        if len(firstcase) >= 5 or len(secondcase) >= 5:
            return "Error: Numbers cannot be more than four digits."

        sum = ""
        if operator == "+":
            sum = str(int(firstcase) + int(secondcase))
        elif operator == "-":
            sum = str(int(firstcase) - int(secondcase))

        lengthcase = max(len(firstcase), len(secondcase)) + 2
        topcase = str(firstcase).rjust(lengthcase)
        bottomcase = operator + str(secondcase).rjust(lengthcase - 1)
        line = ""
        sol = str(sum).rjust(lengthcase)
        for i in range(lengthcase):
            line += "-"

        if problem != problems[-1]:
            firstplace += topcase + '    '
            secondplace += bottomcase + '    '
            lines += line + '    '
            sumrange += sol + '    '

        else:
            firstplace += topcase
            secondplace += bottomcase
            lines += line
            sumrange += sol

    if solve:
        string = firstplace + "\n" + secondplace + "\n" + lines + "\n" + sumrange
    else:
        string = firstplace + "\n" + secondplace + "\n" + lines
    return string

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
