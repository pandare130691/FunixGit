class NhanVien:
	def __init__(self, name, month, luong_coban, working_day, he_so_luong):
		self.name = name
		self.month = month
		self.luong_coban = luong_coban
		self.working_day = working_day
		self.heso = he_so_luong

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

class QuanLy(NhanVien):

	def __init__(self, name, month, luong_coban, working_day, he_so_luong, heso_hieuqua):
		super().__init__(name, month, luong_coban, working_day, he_so_luong)
		self.heso_hieuqua = heso_hieuqua
	
	def tinh_luong_thuong(self):
		self.tinh_luong()
		luong_thucnhan = 0
		if self.heso_hieuqua<1:
			luong_thucnhan = int(self.luong_nhan*self.heso_hieuqua)
		else:
			luong_thucnhan = int(self.luong_nhan * (self.heso_hieuqua-1))
		print('Luong cua nhan vien Nguyen Hai Phong nhan duoc trong thang '+self.month+' la: '+str(luong_thucnhan)+' VND.')

name = input('Ten nhan vien: ')
month = input('Thang: ')
luongcoban = int(input('luong co ban: '))
working_day = int(input('So ngay lam viec: '))
heso = float(input('he so luong: '))
heso_hieuqua = float(input('he so hieu qua: '))
nv = QuanLy(name, month, luongcoban, working_day, heso, heso_hieuqua)
nv.tinh_luong_thuong()
