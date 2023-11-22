
#        GAUTAM KUMAR MAHAR 
#             2103114

########################################
# No student in the statistics class is #
# Smarter than every student in the     #
# logic class. 

# Hence, some student in   #
# the logic class is Smarter than every #
# student in the statistics class.       #
########################################

from z3 import *

# Declare sorts and functions
Student = DeclareSort('Student')

L = Function('Logic', Student, BoolSort())
S = Function('Statistics', Student, BoolSort())
Smarter = Function('Smarter', Student, Student, BoolSort())

# Free variables
x, y = Consts('x y', Student)

# Create a solver
s = Solver()

# Premise: No student in the statistics class is Smarter than every student in the logic class
Premise = ForAll(x, Implies(S(x), Exists(y, And(L(y), Not(Smarter(x, y))))))
s.add(Premise)

# Conclusion: Some student in the logic class is Smarter than every student in the statistics class
conclusion = Exists(x, And(L(x), ForAll(y, Implies(S(y), Smarter(x, y)))))

# Add the statements to the solver
s.add(Not(conclusion))

# Check for validity
if s.check() == sat:
    print("The argument is not valid.")
else:
    print("The argument is valid.")
