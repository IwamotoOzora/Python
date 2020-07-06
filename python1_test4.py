debt = 250000
repayment = 30000
rate = 14
month = 0

while debt > repayment:
    debt = debt * (1 + rate / 12 / 100) - repayment
    month += 1
    print(str(month) + "ヶ月目:返済額=" + str(repayment) +"円,"\
    + "残り" + str(debt) + "円")
debt = debt * (1 + rate / 12 / 100)
month += 1
print(str(month) + "ヶ月目:返済額=" + str(debt) + "円," + "返済完了。")

