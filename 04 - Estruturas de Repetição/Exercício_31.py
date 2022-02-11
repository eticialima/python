"""
31) Faça um programa que calcule o valor de S
    S = 1/1 + 3/2 + 5/3 + 7/4 ... 99/50
"""

s = 0.0

term_01 = range(1, 100, 2)
term_02 = range(1, 51)

for n in range(0, 50):
    s += term_01[n] / term_02[n]

print(s)
