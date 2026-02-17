class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def transfer(self, amount, category_instance):
        if self.withdraw(amount, f"Transfer to {category_instance.name}"):
            category_instance.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        output = self.name.center(30, "*") + "\n"
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:>7.2f}"
            output += f"{desc:<23}{amt}\n"
        output += f"Total: {self.get_balance()}"
        return output

def create_spend_chart(categories):
    res = "Percentage spent by category\n"
    spend_money = []
    for category in categories:
        withdrawals = sum(item['amount'] for item in category.ledger if item['amount'] < 0)
        spend_money.append(abs(withdrawals))

    total_spent = sum(spend_money)
    percentages = []
    for amount in spend_money:
        if total_spent == 0:
            percentages.append(0)
        else:
            percentages.append(int((amount / total_spent) * 100 // 10) * 10)

    for i in range(100, -1, -10):
        res += f"{i:>3}| "
        for p in percentages:
            if p >= i:
                res += "o  "
            else:
                res += "   "
        res += "\n"

    res += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        res += "     "
        for category in categories:
            if i < len(category.name):
                res += category.name[i] + "  "
            else:
                res += "   "
        if i < max_len - 1:
            res += "\n"

    return res
