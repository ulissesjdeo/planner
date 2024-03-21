from os import system as command, name as OS 
from datetime import datetime
from math import ceil, floor
from config import *


# Function to write the "table" in the screen
def line(content):
    start_middle = separator + ' ' * spaces + content + ' ' * spaces
    spaces_to_add = max(0, len(separator_line) - len(start_middle))
    line = start_middle + ' ' * (spaces_to_add - 1) + separator
    print(line)


# Days remaining to the exam
days_remaining = abs((datetime.strptime(EXAM['date'], '%d/%m/%Y') - datetime.now()).days) - 1

# Clear the terminal if wanted
if CLEAR_TERMINAL: command('cls' if OS == 'nt' else 'clear')

# Some vars
if ROUND:
	weeks = floor(days_remaining / 7)
	months = floor(days_remaining / 30)
else:
	weeks = days_remaining / 7
	months = days_remaining / 30

# Print header
print(separator_line)
line('')
line(f'{days_remaining} days to {EXAM["name"]} exam ({weeks} weeks or {months} months)')
line('')
print(separator_line)

# Print body
for study in STUDIES:
	if ROUND:
		pages = ceil((study["total"] - study["done"]) / days_remaining)
		pages_early = ceil((study["total"] - study["done"]) / (days_remaining - EXAM['days_before_goal']))
	else:
		pages = (study["total"] - study["done"]) / days_remaining
		pages_early = (study["total"] - study["done"]) / (days_remaining - EXAM['days_before_goal'])

	line('')
	line(f'{study["title"]}')
	line('')
	line(f'{study["done"]} of {study["total"]}, means {pages} {study["type"]} per day or')
	line(f'{pages_early} {study["type"]} per day to end {EXAM['days_before_goal']} days before exam')
	line('')
	print(separator_line)
