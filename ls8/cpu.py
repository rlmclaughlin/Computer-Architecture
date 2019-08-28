import sys

MUL = 0b10100010
LDI = 0b10000010
PRN = 0b01000111
HLT = 0b00000001

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 256
        self.ram = [0] * 8
        self.pc = 0 
        self.hlt = False

        self.ops = {
            LDI: self.op_ldi,
            HLT: self.op_hlt,
            MUL: self.op_mul,
            PRN: self.op_prn
        }

    def op_ldi(self, op_a, op_b):
        self.reg[op_a] = [op_b]

    def op_prn(self, addr, op_b):
        print(self.reg[addr])

    def op_hlt(self, op_a, op_b):
        self.hlt = True

    def op_mul(self, addr1, addr2): 
        self.alu('MUL', addr1, addr2)
        
    def ram_read(self, mar):
        return self.ram[mar]

    def ram_write(self, mar, mdr):
        self.ram[mar] = mdr

    def load(self):
        """Load a program into memory."""

        address = 0

        #program = [
        #    # From print8.ls8
        #    0b10000010, # LDI R0,8
        #    0b00000000,
        #    0b00001000,
        #    0b01000111, # PRN R0
        #    0b00000000,
        #    0b00000001, # HLT
        #]
#
        #for instruction in program:
        #    self.ram[address] = instruction
        #    address += 1
        with open(filename) as file: 
            for line in file: 
                comment_split = line.split('#')
                instruction = comment_split[0]
        
                if instruction == '':
                    continue
                first_bit = instruction[0]

                if first_bit == '0' or first_bit =='1':
                    self.ram[address] = (instruction[:8], 2)
                    address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "Mul":
            self.reg[reg_a] *= self.reg[reg_b]
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
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""

        
        while not self.hlt:
            ir = self.ram_read(self.pc)
            op_a = self.ram_read(self.pc + 1)
            op_b = self.ram_read(self.pc + 2)
         
            op_size = ir >> 6
            ins_set = ((ir >> 4) & ob1) == 1

            0b00000001 >> 4
        &   0b00000001
            0b00000001

           #if ir == LDI:
           #    self.reg[op_a] = op_b
           #elif ir == PRN:
           #    print(self.reg[op_a])
           #elif ir == HLT:
           #    self.hlt = True
           #

           if ir in self.ops:
               self.ops[ir](op_a, op_b)

           if not ins_set:
               self.pc += op_size + 1

               
        
