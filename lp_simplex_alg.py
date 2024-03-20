"""Simplex algorithm from linked video for CSC373"""

from typing import List, Tuple
from fractions import Fraction


def calc(lst: List[List[float]],
         rhs: List[float]) -> Tuple[List[List[float]], List[float], List[str]]:
    """my dumbass didn't want to relearn the
    algorithm for this so i spent 2 hours coding it instead

    first input should be a list of lists,
    where each sublist is the coefficients of the LHS of an equation.
    equations need to be in slack form from that one youtube wideo.

    https://www.youtube.com/watch?v=FYqg62rYxhs&t=2s&ab_channel=Ekeeda
    ^this wideo. algorithm is also just this wideo

    second input should be the RHSs of
    each equation in the same order as the first input
    (ie. eq1 in lst should correspond to it's RHS in rhs)

    i didnt add for a case when theres no soln
    so figure that out yourself if it happens
    ok now i did. if the output is screaming at you then theres a problem.
    if you didnt notice thats a you problem

    also i made the output very readable,
    but if something isn't lining up with the ratio or rhs use the debugger

    theres no error checking for if the dimensions of
    this don't line up so if theres an error its
    your fault and even if it is something wrong with this,
    its still your fault because haha f u

    i dont wanna write the doctests but here are some verified examples

    midterm:
    lst = [[-4, -1, -3, 0, 0, 0],
           [1, 4, 0, 1, 0, 0],
           [3, -1, 1, 0, 1, 0],
           ]
    rhs = [0, 2, 4]

    i think from one of the wideos idk it was in my notes
    lst = [[-1, -4, 0, 0, 0],
           [2, 1, 1, 0, 0],
           [3, 5, 0, 1, 0],
           [1, 3, 0, 0, 1]]
    rhs = [0, 3, 9, 5]

    a3
    lst = [[-4, -1, -5, -3, 0, 0, 0],
           [1, -1, -1, 3, 1, 0, 0],
           [5, 1, 3, 8, 0, 1, 0],
           [-1, 2, 3, -5, 0, 0, 1]
           ]
    rhs = [0, 1, 55, 3]
    """
    iteration = 1
    var_names = ['z']
    column = []
    # so that you can get a nice output. setting rows
    for i in range(1, len(lst)):
        var_names.append('s' + str(i))

    # setting columns for output
    for i in range(0, len(lst[0])-3):
        column.append('x' + str(i+1))
    for i in range(len(lst[0])-3, len(lst[0])):
        column.append('s' + str(i-2))

    # main loop
    while True:
        key_col = 0
        key_row = 0
        key_ratio = 100
        # ^ default is arbitrary.
        # if the key ratio is in fact 100 then lmao rip you ig

        # find key row
        for i in range(len(lst[0])):
            if lst[0][i] < 0 and lst[0][i] <= lst[0][key_col]:
                key_col = i
        if lst[0][key_col] >= 0:
            return lst, rhs, var_names  # if no row, done

        # find key column
        for i in range(1, len(rhs)):
            ratio = rhs[i]/lst[i][key_col]
            if 0 < ratio < key_ratio:
                key_row = i
                key_ratio = ratio
        if key_ratio == 100:
            print("AHHHHHHHHHHHHHHH STOP STOP STOP AHHHHHHH "
                  + "WAIT CHILL BRO READ THE COMMENTS !!!!!!!!!!"
                  + "!!!!!!!!!!!!!!!!!!!")
            return lst, rhs, var_names  # if no column, done.
            # actually tho this means theres no soln iirc.
            # check like the 3rd video that guy did on simplex
            # from the link in the docstring idk what
            # should happen i didnt test this

        # update key row with new values
        key_val = lst[key_row][key_col]
        for i in range(len(lst[key_row])):
            lst[key_row][i] = lst[key_row][i] / key_val
        rhs[key_row] = rhs[key_row] / key_val

        # readability stuff. this line below is telling you what rows swapped
        print("swap in " + str(iteration) + ' ' + var_names[key_row]
              + " with " + column[key_col])
        # swapping vars for output
        temp = var_names[key_row]
        var_names[key_row] = column[key_col]
        column[key_col] = temp

        # update rest of table
        for i in range(len(rhs)):
            if i != key_row:
                key_val = lst[i][key_col]
                for j in range(len(lst[i])):
                    lst[i][j] = lst[i][j] - key_val * lst[key_row][j]
                rhs[i] = rhs[i] - key_val * rhs[key_row]

        # for double checking your tables
        print("############## iteration " + str(iteration) + " ##############")
        for row in lst:
            print([str(Fraction(x).limit_denominator()) for x in row])
        print("\n")
        iteration += 1


def main():
    """its main pylint idk what you want from me"""
    lst = [[-4, -1, -5, -3, 0, 0, 0],
           [1, -1, -1, 3, 1, 0, 0],
           [5, 1, 3, 8, 0, 1, 0],
           [-1, 2, 3, -5, 0, 0, 1]
           ]
    rhs = [0, 1, 55, 3]
    lst, rhs, var_names = calc(lst, rhs)

    print("################################ " +
          "FINAL OUTPUT ################################")
    for row in lst:
        print([str(Fraction(x).limit_denominator()) for x in row])
    print("\n")
    print([str(Fraction(x).limit_denominator()) for x in rhs])
    print(var_names)

    print("\n")
    print("z max is " + str(Fraction(rhs[0]).limit_denominator()))
    for i in range(1, len(var_names)):
        if 's' not in var_names[i]:
            print(var_names[i] + " is " +
                  str(Fraction(rhs[i]).limit_denominator()))
    # missing xs mean x# = 0


if __name__ == "__main__":
    main()
