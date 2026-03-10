#import math
from math import * #rather than importing the math namespace you import the pi value and can access it with pi instead of math.pi
#only imports the variable pi, not other math functions and values

from aux_fctns import * #imports every value from the file

from math import pi as pi_long #import pi with a different variable name

#import aux_fctns as aux

#print(pi)

#print(aux.fctn1())
#print(aux.fctn2(3))

import aux_fctns as aux # import the file as something else to use aux.fctn1() instead

