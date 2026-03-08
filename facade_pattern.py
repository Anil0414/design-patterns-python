# facade_pattern.py

# Subsystems
class CPU:
    def start(self):
        print("CPU started")

class Memory:
    def load(self, data):
        print(f"Memory loaded with {data}")

class HardDrive:
    def read(self, sector):
        print(f"HardDrive reading sector {sector}")

# Facade
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hdd = HardDrive()

    def start_computer(self):
        self.cpu.start()
        self.memory.load("OS")
        self.hdd.read(100)
        print("Computer is ready to use!")

# Client code
if __name__ == "__main__":
    computer = ComputerFacade()
    computer.start_computer()