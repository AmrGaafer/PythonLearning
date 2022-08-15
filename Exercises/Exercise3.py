# -------------------------------------------------------------------------------------------------------------
# Exercise #3:  Numbers & Arithmetic Operators
# Developer:    Amr Gaafer
# Date          15.08.2022
# -------------------------------------------------------------------------------------------------------------

print("Task#1: Numbers types:")
iVar = 0
fVar = 0.0
complexVar = 0+0j

print(type(iVar))
print(type(fVar))
print(type(complexVar))

print("Task#2: Complex numbers components:")
complexVar = 1+2j
print(complexVar.imag)
print(complexVar.real)

print("Task#3: integer number conversion to float:")
iVar = 10
print(format(iVar, ".10f"))

print("Task#4: float number conversion to integer:")
fVar = 159.650
iVar = int(fVar)
print(iVar)
print(type(iVar))

print("Task#5: mathematical operators:")
print("1) 100 ? 115 = -15")
print(100 - 115)
print("2) 50 ? 30 = 1500")
print(50 * 30)
print("3) 21 ? 4 = 1")
print(21 % 4)
print("4) 110 ? 11 = 10")
print(110 / 11)
print("5) 97 ? 20 = 4")
print(97 // 20)
