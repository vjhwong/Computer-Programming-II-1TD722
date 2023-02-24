"""
Solutions to module 2 - A calculator
Student: Victor Wong
Mail: victor.wong.8183@student.uu.se
Reviewed by: Maximilian Meyer-Mölleringhof
Reviewed date: 2 september 2022
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from statistics import mean
from tokenize import TokenError
from MA2tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


# Inhertence av Exception klass som ska hantera evalueringsfel
class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


# Funktion som hanterar inmatning av argument till funktioner som tar in n argument
def arglist(wtok, variables):
    if wtok.get_current() == "(":  # Kolla för högerparantes, annars SyntaxError
        wtok.next()
        result = [assignment(wtok, variables)]  # Gör en lista med argumenten
        while (
            wtok.get_current() == "," or wtok.get_current() == ")"
        ):  # Fortsätt ta in argument vid ',' och avlsuta vid ')'
            if wtok.get_current() == ")":
                wtok.next()
            elif wtok.get_current() == ",":
                wtok.next()
                result.append(assignment(wtok, variables))
            else:
                raise SyntaxError("Expected ',' or ')'")
    else:
        raise SyntaxError("Expected '('")

    return result


# Funktioner som ska finnas i miniräknaren
def fib(n):
    if n >= 0 and n.is_integer():  # Argumentet måste vara ett icke-negativt heltal

        def _fib(n, lagrat={0: 0, 1: 1}):  # "Hjälpfunktion med memoization"
            if n not in lagrat:
                lagrat[n] = _fib(n - 1, lagrat) + _fib(n - 2, lagrat)
            return lagrat[n]

        return _fib(n)
    else:
        raise EvaluationError("Argument for fib is {n}. Must be an integer >= 0")


def my_log(n):
    if n > 0:
        return math.log(n)
    else:
        raise EvaluationError("Argument for log is {n}. Must be > 0")


def my_fac(n):
    if n >= 0 and n.is_integer():
        return math.factorial(n)
    else:
        raise EvaluationError("Argument for fac is {n}. Must be an integer >= 0")


# Lexikon med funktioner som ska användas i miniräknaren
function_1 = {
    "sin": math.sin,
    "cos": math.cos,
    "exp": math.exp,
    "log": my_log,
    "fib": fib,
    "fac": my_fac,
}

function_n = {"min": min, "max": max, "sum": sum, "mean": mean}


def statement(wtok, variables):
    """See syntax chart for statement"""
    result = assignment(wtok, variables)
    if wtok.is_at_end():  # Om EOL --> Returnerna
        return result
    else:
        raise SyntaxError("Expected EOL")


def assignment(wtok, variables):
    """See syntax chart for assignment"""
    result = expression(wtok, variables)
    while wtok.get_current() == "=":
        wtok.next()
        if wtok.is_name():
            # Lägg till eller ändra variabelns värde i lexikonet
            variables[wtok.get_current()] = result
            wtok.next()
        else:
            raise SyntaxError("Expected name after '='")
    return result


def expression(wtok, variables):
    """See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() == "+" or wtok.get_current() == "-":
        if wtok.get_current() == "+":
            wtok.next()
            result = result + term(wtok, variables)
        elif wtok.get_current() == "-":
            wtok.next()
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    """See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() == "*" or wtok.get_current() == "/":
        if wtok.get_current() == "*":
            wtok.next()
            result = result * factor(wtok, variables)
        elif wtok.get_current() == "/":
            wtok.next()
            try:
                result = result / factor(wtok, variables)
            except ZeroDivisionError:  # Om det är division med noll hantera med EvaluationError
                raise EvaluationError("Division by zero")
    return result


def factor(wtok, variables):
    """See syntax chart for factor"""
    # Fall 1: "("
    if wtok.get_current() == "(":
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() == ")":
            wtok.next()
        else:
            raise SyntaxError("Expected ')'")

    # Fall 2: function_1
    elif wtok.get_current() in function_1:
        func = function_1[wtok.get_current()]  # Hämta funktionen från lexikonet
        wtok.next()
        if wtok.get_current() == "(":
            wtok.next()
            arg = assignment(wtok, variables)
            result = func(arg)  # Lagt till nu!
            if wtok.get_current() == ")":
                wtok.next()
            else:
                raise SyntaxError("Expected ')'")
        else:
            raise SyntaxError("Expected '('")

    # Fall 3: function_n
    elif wtok.get_current() in function_n:
        func = function_n[wtok.get_current()]  # Hämta funktionen från lexikonet
        wtok.next()
        arg = arglist(wtok, variables)  # Läs in argumenten med arglist()
        result = func(arg)

    # Fall 4: name
    elif wtok.is_name():
        if wtok.get_current() in variables:
            result = variables[
                wtok.get_current()
            ]  # Hämta variabelns väre från lexikonet
            wtok.next()
        else:
            raise EvaluationError(f"Undefined variable: '{wtok.get_current()}'")

    # Fall 5: number
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    # Fall 6: "-"
    elif wtok.get_current() == "-":
        wtok.next()
        result = (-1) * factor(wtok, variables)

    else:
        raise SyntaxError("Expected number or '('")

    return result


def vars(variables):
    for key in variables:
        print(f"{key}: {variables[key]}")


def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """

    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    # Note: The unit test file initiate variables in this way. If your implementation
    # requires another initiation you have to update the test file accordingly.
    init_file = "MA2Files\MA2Files\MA2init.txt"
    lines_from_file = ""
    try:
        with open(init_file, "r") as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print("init  :", line)
        else:
            line = input("\nInput : ")
        if line == "" or line[0] == "#":
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == "quit":
            print("Bye")
            exit()

        elif wtok.get_current() == "vars":
            vars(variables)

        else:
            try:
                result = statement(wtok, variables)
                variables["ans"] = result
                print(f"Result: {result}\n")

            except EvaluationError as ve:
                print("*** Evaluation error: ", ve)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                    f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'"
                )

            except TokenError as te:
                print("*** Syntax error: Unbalanced parentheses")


if __name__ == "__main__":
    main()
