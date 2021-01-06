import copy
import logging

class BANGDIEM:

	def __init__(self, path, path_out):
		self.path = path
		self.path_out = path_out
	
	def load_dulieu(self):
		try:
			rf = open(self.path, encoding="utf8")
		except:
			print("Khong the doc file", path)
			return None
		lines = rf.readlines()
		return lines
		data.close()

	def tinhdiem_trungbinh(self, lines):
		output = {}
		if(len(lines) > 1):
			i = 1
			while i < len(lines):
				try:
					cur = lines[i].split(';')
					name = cur[0]
					math = (cur[1]).split(',')
					mathave = float(math[0]) * 0.05 + float(math[1]) * 0.1 + float(math[2]) * 0.15 + float(math[3]) * 0.7
					phys = (cur[2]).split(',')
					physicalave = float(phys[0]) * 0.05 + float(phys[1]) * 0.1 + float(phys[2]) * 0.15 + float(phys[3]) * 0.7
					chem = (cur[3]).split(',')
					chemave = float(chem[0]) * 0.05 + float(chem[1]) * 0.1 + float(chem[2]) * 0.15 + float(chem[3]) * 0.7
					bio = (cur[4]).split(',')
					bioave = float(bio[0]) * 0.05 + float(bio[1]) * 0.1 + float(bio[2]) * 0.15 + float(bio[3]) * 0.7
					eng = (cur[5]).split(',')
					engave = float(eng[0]) * 0.05 + float(eng[1]) * 0.1 + float(eng[2]) * 0.1 + float(eng[3]) * 0.15 + float(eng[4]) * 0.6
					lit = (cur[6]).split(',')
					litave = float(lit[0]) * 0.05 + float(lit[1]) * 0.1 + float(lit[2]) * 0.1 + float(lit[3]) * 0.15 + float(lit[4]) * 0.6
					his = (cur[7]).split(',')
					hisave = float(his[0]) * 0.05 + float(his[1]) * 0.1 + float(his[2]) * 0.1 + float(his[3]) * 0.15 + float(his[4]) * 0.6
					geo = (cur[8]).split(',')
					geoave = float(geo[0]) * 0.05 + float(geo[1]) * 0.1 + float(geo[2]) * 0.1 + float(geo[3]) * 0.15 + float(geo[4]) * 0.6
					aver_point = {"Toan": mathave, "Ly":physicalave, "Hoa": chemave, "Sinh": bioave, "Anh":engave, "Van":litave, "Su": chemave, "Dia":geoave}
					output[name] = aver_point
					i += 1
				except:
					logging.error("line " + str( i + 1) + " data khong dung cau truc")

		if(len(output)>0):
			return output
		else:
			print("input data trống hoặc nhập không đúng định dạng chuẩn")
			return None

	def print_output(self, output):
		out = copy.deepcopy(output)
		for uk, uv in out.items():
			for k,v in uv.items():
				uv[k] = format(v, '.2f')
		print(out)

	def luudiem_trungbinh(self, output):
		rd = copy.deepcopy(output)
		wf = open(self.path_out, mode='w', encoding="utf8")
		title = "Mã HS, Toán , Lý, Hóa, Sinh, Văn, Anh, Sử, Địa" + '\n'
		for uk, uv in rd.items():
			title += uk + ';'
			ic = len(uv)
			for k,v in uv.items():
					title += format(v, '.2f') + ';'
			title = title[0:-1] + '\n'
		wf.write(title)
		wf.close()

