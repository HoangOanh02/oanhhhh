# Bài 1:
# class Animal:
#     def __init__(self, name):
#         self._name = name
#
#     def Display(self):
#         print("I'm {}".format(self._name))
#
#
# class Dog(Animal):
#     def __init__(self, name, size, age, color):
#         super().__init__(name)
#         self.size = size
#         self.age = age
#         self.color = color
#
#     def Go(self, place):
#         print("I'm going to {}".format(place))
#
# obj1 = Dog("bull", "large", 2, "yellow")
#
# obj1.Display()
# obj1.Go("garden")


# Bài 2:
class People:
    def __init__(self, Ma, Ten, NgaySinh, Sdt):
        self.Ma = Ma
        self.Ten = Ten
        self.NgaySinh = NgaySinh
        self.Sdt = Sdt
    def SuaSdt(self):
        SdtMoi = input("Nhap so dien thoai moi: ")
        self.Sdt = SdtMoi


class SinhVien(People):
    def __init__(self,Ma, Ten, NgaySinh, Sdt, DiemTL):
        super().__init__(Ma, Ten, NgaySinh, Sdt)
        self.DiemTL = DiemTL

    def TangDiemTL(self):
        DiemMoi = float(input("Nhập điểm mới:"))
        self.DiemTL = (DiemMoi + self.DiemTL)/2
        print("Điểm tích lũy: {}".format(self.DiemTL))


class GiangVien(People):
    def __init__(self,Ma, Ten, NgaySinh, Sdt, Luong):
        super().__init__(Ma, Ten, NgaySinh, Sdt)
        self.Luong = Luong

    def TangLuong(self):
        Luongmoi = int(input("\nNhập lương mới:"))
        self.Luong = self.Luong + Luongmoi
        print("Lương: {}".format(self.Luong))


SV1 = SinhVien("01", "Hoàng Oanh", "11/04/2002", "0987654321", 2.7)
GV1 = GiangVien("02", "Thanh Tâm", "22/08/4004", "0123456789", 3000)

SV1.TangDiemTL()
GV1.TangLuong()


# pravite, public đồ dô nghe
- DiemTL, Luong
+ TangDiemTL(), TangLuong()




# sửa sdt-tăng lương-tăng điểm