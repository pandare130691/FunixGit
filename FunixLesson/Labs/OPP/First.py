
class Student:
	name = ''
	dtb = 0
	def __init__(self, name, dtb):
		self.name = name
		self.dtb = dtb
	def print_dtb(self):
		print("The average mark of ", self.name, "is",  format(self.dtb, '.2f'))

student = "Phan Xuan Dung"
dtb = 9.5
my_obj = Student(student, dtb)
my_obj.print_dtb()