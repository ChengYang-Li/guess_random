# 猜數字遊戲1-100

import random

target = random.randint(1, 100)
while True:
	guess = int(input("猜1-100的數字，按101離開: "))
	if guess == target:
		print("終於猜對了！")
		break
	elif guess == 101:
		print("下次再加油囉！")
		break
	elif guess != target:
		if guess > target:
			print('你猜得比目標大')
		elif guess < target:
			print('你猜得比目標小')