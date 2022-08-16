# -------------------------------------------------------------------------------------------------------------
# Exercise #7:  Operators & Type Conversion
# Developer:    Amr Gaafer
# Date          15.08.2022
# -------------------------------------------------------------------------------------------------------------

print("Task#1: apply bool():")
print(1.0 == 15)
print(bool(0))
print(bool(''))
print(bool(0+0j))

print(1.0 == 1)
print(bool(1))
print(bool('Amr'))
print(bool(0+0.5j))
print(bool([1]))

print("Task#2: apply boolean operators:")
cpp = 70
pythpn = 55
plcST = 85
print(cpp > 50 and pythpn > 50 and plcST > 50)

print("Task#3: apply boolean operators:")
num_one = 10
num_two = 20
num = 20
print(num > num_one or num > num_two)
print(num > num_one and num > num_two)

print("Task#4: mathematical operators:")
num_one = 10
num_two = 20
result = num_one + num_two
print(result)
result **=3
print(result)
result %= 26000
print(result)
result /= 5
print(result)
print(type(result))
print(type(str(result)))
