# -------------------------------------------------------------------------------------------------------------
# Escape Sequence Characters:
# \b:   Backspace
# \↵:   Escape New Line
# \\:   Escape Backslash
# \':   Escape Single Quote
# \":   Escape Double Quote
# \n:   New Line (Line Feed)
# \r:   Carriage Return (replaces "Charecter by Character" the operand to the left with that on the right)
# NOTE: \n\r guarantees that the following comes in a new line without any other precedent characters
# \t:   Horizontal Tab
# \xhh: Character with a Hex Value (ASCII Code)
#
# NOTE: to escape the escape sequence characters, use raw string "r" operator before the string
# -------------------------------------------------------------------------------------------------------------

# Backspace:
print("Hello  \bWorld!\b ")

# Escape New Line:
print("Hello \
World")

# Escape Backslash:
print("I love Backslash, here it is: \\")

# Escape Single Quote:
print('I\'m Amr')

# Escape Double Quotes:
print("And I love escaping the \"double\" quotes")

# New Line:
print("Hello\nWorld")

# Carriage Return:
print("12345678901234567890\rCarriage Return")

# Horizontal Tab:
print("Hello\tWorld\twith\tTabs")

# Character with a Hex Value:
print("\x48\x65\x6C\x6C\x6F\x20\x57\x6F\x72\x6C\x64\x20\x69\x6E\x20\x41\x53\x43\x49\x49")

print("\nPrint raw string using thr \"r\" operator:")
# Backspace:
print(r"Hello  \bWorld!\b ")

# Escape New Line:
print(r"Hello \
World")

# Escape Backslash:
print(r"I love Backslash, here it is: \\")

# Escape Single Quote:
print(r'I\'m Amr')

# Escape Double Quotes:
print(r"And I love escaping the \"double\" quotes")

# New Line:
print(r"Hello\nWorld")

# Carriage Return:
print(r"12345678901234567890\rCarriage Return")

# Horizontal Tab:
print(r"Hello\tWorld\twith\tTabs")

# Character with a Hex Value:
print(r"\x48\x65\x6C\x6C\x6F\x20\x57\x6F\x72\x6C\x64\x20\x69\x6E\x20\x41\x53\x43\x49\x49")
