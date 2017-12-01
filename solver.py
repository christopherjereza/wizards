import argparse
import Queue as queue
import random
"""
======================================================================
  Complete the following function.
======================================================================
"""
def enforce(constraint, age):
    w1 = constraint[0]
    w2 = constraint[1]
    w3 = constraint[2]
    if age[w1] < age[w2]:
        if age[w3] < age[w1] or age[w3] > age[w2]:
            return False
    else:
        if age[w3] > age[w1] or age[w3] < age[w2]:
            return False
    return True

def validate(solution, constraint):
    w1 = constraint[0]
    w2 = constraint[1]
    w3 = constraint[2]
    if solution.index(w1) < solution.index(w2):
        if solution.index(w3) < solution.index(w1) or solution.index(w3) > solution.index(w2):
            return False
    else:
        if solution.index(w3) > solution.index(w1) or solution.index(w3) < solution.index(w2):
            return False
    return True

def cost(solution, constraints):
    cost = 0
    for constraint in constraints:
        if not validate(solution, constraint):
            cost += 1
    return cost

def neighbor(solution):
    wizToMove = solution.pop(random.randint(0, len(solution) - 1))
    solution.insert(random.randint(0, len(solution)), wizToMove)
    return solution

def acceptance_probability(old_cost, new_cost, T):
    exponent = float((old_cost - new_cost) / float(T))
    alpha = float(float(2.71828) ** float(exponent))
    # print alpha
    return alpha

def anneal(num_wizards, num_constraints, wizards, constraints):
    random.shuffle(wizards)
    solution = wizards
    old_cost = cost(solution, constraints)
    T = 1.0
    T_min = 0.00001
    alpha = 0.99
    while T > T_min:
        i = 1
        while i <= 100:
            new_solution = neighbor(solution)
            new_cost = cost(new_solution, constraints)
            if new_cost == 0:
                return new_solution
            ap = acceptance_probability(old_cost, new_cost, T)
            if ap > random.random():
                solution = new_solution
                old_cost = new_cost
            i += 1
        T = T*alpha
    return solution

def validator(wizards, constraints):
    i = 0
    for wizard in wizards:
        for constraint in constraints:
            wizard1 = constraint[0]
            wizard2 = constraint[1]
            wizard3 = constraint[2]
            if wizard == wizard3:
                if wizards.index(str(wizard)) not in range(wizards.index(str(wizard1)), wizards.index(str(wizard2))):
                    i += 1
    return i // len(constraints)

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
    return anneal(num_wizards, num_constraints, wizards, constraints)
    random.shuffle(wizards)
    complete = False
    while not complete:
        for wizard in wizards:
            for constraint in constraints:
                if wizard == constraint[2]:
                    if (wizards.index(str(constraint[0])) > wizards.index(str(constraint[2]))
                        and wizards.index(str(constraint[1])) < wizards.index(str(constraint[2]))) or (wizards.index(str(constraint[0])) < wizards.index(str(constraint[2]))
                        and wizards.index(str(constraint[1])) > wizards.index(str(constraint[2]))):
                        continue
                    else:
                        to_shuffle = wizards[wizards.index(str(wizard)):]
                        wizards = wizards[0:wizards.index(str(wizard))]
                        random.shuffle(to_shuffle)
                        wizards += to_shuffle 
        if validator(wizards, constraints) == 1:
            return wizards
        else:
            random.shuffle(wizards)


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
