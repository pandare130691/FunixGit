class NhanVien:

	name = ''
	month = 0
	salary_per_day = 0
	day_of_working = 0
	coefficient = 0
	luong_nhan = 0

	def __init__(s, name, month , salary_per_day, day_of_working, coefficient):
		s.name = name
		s.month = month
		s.salary_per_day = salary_per_day
		s.day_of_working = day_of_working
		s.coefficient = coefficient

	def tinh_luong(s):
		#Lương cơ bản x số ngày làm việc x hệ số lương - 1 triệu đồng.
		#Nếu lương tổng > 9 triệu VNĐ/tháng: Lương nhận = 90% lương nhận.
		#Các trường hợp khác: Lương nhận = lương tổng.
		luong_tong = s.salary_per_day * s.day_of_working*s.coefficient - 1000000
		if luong_tong>9000000:
			s.luong_nhan = int(0.9*luong_tong)
		else:
			s.luong_nhan = luong_tong

	def hien_thi_luong (s):
		#Luong cua nhan vien Nguyen Hai Phong nhan duoc trong thang 3 la: 12600000 VND.
		print("Luong cua nhan vien", s.name, "nhan duoc trong thang", s.month, "la:", s.luong_nhan, "VND.")

#Input: "Nguyen Hai Phong", "3 500000 20 1.5"
#"Luong cua nhan vien Nguyen Hai Phong nhan duoc trong thang 3 la: 12600000 VND."

name = "Nguyen Hai Phong"
month = 3
spd = 500000
dw = 20
hsl = 1.5
nv = NhanVien(name, month, spd, dw, hsl)
nv.tinh_luong()
nv.hien_thi_luong()
