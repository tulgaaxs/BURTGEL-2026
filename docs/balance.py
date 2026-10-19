def calculate_ending_balance(opening_balance, income, expense):
    if opening_balance < 0 or income < 0 or expense < 0:
        raise ValueError("Error")

    return opening_balance + income - expense
