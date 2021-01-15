import logging
import copy

def tinhdiem_trungbinh(path):

	try:
		data = open(path, encoding="utf8")
	except:
		print("Khong the doc file", path)
		return None

	lines = data.readlines()
	output = {}
	if(len(lines) > 1):
		i = 1
		while i < len(lines):
			try:
				cur = lines[i].split(';')
				mahs = cur[0]
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
				output[mahs] = aver_point
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

	data.close()

def print_output(output):
	out = copy.deepcopy(output)
	for uk, uv in out.items():
		for k,v in uv.items():
			uv[k] = format(v, '.2f')
	print(out)

def luudiem_trungbinh(pathout, diemtb):
	rd = copy.deepcopy(diemtb)
	wf = open(pathout, mode='w', encoding="utf8")
	title = 'Mã HS, Toán , Lý, Hóa, Sinh, Văn, Anh, Sử, Địa\n'
	for uk, uv in rd.items():
		title += uk + ';'
		for k,v in uv.items():
				title += v+';'
		title = title[0:-1] + '\n'
	wf.write(title)
	wf.close()

def main():
	path = input("Đường dẫn cho diem_chitiet input file: ")
	path_out = input("Đường dẫn cho diem_trungbinh output file: ")
	diem_tb = tinhdiem_trungbinh(path)
	if(diem_tb!=None):
		luudiem_trungbinh(path_out, diem_tb)
		print("Lưu thành công")
	
main()