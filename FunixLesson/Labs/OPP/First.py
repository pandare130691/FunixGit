
class Student:
	name = ''
	dtb = 0
	def __init__(self, name, toan, ly, hoa):
		self.name = name
		self.toan = toan
		self.ly = ly
		self.hoa = hoa
	def print_dtb(self):
		dtb = (self.toan + self.ly + self.hoa)/3
		print("The average mark of ", self.name, "is",  format(dtb, '.2f'))

name = input('Ten cua ban: ')
toan = int(input('Toan: '))
ly = int(input('Ly: '))
hoa = int(input('Hoa: '))
my_o = Student(name, toan, ly, hoa)
my_o.print_dtb()
