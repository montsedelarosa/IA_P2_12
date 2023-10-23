# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

from sympy import symbols, Or, And, Not, Implies, to_cnf, satisfiable

# Definir variables
A, B, C = symbols('A B C')

# Definir una fórmula lógica
formula = And(Or(A, B), Or(Not(A), C), Implies(B, C))

# Convertir la fórmula a su Forma Normal Conjuntiva (FNC)
fnc = to_cnf(formula, True)

# Imprimir la fórmula en FNC
print("Fórmula en FNC:", fnc)

# Realizar resolución
resolucion = satisfiable(fnc, algorithm="dpll")

if resolucion:
    print("La fórmula es válida (satisfacible).")
else:
    print("La fórmula no es válida (insatisfacible).")
