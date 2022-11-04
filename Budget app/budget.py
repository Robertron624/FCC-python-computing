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

    balance = property(get_balance)

    def deposit(self, amount, description=""):
        amountToAdd = {"amount": amount, "description": description}
        self.ledger.append(amountToAdd)

    def check_funds(self, amount) -> bool:
        current_balance = self.get_balance()
        if amount < current_balance:
            return True
        return False

    def withdraw(self, amount, description) -> bool:
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
    title = "Percentage spent by category"

    total_expenses = []

    for categorie in categories:
        category_name = categorie.get_category_name()
        category_ledger = categorie.get_ledger()
        category_expenses = 0

        for transaction in category_ledger:
            if transaction["amount"] < 0:
                category_expenses += abs(transaction["amount"])

        total_expenses.append(
            {"category_name": category_name, "expenses": category_expenses})

    return total_expenses


x = Category("ropa")

x.deposit(200, "new pants")

x.deposit(400, "new shirts")

x.deposit(500, "skirts")

print(x.withdraw(200, "gonna buy merch"))
print(x.withdraw(570, "gonna buy merch"))

print(x.get_balance())


y = Category("ropa")

y.deposit(230, "new pants")

y.deposit(450, "new shirts")

y.deposit(1000, "skirts")

print(y.withdraw(325, "gonna buy merch"))
print(y.withdraw(600, "gonna buy merch"))


print(create_spend_chart([x, y]))
