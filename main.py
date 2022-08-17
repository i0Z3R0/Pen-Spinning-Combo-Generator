import random

print('Generating...')

f = open('tricks.txt', 'r')
lines = f.readlines()

tricks = []

for line in lines:
    name, starts, ends = line.strip().split(',')
    tricks.append([name, starts, ends])

print(tricks)