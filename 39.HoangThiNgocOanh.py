# Bài 1:
class SinhVien:
    def __init__(self, MaSV, TenSV, NgaySinh, Lop, DiemTichLuy, Sdt):
        self.MaSV = MaSV
        self.TenSV = TenSV
        self.NgaySinh = NgaySinh
        self.Lop = Lop
        self.DiemTichLuy = DiemTichLuy
        self.Sdt = Sdt

    def InThongTinSV(self):
        print(self.MaSV, self.TenSV, self.NgaySinh, self.Lop, self.DiemTichLuy, self.Sdt )

    def XepLoai(self):
      if self.DiemTichLuy >= 3.5:
          print("Xuất sắc")
      elif 3.2 <= self.DiemTichLuy < 3.5:
          print("Giỏi")
      elif 2.5 <= self.DiemTichLuy < 3.2:
          print("Khá")
      elif 2 <= self.DiemTichLuy < 2.5:
          print("Trung bình")
      else:
          print("Kém")

    def SuaThongTinSV(self):
        self.Sdt = input( )
        print("Cập nhật thành công")

# Bài 2:
SV1 = SinhVien("201112345", "Nguyễn Tiến Thành", "12/10/2002", "45K14", 3.4, "")
SV2 = SinhVien("201112346", "Phùng Lê Na", "05/06/2001", "45K14", 1.9, "")
SV3 = SinhVien("201112347", "Trần Văn Hùng", "07/11/2002", "45K21.1", 2.3, "")

print("Xếp loại học lực của sinh viên Nguyễn Tiến Thành:")
SV1.XepLoai()

print("Cập nhật số điện thoại mới của Phùng Lê Na:")
SV2.SuaThongTinSV()

print("In thông tin của 3 sinh viên:")
SV1.InThongTinSV()
SV2.InThongTinSV()
SV3.InThongTinSV()
