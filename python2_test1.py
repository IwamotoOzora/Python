def calc_time(speed, distance):
    time = distance / speed
    return time

print("速度を入力してください")
speed = float(input())
print("距離を入力してください")
distance = float(input())

print("時間:" + str(calc_time(speed,distance)))