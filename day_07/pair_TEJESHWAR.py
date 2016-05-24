from math import floor

denominations = [(.01, "penny"),
                 (.05, "nickel"),
                 (.10, "dime"),
                 (.25, "quarter"),
                 (1, "dollar bill"),
                 (5, "five dollar bill"),
                 (10, "ten dollar bill"),
                 (20, "twenty dollar bill")]





currency_dict=dict(denominations)
denom_list =currency_dict.keys()
denom_list.sort(reverse=True)
print denom_list

def calculateChange(due, cash_received):
    balance=cash_received-due
    for i in denom_list:
        if balance>=0.001:
            denomination = floor(balance/i)
            tuple_denom=(i,denomination)
            balance=balance-i*denomination
            print denomination , currency_dict.get(i)


if __name__ == "__main__":
    calculateChange(14.27, 20)
