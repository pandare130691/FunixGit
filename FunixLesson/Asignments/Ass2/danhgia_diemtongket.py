def xeploai_hocsinh():
	path = "trungbinh.txt"
	rf = open(path, encoding='utf8')
	output = {}
	lines = rf.readlines()
	for row in lines:
		try:
			cur = row.split(';')
			name = cur[0]
			math = cur[1]
			phys = cur[2]
			chem = cur[3]
			bio = cur[4]
			eng = cur[5]
			lit = cur[6]
			his = cur[7]
			geo = cur[8]
			dtb = (((float(math)+float(lit)+float(eng)) * 2+ float(phys)+float(chem)+float(bio)+float(his)+float(geo)))/11
			all_ps = [float(math), float(phys), float(chem), float(bio), float(eng), float(lit), float(his), float(geo)]
			output[name] = classify(dtb, all_ps)
		except:
			continue
	print(output)
	return output

def xeploai_thidaihoc_hocsinh(path):
	try:
		rf = open(path, encoding='utf8')
	except:
		print('Path co van de')
		return None
	data = {}
	lines = rf.readlines()
	index = 0
	for line in lines:
		if index>0:
			try:
				cur = line.split(';')
				t = {'math':float(cur[1]), 'phys':float(cur[2]), 'chem':float(cur[3]), 'bio':float(cur[4]), 'eng':float(cur[5]), 'lit':float(cur[6]), 'his':float(cur[7]), 'geo':float(cur[8])}
				data[cur[0]] = classifi_uni(t)
			except:
				continue
		index += 1
	print(data)
	return data

def classify(dtb, all_ps):
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
	
def classifi_uni(inp):
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

def main():
	pathin = input()
	pathout = input()
	xeploai_thidaihoc_hocsinh(pathin)

main()
