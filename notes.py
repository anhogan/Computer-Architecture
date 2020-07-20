'''
NUMBER REPRESENTATION
'''

# ** Decimal, Base 10 **

# 0 - 9
# 10 > 10 + 0 ones
# 11 > 10 + 1 one
# 100 > 100 + 0 tens + 0 ones

# OdNUM for decimal

# ** Hex, Base 16 **

# 0 - 9, A - F
# A > 10
# B > 11
# C > 12
# D > 13
# E > 14
# F > 15
# 10 > 16 ... F becomes a zero and add a one in front
# 11 > 17 ... one F and one one
# 1A > 20 ... 10 + A

# OxNUM for hex
# hex(NUM)
# int(NUM, 16) to convert to decimal
# print(f'{NUM:x}) or print(f'{NUM:X}) for capital letters
# Easier to convert to binary

# ** Binary, Base 2 **

# 0, 1
# 10 > 2, 1 two and zero ones
# 110 > 6, 1 four, 1 two, zero ones
# 1000 > 8, 1 eight, zero fours, zero twos, zero ones

# ObNUM for binary
# int(NUM, 2) to convert to decimal
# print(f'{NUM:b})
# Count by the power of two (1, 2, 4, 8, 16, 32, 64, 128, 256, etc.)

# ** Place Breakdown **

# DECIMAL (Base 10)
# +----- 1000s Place
# |+---- 100s Place
# ||+--- 10s Place
# |||+-- 1s Place
# ||||
# ABCD
# 1234

# BINARY (Base 2)
# +----- 8 Place (0b1000)
# |+---- 4 Place (0b100)
# ||+--- 2 Place (0b10)
# |||+-- 1s Place (0b1)
# ||||
# ABCD
# 1010

# ** Examples **

# HEX to DECIMAL

# 0x73 (Hex) > (7 * 16) + 3 = 112 + 3 = 115 (Decimal)
# 0x3F (Hex) > (3 * 16) + 15 = 48 + 15 = 63 (Decimal)
# 0xE3 (Hex) > (14 * 16) + 3 = 224 + 3 = 227 (Decimal)
# 0xAC (Hex) > (10 * 16) + 12 = 160 + 12 = 172 (Decimal)

# DECIMAL to HEX

# 54 (Decimal) > 54 / 16 = 3.375 > 16 * 3 = 48 > 54 - 48 = 6 > 0x36 (Hex)

# DECIMAL to BINARY
# 3 (Decimal) = 3 / 2 = 1, remainder 1 > 1 / 2 = 0, remainder 1 > 0b11 (Binary)
# 15 (Decimal) = 15 / 2 = 7, remainder 1 > 7 / 2 = 3, remainder 1 > 3 / 2 = 1, remainder 1 > 1 / 2 = 0, remainder 1 > 0b1111 ( Binary)

# BINARY to DECIMAL

# 0b11001010 (Binary) > 0 (1) + 1 (2) + 0 (4) + 1 (8) + 0 (16) + 0 (32) + 1 (64) + 1 (128) = 2 + 8 + 64 + 128 = 74 + 128 = 202 (Decimal)
# 0b11111111 (Binary) > 0b1111 + 0b1111 = (1 + 2 + 4 + 8) + (1 + 2 + 4 + 8) = 15 + 15 = 0xFF (Hex) > (16 * 15) + 15 = 240 + 15 = 255 (Decimal)

# BINARY to HEX

# 0b10101100 (Binary) > 0b1010 + 0b1100 = (8 + 2) + (8 + 4) = 10 + 12 = A + C = 0xAC (Hex)

# Decimal > Hex > Binary
# Binary > Hex > Decimal