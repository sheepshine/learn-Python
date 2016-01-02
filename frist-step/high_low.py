#猜数字游戏
import random
number=random.randint(1,100) 
guess=-1
print("Guess the number")
while guess!=number:
	guess =int(input("It is ..."))

	if guess==number:
		print("Hooray! You guessed it right!")
	elif guess<number:
		print("It's bigger...")
	elif guess>number:
		print("It's not so big.")