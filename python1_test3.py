print("体重を入力してください")
weight = float(input())
print("身長を入力してください")
height = float(input()) / 100

bmi = weight / height ** 2

if bmi < 18.5:
    message = "やせ"
if bmi >= 18.5 and bmi < 25:
    message = "標準"
if bmi >= 25 and bmi < 30:
    message = "肥満"
if bmi > 30:
    message = "高度肥満"
print("あなたは「{}」です。" .format(message)) 