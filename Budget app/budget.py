class Category:

    def __init__(self, category_name) -> None:
        self.category_name = category_name
        self.ledger = []

    def __str__(self) -> str:
        name = self.get_category_name()
        ledger = self.get_ledger()

        astherics = "*" * int((30 - len(name))/2)
        title = f"{astherics}{name}{astherics}"
        total = f"Total: {self.get_balance()}"
        transactions = ""

        for index, elem in enumerate(ledger):
            description = elem["description"]
            amount = f"{elem['amount']:.2f}"
            white_space = " " * (30 - (len(description) + len(amount)))

            if len(description) > 23:  # slice string to contain only first 23 letters
                splicig_number = slice(23 - len(description))
                description = description[splicig_number] + " "

            transactions += f"{description}{white_space}{amount}"

            # Add new line unless it's the last operation
            if index + 1 < len(ledger):
                transactions += "\n"

        return(f"{title}\n{transactions}\n{total}")

    def get_ledger(self) -> list:
        return self.ledger

    def get_category_name(self) -> str:
        return self.category_name

    def get_balance(self) -> float:
        returnedBalance = 0
        for deposit in self.ledger:
            amount = deposit["amount"]
            returnedBalance += amount
        return returnedBalance

    def get_withdrawals(self):
        withdrawals = 0
        for transaction in self.ledger:
            if transaction["amount"] < 0:
                withdrawals += (transaction["amount"]) * -1
        return withdrawals

    balance = property(get_balance)

    def deposit(self, amount, description=""):
        amountToAdd = {"amount": amount, "description": description}
        self.ledger.append(amountToAdd)

    def check_funds(self, amount) -> bool:
        current_balance = self.get_balance()
        if amount <= current_balance:
            return True
        return False

    def withdraw(self, amount, description="") -> bool:
        enough_money = self.check_funds(amount)
        if enough_money:
            self.ledger.append(
                {"amount": amount * (-1), "description": description})
            return True
        return False

    def transfer(self, amount, destiny_budget_object) -> bool:
        if self.check_funds(amount):
            destiny_category_name = destiny_budget_object.get_category_name()
            destin_ledger = destiny_budget_object.get_ledger()
            print(destin_ledger)
            transfer_to_operation = {
                "amount": amount * (-1), "description": f"Transfer to {destiny_category_name}"}

            transfer_from_operation = {
                "amount": amount, "description": f"Transfer from {self.get_category_name()}"
            }

            destiny_budget_object.get_ledger().append(transfer_from_operation)

            self.get_ledger().append(transfer_to_operation)

            return True
        return False


def create_spend_chart(categories):
    formatted_chart = "Percentage spent by category"
    x = len(categories)
    y = 100

    # calculate total & percentages for each category
    percentages = list()
    total_spent = 0
    for category in categories:
        total_spent += category.get_withdrawals()
    for category in categories:
        raw = category.get_withdrawals() / total_spent
        percentages.append(int((raw // .1) * 10))

    while y >= 0:
        formatted_chart += "\n"
        # input the correct right aligned Y axis value
        formatted_chart += str(y) + "| " if y == 100 else " " + str(y) + \
            "| " if y < 100 and y > 0 else "  0| "

        # loop through each category column and check if a bar value exists
        columns = 0
        while columns < x:
            if percentages[columns] >= y:
                # print(percentages[columns], y)
                formatted_chart += "o  "
            else:
                formatted_chart += " "*3
            columns += 1

        y -= 10

    formatted_chart += "\n" + " "*4 + "-" + "-"*x*3

    # label x access using double loop for names
    max_name_length = 0
    for category in categories:
        if len(category.category_name) > max_name_length:
            max_name_length = len(category.category_name)

    z = 0
    while z < max_name_length:
        formatted_chart += "\n" + " "*5
        for category in categories:
            try:
                formatted_chart += category.category_name[z] + " "*2
            except:
                formatted_chart += " "*3

        z += 1

    return formatted_chart


x = Category("ropa")

x.deposit(200, "new pants")

x.deposit(400, "new shirts")

x.deposit(500, "skirts")

x.withdraw(200, "gonna buy merch")
x.withdraw(500, "gonna buy merch")

print(x.get_balance())


y = Category("Tecnologia")

y.deposit(1000, "skirts")

y.withdraw(325, "gonna buy merch")
y.withdraw(600, "gonna buy merch")


print(create_spend_chart([x, y]))
