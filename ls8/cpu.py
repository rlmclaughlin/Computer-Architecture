import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 0x08
        self.ram = [0] * 0xff
        self.pc = 0x00 
        self.ir = 0x00
        self.h = 0b00000001 
        
    def ram_read(self, current):
        return self.ram[current]

    def ram_write(self, write, current):
        self.ram[current] = write

    def load(self):
        """Load a program into memory."""

        address = 0

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 3),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        LDI = 0b10000010
        PRN = 0b01000111
        
        run_cpu = True

        while run_cpu:

            self.ir = self.pc
            o1 = self.ram_read(self.pc + 1)
            o2 = self.ram_read(self.pc + 2)

            if self.ram[self.ir] == self.h:
                run_cpu = False
            elif self.ram[self.ir] == LDI:
                self.reg[o1] = o2
                self.pc += 3
            elif self.ram[self.ir] == PRN:
                print(self.reg[o1])
                self.pc += 2
