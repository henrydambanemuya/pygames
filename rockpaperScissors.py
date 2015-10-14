#!/usr/bin/env/ python
#Created: 10/14/2015
#Location: Notre Dame, Indiana

import random
import time

rock = 1
paper = 2
scissors = 3

names = { rock: "Rock", paper: "Paper", scissors: "Scissors" }
rules = { rock: scissors, paper: rock, scissors: paper }

player_score = 0
computer_score = 0

def start():
	global human
	print "\n"
	human = raw_input("Please enter your name: ");
	print "\n"
	print "Hi %r, let's play a game of Rock, Paper, Scissors." %human
	while game():
		pass
	scores()

def game():
	player = move()
	computer = random.randint(1,3)
	result(player, computer)
	return play_again()

def move():
	while True:
		print
		player = raw_input("Rock = 1\nPaper = 2\nScissors = 3\n\nMake a move: ")
		try:
			player = int(player)
			if player in (1,2,3):
				return player
		except ValueError:
			pass
		print "\n"
		print "Oops! I didn't understand that. Please enter 1, 2, or 3."

def result(player, computer):
	print "\n"
	print "1..."
	time.sleep(1)
	print "2..."
	time.sleep(1)
	print "3..."
	time.sleep(0.5)
	print "\n"
	print "Computer threw {0}!".format(names[computer])
	global player_score, computer_score
	if player == computer:
		print "\n"
		print "Tie Game"
	else:
		if rules[player] == computer:
			print "\n"
			print "Your victory has been assured."
			player_score += 1
		else:
			print "\n"
			print "The computer laughs as you realize you have been defeated."
			computer_score += 1

def play_again():
	print "\n"
	answer = raw_input("Would you like to play again? Y/N?: ")
	if answer in ("y", "Y", "yes", "Yes", "yeah!", "Yeah!", "Of course!"):
		return answer
	else:
		print "\n"
		print "Thanks for playing :)"

def scores():
	global player_score, computer_score, human
	print "\n"
	print "HIGH SCORES"
	print human, player_score
	print "Computer: ", computer_score
	print "\n"

if __name__ == '__main__':
	start()
