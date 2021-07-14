# 猜數字遊戲

import random

s = int(input('設定猜數字範圍的起始: '))
e = int(input('設定猜數字範圍的結束: '))
target = random.randint(s, e)
times = 0

while True:
	print('猜', s, '到', e, '的數字,按101離開: ')
	guess = int(input('請輸入: '))
	times += 1 
	if guess == target:
		print('終於猜對了！你總共猜了', times,'次')
		break
	elif guess == 101:
		print('你才嘗試', times-1, '次', '答案是: ', target, '下次再加油囉！')
		break
	elif guess != target:
		if guess > target:
			print('你猜得比目標大')
		elif guess < target:
			print('你猜得比目標小')
	print('這是你猜的第', times,'次')