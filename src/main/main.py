from analyze import extract_instructions

# Simulated register file
registers = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'H': 0,
    'L': 0
}

def parse_immediate(value):
    """Convert immediate like 05H to integer."""
    if value.endswith('H'):
        return int(value[:-1], 16)
    return int(value)

def simulate_instruction(instr):
    opcode = instr['opcode']
    operands = instr['operands']

    if opcode == 'MVI':
        reg, value = operands
        if reg in registers:
            registers[reg] = parse_immediate(value)
            print(f"{reg} <- {value} (now {registers[reg]})")
        else:
            print(f"Error: Unknown register {reg}")

    elif opcode == 'ADD':
        reg = operands[0]
        if reg in registers:
            registers['A'] = (registers['A'] + registers[reg]) & 0xFF
            print(f"A <- A + {reg} = {registers['A']}")
        else:
            print(f"Error: Unknown register {reg}")

    elif opcode == 'HLT':
        print("Program halted.")
        return False  # Stop execution

    else:
        print(f"Unknown instruction: {opcode}")
    
    return True

def main():
    instructions = extract_instructions("input.asm")
    print("\n--- Parsed Instructions ---")
    for i, instr in enumerate(instructions):
        print(f"{i+1}: {instr}")

    print("\n--- Simulation ---")
    for instr in instructions:
        should_continue = simulate_instruction(instr)
        if not should_continue:
            break

    print("\n--- Final Register State ---")
    for reg, val in registers.items():
        print(f"{reg}: {val:02X}")

if __name__ == "__main__":
    main()
