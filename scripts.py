
"""
Algorithmic Methods of Data Mining - Homework 1
Autore: <Francesco Lugliè>

Soluzioni delle sfide HackerRank svolte. Ogni sezione riporta il nome della
sfida e il codice consegnato su HackerRank.
Nota: il file raccoglie le soluzioni, quindi non va eseguito tutto in una
volta (ogni esercizio legge i suoi dati con input()).
"""


# =============================================================================
# PROBLEM 1 - Python challenges
# =============================================================================


# -----------------------------------------------------------------------------
# Introduction
# https://www.hackerrank.com/domains/python/py-introduction
# -----------------------------------------------------------------------------

# --- Introduction: Say "Hello, World!" With Python ---
print("Hello, World!")


# --- Introduction: Python If-Else ---
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1:
        print("Weird")
    elif n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")


# --- Introduction: Arithmetic Operators ---
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    sum = (a + b)
    dif = (a - b)
    product = (a * b)
    print(sum)
    print(dif)
    print(product)


# --- Introduction: Python: Division ---
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)


# --- Introduction: Loops ---
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i ** 2)


# --- Introduction: Write a function (leap year) ---
def is_leap(year):
    leap = True

    # Write your logic here
    if year % 400 == 0:
        return (True)
    elif year % 100 == 0:
        return (False)
    elif year % 4 == 0:
        return leap
    else:
        return (False)

year = int(input())
print(is_leap(year))


# --- Introduction: Print Function ---
if __name__ == '__main__':
    n = int(input())
    for k in range(1, n + 1):
        print(k, end="")


# -----------------------------------------------------------------------------
# Data types
# https://www.hackerrank.com/domains/python/py-basic-data-types
# -----------------------------------------------------------------------------

# --- Data types: List Comprehensions ---
x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n])


# --- Data types: Find the Runner-Up Score! ---
n = int(input())
A = [int(numero) for numero in input().split()]

massimo = max(A)
B = [numero for numero in A if numero != massimo]

print(max(B))


# --- Data types: Nested Lists ---
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # voti distinti in ordine crescente
    voti = sorted(set(s[1] for s in students))
    secondo_minimo = voti[1]

    # nomi con il secondo voto più basso, in ordine alfabetico
    nomi = sorted(s[0] for s in students if s[1] == secondo_minimo)

    for nome in nomi:
        print(nome)


# --- Data types: Finding the percentage ---
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    voti = student_marks[query_name]
    media = sum(voti) / len(voti)
    print(f"{media:.2f}")


# --- Data types: Lists ---
if __name__ == '__main__':
    N = int(input())
    lista = []
    for _ in range(N):
        comando, *args = input().split()
        if comando == "insert":
            lista.insert(int(args[0]), int(args[1]))
        elif comando == "print":
            print(lista)
        elif comando == "remove":
            lista.remove(int(args[0]))
        elif comando == "append":
            lista.append(int(args[0]))
        elif comando == "sort":
            lista.sort()
        elif comando == "pop":
            lista.pop()
        elif comando == "reverse":
            lista.reverse()


# --- Data types: Tuples ---
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))


# --- Strings: Mutations ---
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# --- Strings: String Validators ---
if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))


# --- Strings: Text Wrap ---
import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# -----------------------------------------------------------------------------
# Strings
# https://www.hackerrank.com/domains/python/py-strings
# -----------------------------------------------------------------------------

# --- Strings: String Split and Join ---
def split_and_join(line):
    # write your code here
    result = line.split(" ")
    result = "-".join(result)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# --- Strings: What's Your Name? ---
def print_full_name(first, last):
    # Write your code here
    print("Hello " + first + " " + last + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# --- Strings: sWAP cASE ---
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# --- Strings: Find a string ---
def count_substring(string, sub_string):
    conta = 0
    k = len(sub_string)
    for i in range(len(string)):
        if string[i : i + k] == sub_string:
            conta = conta + 1
    return conta

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


# =============================================================================
# PROBLEM 2 - Algorithms
# =============================================================================

# --- Birthday Cake Candles ---
# https://www.hackerrank.com/challenges/birthday-cake-candles
import sys


def birthdayCakeCandles(candles):
    # Trova l'altezza massima e conta quante candele la raggiungono
    massimo = max(candles)
    return candles.count(massimo)


if __name__ == '__main__':
    n = int(input().strip())
    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)
    print(result)
