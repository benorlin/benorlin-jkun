from polynomial import Polynomial
from states import states

for name, votes in states.items():
    polyProd = Polynomial([1])

    for other, otherVotes in states.items():
        if other == name:
            continue
        coefficients = [0.5] + [0] * (otherVotes - 1) + [0.5]
        polyProd = polyProd * Polynomial(coefficients)

    sumOfCoeffs = sum(polyProd.coefficients[i] for i in range(270-votes, 270))
    print("{:20s}{:.3f}".format(name, sumOfCoeffs))
