def arithmetic_arranger(problems, showResult=False):

    formatted_operations = ""

    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""

    if(len(problems) > 5):
        return "Error: Too many problems."

    for index, problem in enumerate(problems):
        splited_problem = problem.split()
        first_number, second_number = splited_problem[0], splited_problem[2]
        operator = splited_problem[1]
        # print(len(problems))

        try:
            int(first_number)
            int(second_number)
        except:
            return "Error: Numbers must only contain digits."

        if operator != "+" and operator != "-":
            return(f"Error: Operator must be '+' or '-'.")

        operator = operator[0]

        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

        separator_number = max([len(first_number), len(second_number)]) + 2
        if index + 1 < len(problems):
            third_line += ("-" * separator_number) + "    "
            first_line += f"{' '* (separator_number - len(first_number))}{first_number}    "
            second_line += f"{operator}{' ' * (((separator_number - len(second_number)))-1)}{second_number}    "
        else:
            third_line += ("-" * separator_number)
            first_line += f"{' '* (separator_number - len(first_number))}{first_number}"
            second_line += f"{operator}{' ' * (((separator_number - len(second_number)))-1)}{second_number}"

        formatted_operations = f"{first_line}\n{second_line}\n{third_line}"

        if showResult:
            mayor = max([len(first_number), len(second_number)])
            result = 0
            if operator == "+":
                result = int(first_number) + int(second_number)
            else:
                result = int(first_number) - int(second_number)

            if index + 1 < len(problems):
                if result < 0:
                    fourth_line += f"{' ' * (((separator_number - mayor))-1)}{result}    "
                else:
                    fourth_line += f"{' ' * ((separator_number - mayor))}{result}    "
            else:
                if result < 0:
                    fourth_line += f"{' ' * (((separator_number - mayor))-1)}{result}"
                else:
                    fourth_line += f"{' ' * ((separator_number - mayor)-1)}{result}"
            formatted_operations += f"\n{fourth_line}"

    return formatted_operations


# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(
#     ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

# print(arithmetic_arranger(["3801 - 2", "123 + 49"]))

# print(arithmetic_arranger(['3 + 855', '988 + 40'], True))

# print(arithmetic_arranger(['32 - 698', '1 - 3801',
#       '45 + 43', '123 + 49', '988 + 40'], True))
