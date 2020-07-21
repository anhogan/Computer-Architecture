PRINT_NAME = 0b01 # 1
HALT = 0b10 # 2
PRINT_NUM = 0b11 # 3
SAVE = 0b100 # 4
PRINT_REG = 0b101 # 5
ADD = 0b110 # 6

memory = [
  PRINT_NAME,
  PRINT_NAME,
  PRINT_NUM,
  42,
  SAVE,
  2,
  99,
  SAVE,
  3,
  1,
  ADD,
  2,
  3,
  PRINT_REG,
  2,
  HALT
] # RAM

registers = [0] * 8

pc = 0 # Program counter
running = True

while running:
  command = memory[pc]

  if command == PRINT_NAME:
    print('Amanda')
  elif command == HALT:
    running = False
  elif command == PRINT_NUM:
    number = memory[pc + 1]
    print(number)

    pc += 1
  elif command == SAVE:
    register = memory[pc + 1]
    number = memory[pc + 2]
    registers[register] = number

    pc += 2
  elif command == PRINT_REG:
    register_index = memory[pc + 1]
    print(registers[register_index])
    
    pc += 1
  elif command == ADD:
    register_one = memory[pc + 1]
    register_two = memory[pc + 2]

    registers[register_one] = registers[register_one] + registers[register_two]

    pc += 2

  pc += 1

  # pc += 1 + (command >> 6)