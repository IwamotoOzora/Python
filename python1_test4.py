debt = 250000
repayment = 30000
rate = (1 + 14 / 12 / 100)
month = 0

while debt > 0:
    debt = debt * rate - repayment
    month += 1
    print(str(month) + "ヶ月目:返済額=" + str(repayment) +"円,"\
    + "残り" + str(debt) + "円")
    if debt < repayment:
          break
print(str(month + 1) + "ヶ月目:返済額=" + str(debt * rate) + "円," + "返済完了。")

