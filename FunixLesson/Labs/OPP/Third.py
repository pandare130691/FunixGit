'''
Kế thừa (inheritance) trong OOP
Đề bài: Tiếp tục với bài tập về phương thức ở task trước, ở bài này chúng ta sẽ tính lương cho một quản lý và in ra kết quả dựa theo lương nhận và hệ số hiệu quả. Hãy hoàn thiện các class NhanVien, QuanLy (kế thừa class NhanVien) và 3 phương thức tinh_luong, hien_thi_luong và tinh_luong_thuong.

Công thức tính lương cho quản lý: đồng.
Nếu lương tổng > 9 triệu VNĐ/tháng: Lương nhận chưa thưởng = 90% lương nhận.
Các trường hợp khác: Lương nhận chưa thưởng = lương tổng.
Nếu hệ số hiệu quả < 1: Lương thực nhận = lương nhận chưa thưởng * hệ số hiệu quả.
Các trường hợp khác: Lương thực nhận = lương nhận chưa thưởng * (hệ số hiệu quả - 1).

Nguyen Hai Dang
4 1000000 15 1.7 1.5

Luong cua nhan vien Nguyen Hai Dang nhan duoc trong thang 4 la: 47050000 VND.

ket qua lam tron ve int
'''

class NhanVien:

	def __init__(s, name, month , salary_per_day, day_of_working, coefficient):
		s.name = name
		s.month = month
		s.salary_per_day = salary_per_day
		s.day_of_working = day_of_working
		s.coefficient = coefficient

	def tinh_luong(s):
		#Lương tổng = Lương cơ bản x số ngày làm việc x hệ số lương - 1 triệu đồng.
		#Nếu lương tổng > 9 triệu VNĐ/tháng: Lương nhận chưa thưởng = 90% lương nhận.
		#Các trường hợp khác: Lương nhận chưa thưởng = lương tổng.
		luong_tong = s.salary_per_day * s.day_of_working*s.coefficient - 1000000
		if luong_tong>9000000:
			s.luong_nhan_chua_thuong = int(0.9*luong_tong)
		else:
			s.luong_nhan_chua_thuong = luong_tong

	def hien_thi_luong (s, real_salary):
		print("Luong cua nhan vien", s.name, "nhan duoc trong thang", s.month, "la:", int(real_salary), "VND.")

class QuanLy(NhanVien):

	def __init__(s, name, month, salary_basic, working_day, coeffi, performance):
		super().__init__(name, month, salary_basic, working_day, coeffi)
		s.performance = performance

	def tinh_luong_thuong(s):
		s.tinh_luong()
		if s.performance<1:
			real_salary = s.luong_nhan_chua_thuong * s.performance
		else:
			real_salary = s.luong_nhan_chua_thuong * (s.performance-1)
		return real_salary

name = "Nguyen Hai Quang"
m = 6
spd = 1000000
wd = 20
coe = 1.8
per = 1.9
quanly = QuanLy(name, m, spd, wd, coe, per)
real_salary = quanly.tinh_luong_thuong()
quanly.hien_thi_luong(real_salary)
