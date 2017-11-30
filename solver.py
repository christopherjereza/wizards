import argparse
import queue
import random
"""
======================================================================
  Complete the following function.
======================================================================
"""
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
    d = {}
    age = {}
    index = 0
    for wizard in wizards:
        age[wizard] = index
        index++
        d[wizard] = [[]]
    q = queue.Queue()
    for constraint in constraints:
        w1 = constraint[0]
        w2 = constraint[1]
        w3 = constraint[2]
        d[w1].append(constraint)
        d[w2].append(constraint)
        d[w3].append(constraint)
        q.put(constraint)
    while not q.empty():
        constraint = q.pop()
        enforce = true
        w1 = constraint[0]
        w2 = constraint[1]
        w3 = constraint[2]
        if age[w1] < age[w2]:
            if age[w3] > age[w1] and age[w3] < age[w2]:
                enforce = false
        else:
            if age[w3] < age[w1] and age[w3] > age[w2]:
                enforce = false

        if enforce is false:
            wizToSwap = random.choice([w1, w2])
            temp = age[w3]
            age[w3] = age[wizToSwap]
            age[wizToSwap] = temp
            w3Constraints = d[w3]
            wizToSwapConstraints = d[wizToSwap] 
            for c in wizToSwapConstraints:
                if c not in queue:
                    queue.add(c)
            for c in w3Constraints:
                if c not in queue:
                    queue.add(c)
    sorted(d, key=d.get)
    return d.keys()

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
