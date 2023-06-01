driving = input('請問你有沒有開過車？')
if driving != '有' and driving != '沒有':
	print('請輸入有或沒有')
	raise systemExit

age = int(input('請問你的年齡？'))
if driving == '有':
	if age >= 18:
		print('pass')
	else:
		print('你怎麼會開過車')
elif driving == '沒有':
	if age >= 18:
		print('可以開車了')
	else:
		print('可以再等等')
else:
	print('請輸入合乎邏輯的答案')