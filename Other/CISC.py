class CISC:
    def __init__(self):
        self.bits = [None] * 32

    # get proper index
    def get(self, i): return len(self.bits) - 1 - i

    def clear(self, i): self.bits[self.get(i)] = 0

    def set(self, i): self.bits[self.get(i)] = 1

    def a(self, i, ii):
        if self.bits[self.get(i)] is None or self.bits[self.get(ii)] is None:
            self.bits[self.get(i)] = None
        if self.bits[self.get(i)] == 1 and self.bits[self.get(ii)] == 1: self.set(i)
        if self.bits[self.get(i)] == 0 or self.bits[self.get(ii)] == 0: self.clear(i)

    def o(self, i, ii):
        if self.bits[self.get(i)] == 1 or self.bits[self.get(ii)] == 1: self.set(i)
        elif self.bits[self.get(i)] is None or self.bits[self.get(ii)] is None: self.bits[self.get(i)] = None

isReading = True
while(isReading):
    lines: int = int(input())
    if(lines == 0): 
        isReading = False
        break

    cpu = CISC()
    for i in range(lines):
        line = input().split()
        instruction = line[0]
        if(instruction == "SET"): cpu.set(int(line[1]))
        elif(instruction == "CLEAR"): cpu.clear(int(line[1]))
        elif(instruction == "AND"): cpu.a(int(line[1]), int(line[2]))
        elif(instruction == "OR"): cpu.o(int(line[1]), int(line[2]))

    output = ""
    for bit in cpu.bits:
        if bit is None: 
            output += "?"
            continue
        output += "0" if bit == 0 else "1"

    print(output)