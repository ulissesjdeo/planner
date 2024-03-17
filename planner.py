from os import system as command, name as OS 
from datetime import datetime
from math import ceil, floor
from config import *


# Function to write the "table" in the screen
def linify(content):
    start_middle = separator + ' ' * spaces + content + ' ' * spaces
    spaces_to_add = max(0, len(separator) - len(start_middle))
    line = start_middle + ' ' * (spaces_to_add - 1) + separator
    print(line)


# Days remaining to the exam
days_remaining = abs((datetime.strptime(EXAM['date'], '%d/%m/%Y') - datetime.now()).days) - 1

# Clear the terminal if wanted
if CLEAR_TERMINAL: command('cls' if OS == 'nt' else 'clear')

# Print header
print(separator)
linify('')
linify(f'{days_remaining} days to {EXAM["name"]} exam ({floor(days_remaining / 7)} weeks or {floor(days_remaining / 30)} months)')
linify('')
print(separator)

# Print body
for study in STUDIES:
	linify('')
	linify(f'{study["title"]}')
	linify('')
	linify(f'{study["done"]} of {study["total"]}, means {ceil((study["total"] - study["done"]) / days_remaining)} {study["name"]} per day or')
	linify(f'{ceil((study["total"] - study["done"]) / (days_remaining - EXAM['days_before_goal']))} {study["name"]} per day to end {EXAM['days_before_goal']} days before exam')
	linify('')
	print(separator)
