import argparse
import random
import math
import copy
import time
"""
======================================================================
  Complete the following function.
======================================================================
"""
def cost(solution, constraints):
    return validator(solution, constraints)

#Move a randomly-selected wizard to a random location in the ordering
def neighbor(solution):
    temp = copy.deepcopy(solution)
    wizToMove = temp.pop(random.randrange(len(temp)))
    temp.insert(random.randrange(len(temp)), wizToMove)
    return temp

#The probability of accepting a sampled ordering.
def acceptance_probability(old_cost, new_cost, T):
    if new_cost < old_cost:
        return 1.0
    else:
        return math.exp((old_cost - new_cost) / T)

#Simulated Annealing main function
def anneal(num_wizards, num_constraints, wizards, constraints):
    ageDict = {}
    startTime = time.time()
    random.shuffle(wizards)
    solution = wizards
    old_cost = cost(solution, constraints)
    new_cost = num_constraints
    T = 1.0
    T_min = 0.0001
    alpha = 0.9
    while T > T_min:
        currTime = time.time()
        if currTime - startTime > num_wizards*2:
            return wizards, old_cost
        i = 1
        while i <= 9000:
            new_solution = neighbor(solution)
            new_cost = cost(new_solution, constraints)
            if new_cost == 0:
                return new_solution, new_cost
            ap = acceptance_probability(old_cost, new_cost, T)
            if ap > random.random():
                solution = new_solution
                old_cost = new_cost
            i += 1
        T = T*alpha
    return solution, old_cost

def validator(wizards, constraints):
    count = 0
    for constraint in constraints:
        wiz1 = wizards.index(constraint[0])
        wiz2 = wizards.index(constraint[1])
        wiz3 = wizards.index(constraint[2])
        if wiz1 < wiz2:
            if wiz3 > wiz1 and wiz3 < wiz2:
                continue
            else:
                count += 1
        if wiz2 < wiz1:
            if wiz3 < wiz1 and wiz3 > wiz2:
                continue
            else:
                count += 1
    return len(constraints) - count

def solve(num_wizards, num_constraints, wizards, constraints):
    """
    Write your algorithm here.
    Input:
        num_wizards: Number of wizards
        num_constraints: Number of constraints
        wizards: An array of wizard names, in no particular order
        constraints: A 2D-array of constraints,
                     where constraints[0] may take the form ['A', 'B', 'C']

    Output:
        An array of wizard names in the ordering your algorithm returns
    """
    ret = wizards
    cost = num_constraints
    while cost > 0:
        print 'attempt'
        print cost
        ret, cost = anneal(num_wizards, num_constraints, ret, constraints)
    return ret

"""
======================================================================
   No need to change any code below this line
======================================================================
"""

def read_input(filename):
    with open(filename) as f:
        num_wizards = int(f.readline())
        num_constraints = int(f.readline())
        constraints = []
        wizards = set()
        for _ in range(num_constraints):
            c = f.readline().split()
            constraints.append(c)
            for w in c:
                wizards.add(w)

    wizards = list(wizards)
    return num_wizards, num_constraints, wizards, constraints

def write_output(filename, solution):
    with open(filename, "w") as f:
        for wizard in solution:
            f.write("{0} ".format(wizard))

if __name__=="__main__":
    parser = argparse.ArgumentParser(description = "Constraint Solver.")
    parser.add_argument("input_file", type=str, help = "___.in")
    parser.add_argument("output_file", type=str, help = "___.out")
    args = parser.parse_args()

    num_wizards, num_constraints, wizards, constraints = read_input(args.input_file)
    solution = solve(num_wizards, num_constraints, wizards, constraints)
    write_output(args.output_file, solution)
