import argparse

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
                     where constraints[0] may take the form ['A', 'B', 'C']i

    Output:
        An array of wizard names in the ordering your algorithm returns
    """
    create dictionary where dictionary[wizard] returns the set of all constraints involving that wizard:
    add all constraints to queue
    result = [all wizards]
    while queue is not empty:
        constraint = queue.pop()
        constraint = true
        if w1 < w2:
            if not (w3 < w1 or w3 > w2):
                constraint = false

        else:
            if not (w3 > w1 or w3 < w2):
                constraint = false

        if constraint is false:
            swap w3 w1
            w1Constraints = dictionary[w1]
            w2Constraints = dictionary[w2]
            w3Constraints = dictionary[w3]
            for c in w1Constraints:
                if c not in queue:
                    queue.add(c)
            for c in w2Constraints:
                if c not in queue:
                    queue.add(c)
            for c in w3Constraints:
                if c not in queue:
                    queue.add(c)
    return result

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
