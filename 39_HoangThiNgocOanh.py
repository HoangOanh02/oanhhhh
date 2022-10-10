class QuanLyHangHoa:
    def __init__(self, Mahang, Tenhang, Soluong, Gianhap, Giaban, Khuyenmai):
        self.Mahang = Mahang
        self.Tenhang = Tenhang
        self.Soluong = Soluong
        self.Gianhap = Gianhap
        self.Giaban = Giaban
        self.Khuyenmai = Khuyenmai

    def Tinhgiaban(self):
        if self.Soluong > 100:
            self.Giaban = self.Gianhap * (110/100)
        if 50 < self.Soluong < 100:
            self.Giaban = self.Gianhap * (115/100)
        if self.Soluong < 50:
            self.Giaban = self.Gianhap * (120/100)

MH1 = QuanLyHangHoa("M01", "Mì tôm Hảo Hảo", 100, 3000, "", 0)
MH2 = QuanLyHangHoa("D01", "Dầu ăn Tường An (1 lít)", 20, 40000, "", 0)


MH1.Tinhgiaban()
print('Giá nhập: {}'.format(MH1.Gianhap))
print('Giá bán: {}'.format(MH1.Giaban))



