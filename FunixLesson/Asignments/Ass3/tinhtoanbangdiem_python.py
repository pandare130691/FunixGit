import copy
import logging

class BANGDIEM:

	def __init__(self, path, path_out):
		self.path = path
		self.path_out = path_out
	
	def load_dulieu(self):
		try:
			data = open(self.path, encoding="utf8")
		except:
			print("Khong the doc file", self.path)
			return None
		lines = data.readlines()
		data.close()
		return lines

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
					aver_point = {"Toan": mathave, "Ly":physicalave, "Hoa": chemave, "Sinh": bioave, "Anh":engave, "Van":litave, "Su": hisave, "Dia":geoave}
					output[name] = aver_point
					i += 1
				except:
					logging.error("line " + str( i + 1) + " data khong dung cau truc")

		if(len(output)>0):
			rt = {}
			for k,v in output.items():
				citem = {}
				for k2,v2 in v.items():
					citem[k2] = format(v2, '.2f')
				rt[k] = citem
			return rt
		else:
			print("input data trống hoặc nhập không đúng định dạng chuẩn")
			return None

	def print_output(self, output):
		print(output)

	def luudiem_trungbinh(self, output):
		rd = copy.deepcopy(output)
		wf = open(self.path_out, mode='w', encoding="utf8")
		title = "Mã HS, Toán , Lý, Hóa, Sinh, Văn, Anh, Sử, Địa" + '\n'
		for uk, uv in rd.items():
			title += uk + ';'
			for k,v in uv.items():
			    title += v + ';'
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
				math = float(item['Toan'])
				phys = float(item['Ly'])
				chem = float(item['Hoa'])
				bio = float(item['Sinh'])
				eng = float(item['Anh'])
				lit = float(item['Van'])
				his = float(item['Su'])
				geo =float( item['Dia'])
				dtb = ((math+lit+eng) * 2+ phys+chem+bio+his+geo)/11
				all_ps = [math, phys, chem, bio,eng, lit, his, geo]
				if dtb>9 and len([c for c in all_ps if c<8])==0:
					output[cur] = 'Xuat sac'
				elif dtb > 8 and len([c for c in all_ps if  c<6.5])==0:
					output[cur] = 'Gioi'
				elif dtb > 6.5 and len([c for c in all_ps if c<5])==0:
					output[cur] = 'Kha'
				elif dtb > 6 and len([c for c in all_ps if c<4.5])==0:
					output[cur] = 'TB kha'
				else:
					output[cur] = 'TB'
			except:
				continue
		print(output)
		return output

	def xeploai_thidaihoc_hocsinh(self, bang_diem_tb):
		data = {}
		for k, inp in bang_diem_tb.items():
			try:
				a = 0
				a1 = 0
				b = 0
				c = 0
				d = 0
				#A
				a_p = float(inp['Toan'])+float(inp['Ly'])+float(inp['Hoa'])
				if a_p>=24:
					a = 1
				elif a_p <24 and a_p>=18:
					a = 2
				elif a_p <18 and a_p>=12:
					a = 3
				else:
					a = 4
				#A1
				a_p1 = float(inp['Toan'])+float(inp['Ly'])+float(inp['Anh'])
				if a_p1>=24:
					a1 = 1
				elif a_p1 <24 and a_p1>=18:
					a1 = 2
				elif a_p1 <18 and a_p1>=12:
					a1 = 3
				else:
					a1 = 4
				#B
				b_p = float(inp['Toan'])+float(inp['Hoa'])+float(inp['Sinh'])
				if b_p>=24:
					b = 1
				elif b_p <24 and b_p>=18:
					b = 2
				elif b_p <18 and b_p>=12:
					b = 3
				else:
					b = 4
				#C
				c_p = float(inp['Van'])+float(inp['Su'])+float(inp['Dia'])
				if c_p>=21:
					c = 1
				elif c_p <21 and c_p>=15:
					c = 2
				elif c_p <15 and c_p>=12:
					c = 3
				else:
					c = 4
				#D
				d_p = float(inp['Toan'])+float(inp['Van'])+float(inp['Anh'])*2
				if d_p>=32:
					d = 1
				elif d_p <32 and d_p>=24:
					d = 2
				elif d_p <24 and d_p>=20:
					d = 3
				else:
					d = 4
				data[k] = [a,a1,b,c,d]
			except:
				continue
		print(data)
		return data

class TUNHIEN(DANHGIA):

	def __init__(self, student):
		self.student = student

	def xeploai_thidaihoc_hocsinh(self):

		toan = float(self.student['Toan'])
		ly =  float(self.student['Ly'])
		hoa =  float(self.student['Hoa'])
		sinh =  float(self.student['Sinh'])
		anh =  float(self.student['Anh'])

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

		van = float(self.student['Van'])
		su = float(self.student['Su'])
		dia = float(self.student['Dia'])

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

		d_p = float(self.student['Toan'])+float(self.student['Van'])+float(self.student['Anh'])*2
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
	path_danhgia = input("Duong dan luu file danh_gia_hocsinh output: ")
	danh_gia = DANHGIA(path, path_out)
	data =	danh_gia.load_dulieu()
	if(data!=None):
		diemtb = danh_gia.tinhdiem_trungbinh(data)
		if(diemtb!=None):
			danh_gia.print_output(diemtb)
			danh_gia.luudiem_trungbinh(diemtb)
			luudiem_chitiet(path_dct, data)
			xeploai = danh_gia.xeploai_hocsinh(diemtb)
			xeploai_daihoc = danh_gia.xeploai_thidaihoc_hocsinh(diemtb)
			luudanhgia(path_danhgia, xeploai, xeploai_daihoc)
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

def luudanhgia( path_danhgia, xeploai, xeploai_thidaihoc):
	wf = open(path_danhgia, mode='w', encoding="utf8")
	title = 'Ma HS, xeploai_TB chuan, xeploai_A, xeploai_A1, xeploai_B, xeploai_C, xeploai_D\n'
	for k1,v1 in xeploai_thidaihoc.items():
		hocluc = ""
		for k2, v2 in xeploai.items():
			if k1==k2:
				hocluc = v2
				break
		title += k1 + "; " + hocluc + "; "
		for v in v1:
			title += str(v) + "; "
		title = title[0:-2] + "\n"
	wf.write(title)
	wf.close()

main()