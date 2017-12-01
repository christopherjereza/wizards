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

def neighbor(solution):
    temp = copy.deepcopy(solution)
    wizToMove = temp.pop(random.randrange(len(temp)))
    temp.insert(random.randrange(len(temp)), wizToMove)
    return temp

def acceptance_probability(old_cost, new_cost, T):
    if new_cost < old_cost:
        return 1.0
    else:
        return math.exp((old_cost - new_cost) / T)


def anneal(num_wizards, num_constraints, wizards, constraints):
    startTime = time.time()
    random.shuffle(wizards)
    solution = wizards
    old_cost = cost(solution, constraints)
    new_cost = None
    T = 1.0
    T_min = 0.0001
    alpha = 0.9
    while T > T_min:
        currTime = time.time()
        if currTime - startTime > num_wizards*3:
            print new_cost
            return None
        i = 1
        while i <= 6000:
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
    print currTime - startTime
    return solution

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
<<<<<<< HEAD
    ret = None
    while ret is None:
        print 'attempt'
        ret = anneal(num_wizards, num_constraints, wizards, constraints)
    return ret
=======
    res = random.shuffle(wizards)
    neighbors = [[]]
    cost = 0
    while !validate(res):
        for c in constraints:
            wiz1 = c[0]
            wiz2 = c[1]
            wiz3 = c[2]
            if res.index(wiz3) > res.index(wiz1) and res.index(wiz3) < res.index(wiz2):
                cost += 1
            else:

            elif res.index(wiz3) < res.index(wiz1) and res.index(wiz3) > res.index(wiz2):
                cost += 1
    return res

def validate(ordering, constraints):
    for c in constraints:
        wiz1 = c[0]
        wiz2 = c[1]
        wiz3 = c[2]
        if res.index(wiz3) > res.index(wiz1) and res.index(wiz3) < res.index(wiz2) 
            or res.index(wiz3) < res.index(wiz1) and res.index(wiz3) > res.index(wiz2):
                return False
    return True


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
        index+=1
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
>>>>>>> 34fa090c9390fec9814a0eb72dda2a1e2eb7534b

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
