'''
Introduction to set
Đề bài: Phòng làm việc của trưởng phòng Yoon có 10 bạn nam. Yoon muốn tính chiều cao trung
bình của các số đo chiều cao khác nhau của các bạn trong phòng của mình. Bạn hãy viết chương
trình giúp Yoon xác định chiều cao trung bình này biết số đo của 10 bạn được nhập từ bàn phím
trên 1 dòng.
'''

def Act1():
	n = "1.74 1.74 1.80 1.67 1.59 1.59 1.80 1.73 1.73 1.80"
	lst = n.split()
	s = {float(value) for value in lst}
	print(format( sum(s)/len(s), ".2f"))
#Act1()

'''
Add method in Set
Đề bài: Mỗi tháng, giám đốc Yoon đi công tác qua 3-10 quốc gia, có những quốc gia Yoon bay
qua bay lại nhiều lần. Anh ấy muốn đếm tổng số các quốc gia khác nhau mà anh ấy đã đi qua
thông qua thông tin trên hộ chiếu. Áp dụng hàm set.add() để giúp Yoon thống kê số
quốc gia mà anh ấy đã đi qua.
'''
def Act2():
	n = input()
	lst = n.split()
	s = set()
	for c in lst:
		s.add(c)
	print(len(s))
#Act2()

'''
Remove method in Set
Đề bài: Cho một dãy số gồm các số tự nhiên và một dòng các lệnh remove cần được thực thi. Hãy
đưa dãy số tự nhiên này vào một set s, thực thi các lệnh remove ở dòng lệnh remove và in ra tổng các
phần tử còn lại trong set s. Nếu giá trị cần remove không có trong set s, bỏ qua giá trị ấy.
'''

def Act3():
	d1 = "1 7 21 6 1 9 1 7 6 22"
	r1 = "3 2 22 6 1"
	lstD = [int(v) for v in d1.split()]
	lstR = [int(v) for v in r1.split()]
	s = {v for v in lstD}
	for v in lstR:
		try:
			s.remove(v)
		except:
			continue
	print(sum(s))

#Act3()