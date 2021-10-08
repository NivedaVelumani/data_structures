class Computer:
    def config(self):
        print("i5,ITB,16gb")

com1=Computer()
print(type(com1))

Computer.config(com1)
