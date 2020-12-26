import math as m

# a)
def kiemtra_tamgiac(input):
    ab = m.sqrt((input[2] - input[0]) ** 2 + (input[3] - input[1]) ** 2)
    ac = m.sqrt((input[4] - input[0]) ** 2 + (input[5] - input[1]) ** 2)
    bc = m.sqrt((input[4] - input[2]) ** 2 + (input[5] - input[3]) ** 2)
    if ab +bc == ac or ac + bc == ab or ab + ac == bc or bc + ac == ab or ac + ab == bc or bc + ab == ac:
        return False
    else:
        return True

# b)
def goccanh_tamgiac(input):

	ab = m.sqrt((input[2] - input[0]) ** 2 + (input[3] - input[1]) ** 2)
	ac = m.sqrt((input[4] - input[0]) ** 2 + (input[5] - input[1]) ** 2)
	bc = m.sqrt((input[4] - input[2]) ** 2 + (input[5] - input[3]) ** 2)

	if ab + bc == ac or ac + bc == ab or ab + ac == bc or bc + ac == ab or ac + ab == bc or bc + ab == ac:
		return []
	else:
		gc = m.acos(-1 * (ab ** 2 - ac ** 2 - bc ** 2) / (2 * bc * ac))
		gb = m.acos(-1 * (ac ** 2 - bc ** 2 - ab ** 2) / (2 * bc * ab))
		ga = m.acos(-1 * (bc ** 2 - ab ** 2 - ac ** 2) / (2 * ab * ac))
		kq = [round(ab, 2), round(bc,2), round(ac,2), round(ga * 180 / m.pi, 2), round(gb * 180 / m.pi, 2), round(gc * 180 / m.pi, 2)]
		return kq

# c)
def xet_tamgiac(input):
	ab = m.sqrt((input[2] - input[0]) ** 2 + (input[3] - input[1]) ** 2)
	ac = m.sqrt((input[4] - input[0]) ** 2 + (input[5] - input[1]) ** 2)
	bc = m.sqrt((input[4] - input[2]) ** 2 + (input[5] - input[3]) ** 2)

	if ab + bc == ac or ac + bc == ab or ab + ac == bc or bc + ac == ab or ac + ab == bc or bc + ab == ac:
		return "Khong phai la tam giac"
	else:
		gc = 180 / m.pi * (m.acos(-1 * (ab ** 2 - ac ** 2 - bc ** 2) / (2 * bc * ac)))
		gb = 180 / m.pi * (m.acos(-1 * (ac ** 2 - bc ** 2 - ab ** 2) / (2 * bc * ab)))
		ga = 180 / m.pi * (m.acos(-1 * (bc ** 2 - ab ** 2 - ac ** 2) / (2 * ab * ac)))
		if ab == bc and bc == ac:
			return "ABC là tam giac deu"
		elif ab == ac and ga == 90:
			return "ABC la tam giac vuong can tai dinh A"
		elif ab == bc and gb == 90:
			return "ABC la tam giac vuong can tai dinh B"
		elif ac == bc and gc == 90:
			return "ABC la tam giac vuong can tai dinh C"
		elif ab == ac and ga > 90:
			return "ABC la tam giac tu va can tai dinh A"
		elif ab == bc and gb > 90:
			return "ABC la tam giac tu va can tai dinh B"
		elif ac == bc and gc > 90:
			return "ABC la tam giac tu va can tai dinh C"
		elif ab == ac and ga < 90:
			return "ABC là tam giac can tai dinh A"
		elif ab == bc and gb < 90:
			return "ABC là tam giac can tai dinh B"
		elif ac == bc and gc > 90:
			return "ABC là tam giac can tai dinh C"
		elif ga == 90:
			return "ABC la tam giac vuong tai dinh A va la tam giac vuong"
		elif gb == 90:
			return "ABC la tam giac vuong tai dinh B va la tam giac vuong"
		elif gc == 90:
			return "ABC la tam giac vuong tai dinh C va la tam giac giac vuong"
		elif ga > 90:
			return "ABC la tam giac tu tai dinh A va la tam giac binh thuong"
		elif gb > 90:
			return "ABC la tam giac tu tai dinh B va la tam giac binh thuong"
		elif gc > 90:
			return "ABC la tam giac tu tai dinh C va la tam giac binh thuong"
		else:
			return "ABC la tam giac nhon tai dinh A/B/C va la tam giac binh thuong"

# d)
def dientich_tamgiac(input):
	ab = m.sqrt((input[2] - input[0]) ** 2 + (input[3] - input[1]) ** 2)
	ac = m.sqrt((input[4] - input[0]) ** 2 + (input[5] - input[1]) ** 2)
	bc = m.sqrt((input[4] - input[2]) ** 2 + (input[5] - input[3]) ** 2)
	# Heron: sqrt (p*(p-a)*(p-b)*(p-c))
	p = 1 / 2 * (ab + bc + ac)
	gt = m.sqrt(p * (p - ab) * (p - bc) * (p - ac))
	return round(gt, 2)

