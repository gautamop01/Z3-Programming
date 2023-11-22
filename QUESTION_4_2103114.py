
#        GAUTAM KUMAR MAHAR 
#             2103114

########################################
# Whoever can read is literate.         #
# Dolphins are not literate.             #
# Some dolphins are intelligent.         #
# Some who are intelligent cannot read.  #
########################################


from z3 import *

# Declare sorts and functions
Entity = DeclareSort('Entity')

# Define boolean functions
Read = Function('Read', Entity, BoolSort())
Dolphin = Function('Dolphin', Entity, BoolSort())
Literate = Function('Literate', Entity, BoolSort())
Intelligent = Function('Intelligent', Entity, BoolSort())

# Free variable
x = Const('x', Entity)

# Create a solver
s = Solver()

# Statements
# Premise 1: Whoever can read is literate
Premise1 = ForAll(x, Implies(Read(x), Literate(x)))
s.add(Premise1)

# Premise 2: Dolphins are not literate
Premise2 = ForAll(x, Implies(Dolphin(x), Not(Literate(x))))
s.add(Premise2)

# Premise 3: Some dolphins are intelligent
Premise3 = Exists(x, And(Dolphin(x), Intelligent(x)))
s.add(Premise3)

# Conclusion: Some who are intelligent cannot read.
conclusion = Exists(x, And(Intelligent(x), Not(Read(x))))
s.add(Not(conclusion))

# Check for validity
if s.check() == sat:
    print("The argument is not valid.")
else:
    print("The argument is valid.")
