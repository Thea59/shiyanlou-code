a=0
while a<=99:
	a+=1
	if a%7==0 or a%10==7 or a//10==7: ##分别排除7的倍数（除以7余数为0的数）、个位为7（除以10余7的数）、十位为7（除以10取整数为7的数，向下取整）
		continue
	else:
		print(a)
