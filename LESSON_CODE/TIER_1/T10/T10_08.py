from collections import UserList

class AmountPaymentList(UserList):
    def amount_payment(self):
        total = 0
        for value in self.data:
            if value > 0:
                total += value
        return total

# Example usage:
payment = AmountPaymentList([1, -3, 4])
print(payment.amount_payment())  # Output: 5

            