class DANHGIA(BANGDIEM):

	def __init__(self, path, path_out):
		super().__init__(path, path_out)

	def xeploai_hocsinh(self, bang_diem_tb):
		output = copy.deepcopy(bang_diem_tb)
		for k,item in output.items():
			try:
				cur = k
				math = item['Toan']
				phys = item['Ly']
				chem = item['Hoa']
				bio = item['Sinh']
				eng = item['Anh']
				lit = item['Van']
				his = item['Su']
				geo = item['Dia']
				dtk = ((math+lit+eng) * 2+ phys+chem+bio+his+geo)/11
				all_ps = [math, phys, chem, bio,eng, lit, his, geo]
				output[name] = classify(dtk, all_ps)
			except:
				continue
		print(output)
		return output

	def xeploai_thidaihoc_hocsinh(self, bang_diem_tb):
		data = {}
		for student in bang_diem_tb:
			try:
				data[cur[0]] = classifi_uni(student)
			except:
				continue
		print(data)
		return data

	def classify(self, dtb, all_ps):
		if dtb>9 and len([c for c in all_ps if c<8])==0:
			return 'Xuat sac'
		elif dtb > 8 and len([c for c in all_ps if  c<6.5])==0:
			return 'Gioi'
		elif dtb > 6.5 and len([c for c in all_ps if c<5])==0:
			return 'Kha'
		elif dtb > 6 and len([c for c in all_ps if c<4.5])==0:
			return 'TB kha'
		else:
			return 'TB'

	def classifi_uni(self, inp):
		a = 0
		a1 = 0
		b = 0
		c = 0
		d = 0
		#A
		a_p = inp['math']+inp['phys']+inp['chem']
		if a_p>=24:
			a = 1
		elif a_p <24 and a_p>=18:
			a = 2
		elif a_p <18 and a_p>=12:
			a = 3
		else:
			a = 4
		#A1
		a_p1 = inp['math']+inp['phys']+inp['eng']
		if a_p1>=24:
			a1 = 1
		elif a_p1 <24 and a_p1>=18:
			a1 = 2
		elif a_p1 <18 and a_p1>=12:
			a1 = 3
		else:
			a1 = 4
		#B
		b_p = inp['math']+inp['chem']+inp['bio']
		if b_p>=24:
			b = 1
		elif b_p <24 and b_p>=18:
			b = 2
		elif b_p <18 and b_p>=12:
			b = 3
		else:
			b = 4
		#C
		c_p = inp['lit']+inp['his']+inp['geo']
		if c_p>=21:
			c = 1
		elif c_p <21 and c_p>=15:
			c = 2
		elif c_p <15 and c_p>=12:
			c = 3
		else:
			c = 4
		#D
		d_p = inp['math']+inp['lit']+inp['eng']*2
		if d_p>=32:
			d = 1
		elif d_p <32 and d_p>=24:
			d = 2
		elif d_p <24 and d_p>=20:
			d = 3
		else:
			d = 4

		return [a,a1,b,c,d]

class TUNHIEN(DANHGIA):

	def __init__(self, student):
		self.student = student

	def xeploai_thidaihoc_hocsinh(self):

		toan = self.student['Toan']
		ly = self.student['Ly']
		hoa = self.student['Hoa']
		sinh = self.student['Sinh']
		anh = self.student['Anh']

		a_p = toan + ly + hoa
		if a_p>=24:
			a = 1
		elif a_p <24 and a_p>=18:
			a = 2
		elif a_p <18 and a_p>=12:
			a = 3
		else:
			a = 4

		a_p1 = toan + ly + anh
		if a_p1>=24:
			a1 = 1
		elif a_p1 <24 and a_p1>=18:
			a1 = 2
		elif a_p1 <18 and a_p1>=12:
			a1 = 3
		else:
			a1 = 4

		b_p =  toan + hoa + sinh
		if b_p>=24:
			b = 1
		elif b_p <24 and b_p>=18:
			b = 2
		elif b_p <18 and b_p>=12:
			b = 3
		else:
			b = 4

		return [a, a1, b]

class XAHOI(DANHGIA):

	def __init__(self, student):
		self.student = student

	def xeploai_thidaihoc_hocsinh(self):

		van = self.student['Van']
		su = self.student['Su']
		dia = self.student['Dia']

		c_p = van + su + dia
		if c_p>=21:
			c = 1
		elif c_p <21 and c_p>=15:
			c = 2
		elif c_p <15 and c_p>=12:
			c = 3
		else:
			c = 4

		return c

class COBAN(DANHGIA):

	def __init__(self, student):
		self.student = student

	def xeploai_thidaihoc_hocsinh(self):

		d_p = self.student['Toan']+self.student['Van']+self.student['Anh']*2
		if d_p>=32:
			d = 1
		elif d_p <32 and d_p>=24:
			d = 2
		elif d_p <24 and d_p>=20:
			d = 3
		else:
			d = 4

		return d


def main():
	path = input("Duong dan file diem_chitiet: ")
	path_out = input("Duong dan luu file diem_trungbinh output: ")
	path_dct = input("Duong dan luu file diem_chitiet output: ")
	danh_gia = DANHGIA(path, path_out)
	data =	danh_gia.load_dulieu()
	if(data!=None):
		diemtb = danh_gia.tinhdiem_trungbinh(data)
		if(diemtb!=None):
			danh_gia.print_output(diemtb)
			danh_gia.luudiem_trungbinh(diemtb)
			luudiem_chitiet(path_dct, data)
			danh_gia.xeploai_hocsinh(diemtb)
			tdh = {}
			for k,v in diemtb.items():
				tn = TUNHIEN(v).xeploai_thidaihoc_hocsinh()
				tn.append(XAHOI(v).xeploai_thidaihoc_hocsinh())
				tn.append(COBAN(v).xeploai_thidaihoc_hocsinh())
				tdh[k] = tn
			print(tdh)

def luudiem_chitiet(path, data):
		wf = open(path, mode='w', encoding="utf8")
		wf.writelines(data)
		wf.close()

main()


