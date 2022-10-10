class NhanVien:
    def __init__(self, MaNV, HoTen, HeSoLuong):
        self.MaNV = MaNV
        self.HoTen = HoTen
        self.HeSoLuong = HeSoLuong
    def TinhLuong(self):
        print("Lương tính theo từng vị trí CV:")

class GiaoVien(NhanVien):
    def __init__(self, MaNV, HoTen,HeSoLuong,HeSoCV,SoNamKN):
        super().__init__(MaNV, HoTen,HeSoLuong)
        self.HeSoCV = HeSoCV
        self.SoNamKN = SoNamKN
    def TinhLuong(self):
        self.Luong = (self.HeSoLuong +self.HeSoCV + self.SoNamKN / 5) *  1200000
        print(self.Luong)

class GiaoVu(NhanVien):
    def __init__(self, MaNV, HoTen,HeSoLuong,HeSoCV):
        super().__init__(MaNV, HoTen, HeSoLuong)
        self.HeSoCV = HeSoCV
    def TinhLuong(self):
        self.Luong = ( self.HeSoLuong + self.HeSoCV ) * 1200000
        print(self.Luong)


GVien = GiaoVien("01", "Nhan vien A", 4,5, 7)
GVu = GiaoVu("02", "Giao vu B",15, 9)

GVien.TinhLuong()
GVu.TinhLuong()