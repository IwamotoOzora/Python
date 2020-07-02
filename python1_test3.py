print("体重を入力してください")
weight = float(input())
print("身長を入力してください")
height = float(input()) / 100

BMI = weight / height ** 2

if BMI < 18.5:
    message = "やせ"
if 18.5 <= BMI < 25:
    message = "標準"
if 25 <= BMI < 30:
    message = "肥満"
if BMI > 30:
    message = "高度肥満"
print("あなたは" + "「" + message + "」" + "です。") 