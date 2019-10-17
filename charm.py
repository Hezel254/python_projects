import random


class Dice:
	def roll():
		first= random.randint(1,6)
		second= random.randint(1,6)
		return first, second


dice= Dice
print(dice.roll())
