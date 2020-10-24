# this program constructs a 3 peg tower of hanoi given x rings and then solves it

import numpy as np

# number of rings
nrings = input('How many rings? ')


# custom exception for invalid moves
class InvalidMove(Exception):
    pass


# creates each peg and assigns the first one all the rings
peg1 = ['1']
for each in reversed(range(nrings)):
    peg1 = peg1 + [each + 1]
peg2 = ['2']
peg3 = ['3']


# moves one ring from the top of the source to the top of the destination
def move_ring(source, destination):
    destination.append(source.pop())


def solve(n, source, spare, destination):
    # nothing left to do
    if n == 0:
        return

    # move a tower of size n - 1 to the spare peg
    solve(n - 1, source, destination, spare)

    # move the largest peg from the source to the destination
    # and also print the step for display purposes
    print(f"move ring {source[-1]} from peg {source[0]} to peg {destination[0]}")
    move_ring(source, destination)

    # move the tower of size n - 1 to the destination peg
    solve(n - 1, spare, source, destination)



solve(nrings, peg1, peg2, peg3)
