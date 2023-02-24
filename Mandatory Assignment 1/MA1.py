"""
Solutions to module 1
Student: Victor Wong
Mail: victor.wong.8183@student.uu.se
Reviewed by: Tom Smedsaas
Reviewed date: 29 augusti 2022
"""
import random
import time


def power(x, n):  # Optional
    if n < 0:
        return 1 / power(x, -n)
    elif n == 0:
        return 1
    else:
        return x * power(x, n - 1)


def multiply(m, n):  # Compulsory
    # Basfallen
    if n == 0 or m == 0:
        return 0
    elif n == 1:
        return m
    elif m == 1:
        return n

    # Ta m (funkar med n också) och addera till produkten av m och n-1
    else:
        return m + multiply(m, n - 1)


def divide(t, n):  # Optional
    if t == n:
        return 1
    elif t < n:
        return 0
    else:
        return 1 + divide(t - n, n)


def harmonic(n):  # Compulsory
    # Basfall: n == 1 -> 1/1==1
    if n == 1:
        return 1
    else:
        return 1.0 / n + harmonic(n - 1)


def digit_sum(x):  # Optional
    if x < 10:
        return x
    else:
        return int(str(x)[0]) + digit_sum(int(str(x)[1:]))


def get_binary(x):  # Optional
    if x == 0:
        return ""


def reverse(s):  # Optional
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])


# Minimera kopierandet av listor
def largest(a):  # Compulsory

    # Basfall listan har 1 element, returnera det elementet
    if len(a) == 1:
        return a[0]
    else:
        # Om första elementet är mindre än det andra så kollar vi endast på element 2 och framåt
        if a[0] < a[1]:
            return largest(a[1:])
        # Om det första elementet är störe än det andra så kollar vi på alla element utom det andra
        else:
            return largest([a[0]] + a[2:])


def count(x, s):  # Compulsory
    # Basfall: Tom lista, returnera 0
    if len(s) == 0:
        return 0

    # Om x, det vi söker efter, inte är en lista
    if type(x) != list:

        # Om första elementet i listan är en lista
        if type(s[0]) == list:

            # Sök igenom listan i listan som har index 0 och sök resten av överta listan
            return count(x, s[0]) + count(x, s[1:])

        # Om första elementet är det vi söker efter
        elif s[0] == x:

            # Returnera 1 + sök genom resten av listan
            return 1 + count(x, s[1:])

        # Om första elementet inte är det vi söker efter
        else:

            # Retuerna resultatet av att söka genom resten av listan
            return count(x, s[1:])

    # Om vi söker efter en lista i listan
    else:
        # Om första elementet är listan vi söker efter i listan
        if type(s[0]) == list and s[0] == x:

            # Returnera 1+ resultatet av sökning genom resten av listan
            return 1 + count(x, s[1:])
        else:

            # Om det inte är listan vi söker efter returnera resultatet av att söka genom resten av listan
            return count(x, s[1:])


def zippa(l1, l2):  # Compulsory
    # Basfall: en lista är tom, returnera den andra listan då
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1

    # Returnera en lista av de första två elementen och kalla funktionen på resterande elementen i listorna
    else:
        return [l1[0], l2[0]] + zippa(l1[1:], l2[1:])


def bricklek(f, t, h, n):  # Compulsory
    if n == 0:
        return []
    else:
        return (
            bricklek(f, h, t, n - 1)  # Flytta de n-1 översta brickorna til lh
            + [f + "->" + t]  # Flytta den kvarvarande från f till t
            + bricklek(h, t, f, n - 1)  # Flytta de n-1 brickorna på h till t
        )


def main():
    """Demonstates my implementations"""
    # Write your demonstration code here


if __name__ == "__main__":
    main()

####################################################

"""
Answers to the none-coding tasks
================================


Exercise 16: Time for bricklek with 50 bricks:
t(n) = 2^n -1
t(50) = 2^50 - 1
t(50) ≈ 1.126*10^15 sekunder
1.126*10^15 ≈ 36 miljoner år
  
  
  
  


Exercise 17: Time for Fibonacci: 
a)



def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# sizes = [30, 31, 32, 33]
sizes = [35, 36, 37]
for i, n in enumerate(sizes):
    tstart = time.perf_counter()
    fib(n)
    tstop = time.perf_counter()
    print(f"Measured time for {n}: {tstop - tstart} seconds")
    if i != 0:
        print(f"Measured time divided by 1.618: {(tstop - tstart)/1.618}\n\n")

Exercise 17: Time for Fibonacci: 
b)  
t(n) för fib(n) när n = 50:
t(50) = 1.618^50
t(50) = 28114208661.7 sekunder
28114208661.7 sekunder ≈ 890 år

t(n) för fib(n) när n = 100:
t(100) = 1.618^100
t(100) = 7.9040873e+20 sekunder
7.9040873e+20 sekunder ≈ 25*10^12 år




Exercise 20: Comparison sorting methods:
Instickssortering är O(n^2)
mergesort är O(n*log(n))

10^6 tal med instickssortering:
    t(10^6) ≈ (10^6)^2 = 10^12 sekunder
    10^12 sekunder ≈ 32000 år

10^6 tal med mergesort:
    t(10^6) ≈ 10^6 * log(10^6) = 6*10^6 sekunder
    6*10^6 sekunder ≈ 69 dagar


10^9 tal med instickssortering:
    t(10^9) ≈ (10^9)^2 = 10^18 sekunder
    10^18 sekunder ≈ 320 miljarder år

10^9 tal med mergesort:
    t(10^9) ≈ 10^9 * log(10^9) = 9*10^9 sekunder
    9*10^9 sekunder ≈ 290 år






Exercise 21: Comparison Theta(n) and Theta(n log n)

A löser ett problem på storlek n på n sekunder --> Theta(n)
B löser samma problem på c*n*log(n) sekunder Testkörningen visar att det tar 1 sekund
för B att lösa problemet när n = 10

Vi har:
t_B(n) = c*n*log(n)

Om n = 10:
t_B(10) = c*10*log(10)
c = 1/(10*log(10))
c = 1/10
c = 0.1

Vi vill veta när t_A(n) < t_B(n)
n < 0.1*n*log(n)
Vilket ger att n > 10^10
  

  
  
  

"""