# e)
def duongcao_tamgiac(input):
	ab = m.sqrt((input[2] - input[0]) ** 2 + (input[3] - input[1]) ** 2)
	ac = m.sqrt((input[4] - input[0]) ** 2 + (input[5] - input[1]) ** 2)
	bc = m.sqrt((input[4] - input[2]) ** 2 + (input[5] - input[3]) ** 2)
	p = 1 / 2 * (ab + bc + ac)
	cA = round(2 * m.sqrt(p*(p-ab)*(p-ac)*(p-bc)) / bc, 2)
	cB = round(2 * m.sqrt(p*(p-ab)*(p-ac)*(p-bc)) / ac, 2)
	cC = round(2 * m.sqrt(p*(p-ab)*(p-ac)*(p-bc)) / ab, 2)
	return [cA, cB, cC]

# f)
def trungtuyen_tamgiac(input):
	ab = m.sqrt((input[2] - input[0]) ** 2 + (input[3] - input[1]) ** 2)
	ac = m.sqrt((input[4] - input[0]) ** 2 + (input[5] - input[1]) ** 2)
	bc = m.sqrt((input[4] - input[2]) ** 2 + (input[5] - input[3]) ** 2)
	a = 2 * (ab ** 2 + ac ** 2) - bc**2
	a2 = a/4
	a3 = m.sqrt(a2)
	a4 = a3 * 2/3
	ttA = round(2 / 3 *m.sqrt(((2 * (ab ** 2 + ac ** 2) - bc ** 2)/4)),2)
	ttB = round(2 / 3 * m.sqrt((2 * (ab ** 2 + bc ** 2) - ac ** 2)/4), 2)
	ttC = round(2 / 3 * m.sqrt((2 * (ac ** 2 + bc ** 2) - ab ** 2)/4), 2)
	return  [ttA, ttB, ttC]

# g)
def tam_tamgiac(input):
	xA = input[0]
	yA = input[1]
	xB = input[2]
	yB = input[3]
	xC = input[4]
	yC = input[5]
	# trong tam G
	xG = (xA + xB+ xC)/3;
	yG = (yA + yB+ yC)/3;
	# truc tam H (xH, yH)
	'''
	vector AB = (xB - xa, yb-ya)
	vector BC = (xc - xb, yc-yb)
	vector CH = (xh - xc, yh - yc)
	vector AH = (xh - xa, yh - ya)
	AH* BC = 0 <=> xg * (xc - xb) + yg * (yc - yb) = xa * (xc - xb) + ya * (yc - yb)
	CH* AB = 0 <=> xg * (xb - xa) + yg * (yb - ya) = xc * (xb - xa) + yc * (yb - ya)
	'''
	tgt = giaiphuongtrinh(xC-xB, yC-yB, xA * (xC - xB) + yA * (yC - yB), xB-xA, yB-yA, xC*(xB-xA)+yC*(yB-yA))

	return  [xG, yG, tgt[0], tgt[1]]

def giaiphuongtrinh(a1, b1, c1, a2, b2, c2):
	d = a1*b2 - a2*b1
	dx = c1*b2 - c2*b1
	dy = a1*c2 - a2*c1
	if(d==0):
		if dx==dy==0:
			return [1,2,3,4] #vo so nghiem
		else:
			return [] #vo nghiem
	else:
		return [dx/d, dy/d]

def giaima_tamgiac(input):
	kttg = kiemtra_tamgiac(input)
	if kttg:
		print('A, B, C hop thanh mot tam giac')
		gctg =	goccanh_tamgiac(input)
		print('1. So do co ban cua tam giac:')
		print('Chieu dai canh AB:', gctg[0])
		print('Chieu dai canh BC:', gctg[1])
		print('Chieu dai canh CA:', gctg[2])
		print('Goc A:', gctg[3])
		print('Goc B:', gctg[4])
		print('Goc C:', gctg[5])
		print(xet_tamgiac(input))
		print("2. Dien tich cua tam giac ABC:",  dientich_tamgiac(input))
		print("3. So do nang cao tam giac ABC:")
		tdc = duongcao_tamgiac(input)
		print("Do dai duong cao tu dinh A:", tdc[0] )
		print("Do dai duong cao tu dinh B:", tdc[1] )
		print("Do dai duong cao tu dinh C:", tdc[2] )
		ttt = trungtuyen_tamgiac(input)
		print("Khoang cach den trong tam tu dinh A:", ttt[0] )
		print("Khoang cach den trong tam tu dinh B:", ttt[1] )
		print("Khoang cach den trong tam tu dinh C:", ttt[2] )
		ttg = tam_tamgiac(input)
		print("4. Toa do mot so diem dac biet cua tam giac ABC:" )
		print("Toa do trong tam:", ttg[0], ttg[1] )
		print("Toa do truc tam:", ttg[2], ttg[3] )

	else:
		print('A, B, C khong hop thanh mot tam giac')

giaima_tamgiac([0,0, 0, 4, 3,0])