class NhanVien:
	def __init__(self, name, month, luong_coban, working_day, he_so_luongluong):
		self.name = name
		self.month = month
		self.luong_coban = luong_coban
		self.working_day = working_day
		self.heso = he_so_luongluong

	def tinh_luong(self):
		'''
		Lương tổng = Lương cơ bản x số ngày làm việc x hệ số lương - 1 triệu đồng.
		Nếu lương tổng > 9 triệu VNĐ/tháng: Lương nhận = 90% lương nhận.
		Các trường hợp khác: Lương nhận = lương tổng.
		'''
		luong_tong = self.luong_coban * self.working_day * self.heso - 1000000
		if luong_tong>9000000:
			self.luong_nhan = int(luong_tong*0.9)
		else:
			self.luong_nhan = luong_tong
	
	def hien_thi_luong(self):
		print('Luong cua nhan vien '+self.name+' nhan duoc trong thang '+self.month+' la: '+str(self.luong_nhan)+' VND.')

name = input('Ten nhan vien: ')
month = input('Thang: ')
luongcoban = int(input('luong co ban: '))
working_day = int(input('So ngay lam viec: '))
heso = float(input('he so luong: '))
nv = NhanVien(name, month, luongcoban, working_day, heso)
nv.tinh_luong()
nv.hien_thi_luong()
