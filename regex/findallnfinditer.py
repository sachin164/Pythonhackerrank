# # Enter your code here. Read input from STDIN. Print output to STDOUT
# Task
# You are given a string . It consists of alphanumeric characters, spaces and symbols(+,-).
# Your task is to find all the substrings of that contains or more vowels.
# Also, these substrings must lie in between

# consonants and should contain vowels only.

# Note :
# Vowels are defined as: AEIOU and aeiou.
# Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

# Input Format

# A single line of input containing string

# .

# Constraints

# Output Format

# Print the matched substrings in their order of occurrence on separate lines.
# If no match is found, print -1.

# Sample Input

# rabcdeefgyYhFjkIoomnpOeorteeeeet

# Sample Output

# ee
# Ioo
# Oeo
# eeeee

# Explanation

# ee is located between consonant
# and .
# Ioo is located between consonant and .
# Oeo is located between consonant and .
# eeeee is located between consonant and . 

import re


def solve(S):
    vowel = '[aeiou]'
    consonant = '[qwrtypsdfghjklzxcvbnm]'
    return re.findall(r'{consonant}({vowel}{{2,}})(?={consonant})'.format(vowel=vowel, consonant=consonant), S, re.IGNORECASE)


def main():
    S = input()

    solution = solve(S)
    if solution:
        print(*solution, sep='\n')
    else:
        print(-1)


if __name__ == '__main__':