def arithmetic_arranger(problems, showResult=False):

    formated_string = ""

    if(len(problems) > 5):
        return "Error: Too many problems"

    for problem in problems:
        splited_problem = problem.split()
        first_number, second_number = splited_problem[0], splited_problem[2]
        operator = splited_problem[1]

        try:
            int(first_number)
            int(second_number)
        except:
            return "Error: Numbers must only contain digits"

        if operator != "+" and operator != "-":
            return(f"Error: Operator must be '+' or '-', got: {operator}")

        operator = operator[0]

        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits"

        separator_number = max([len(first_number), len(second_number)]) + 2
        third_line = ("-" * separator_number)
        first_line = f"{' '* (separator_number - len(first_number))}{first_number}"
        second_line = f"{operator}{' ' * (((separator_number - len(second_number)))-1)}{second_number}"

        if showResult:
            result = 0
            if operator == "+":
                result = int(first_number) + int(second_number)
            else:
                result = int(first_number) - int(second_number)

            fourth_line = f"{' ' * (((separator_number - len(second_number)))-1)}{result}"
            operation_to_add = f"{first_line}\n{second_line}\n{third_line}\n{fourth_line}\n"
            formated_string += operation_to_add
        else:
            operation_to_add = f"{first_line}\n{second_line}\n{third_line}\n"
            formated_string += operation_to_add

    return formated_string


# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(
    ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
