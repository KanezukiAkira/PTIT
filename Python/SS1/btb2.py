ho_ten = input("Nhap ho ten nhan vien: ")
gio_lam = float(input("Nhap so gio lam viec: "))
luong_gio = float(input("Nhap luong moi gio: "))
luong_thang = gio_lam * luong_gio
print(f"Luong thang cua nhan vien {ho_ten} la: {luong_thang}")


dtb = float(input("Nhap diem trung binh: "))
if dtb >= 8:
    print("Xep loai: Gioi")
elif dtb >= 6.5:
    print("Xep loai: Kha")
elif dtb >= 5:
    print("Xep loai: Trung binh")
else:
    print("Xep loai: Yeu")


don_gia = float(input("Nhap don gia: "))
so_luong = float(input("Nhap so luong: "))
tong_tien_hang = don_gia * so_luong
if tong_tien_hang > 500000:
    tong_tien_hang = tong_tien_hang * 0.9
print(f"So tien phai thanh toan: {tong_tien_hang} VND")


n_bai4 = int(input("Nhap so nguyen duong n: "))
tong_bai4 = 0
for i in range(1, n_bai4 + 1):
    tong_bai4 += i
print(f"Tong tu 1 den {n_bai4} la: {tong_bai4}")


n_bai5 = int(input("Nhap n: "))
dem_bai5 = 0
for i in range(1, n_bai5 + 1):
    if i % 3 == 0:
        dem_bai5 += 1
print(f"Co {dem_bai5} so tu 1 den {n_bai5} chia het cho 3.")


so_lan_nhap = 0
while so_lan_nhap < 3:
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "123456":
        print("Dang nhap thanh cong!")
        so_lan_nhap = -1
        break
    else:
        print("Sai thong tin dang nhap!")
        so_lan_nhap += 1
if so_lan_nhap == 3:
    print("Ban da nhap sai qua 3 lan. He thong khoa.")


tong_doanh_thu = 0.0
for i in range(7):
    val = float(input(f"Nhap doanh thu ngay {i + 1}: "))
    tong_doanh_thu += val
print(f"Tong doanh thu trong tuan la: {tong_doanh_thu}")


so_du = 10000000
so_tien_rut = int(input("Nhap so tien muon rut: "))
if so_tien_rut > so_du:
    print("Giao dich that bai: So du khong du.")
elif so_tien_rut % 50000 != 0:
    print("Giao dich that bai: So tien rut phai chia het cho 50.000.")
else:
    so_du -= so_tien_rut
    print(f"Rut tien thanh cong. So du con lai: {so_du} VND")


print("=== MENU ===\n1. Ca phe (25.000)\n2. Tra sua (35.000)\n3. Nuoc cam (30.000)")
lua_chon = int(input("Chon do uong (1-3): "))
if lua_chon < 1 or lua_chon > 3:
    print("Lua chon khong hop le.")
else:
    so_luong_do_uong = int(input("Nhap so luong: "))
    gia_don_vi = 0
    if lua_chon == 1:
        gia_don_vi = 25000
    elif lua_chon == 2:
        gia_don_vi = 35000
    elif lua_chon == 3:
        gia_don_vi = 30000
    tong_tien_cafe = gia_don_vi * so_luong_do_uong
    if tong_tien_cafe > 100000:
        tong_tien_cafe = tong_tien_cafe * 0.9
    print(f"Tong tien phai thanh toan: {tong_tien_cafe} VND")


n_bai10 = int(input("Nhap mot so nguyen: "))
if n_bai10 % 2 == 0:
    print(f"{n_bai10} la so chan.")
else:
    print(f"{n_bai10} la so le.")

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))
max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
print(f"So lon nhat la: {max_val}")

n_bai12 = int(input("Nhap so nguyen duong n: "))
if n_bai12 < 0:
    print("Khong the tinh giai thua cho so am.")
else:
    giai_thua = 1
    for i in range(1, n_bai12 + 1):
        giai_thua *= i
    print(f"{n_bai12}! = {giai_thua}")

so_bi_mat = 7
doan_dung = False
while doan_dung == False:
    du_doan = int(input("Nhap so ban doan: "))
    if du_doan == so_bi_mat:
        print(f"Chuc mung! Ban da doan dung so {so_bi_mat}.")
        doan_dung = True
    else:
        print("Chua chinh xac, vui long doan lai.")

so_km = float(input("Nhap so km khach da di: "))
if so_km <= 0:
    print("So km khong hop le.")
else:
    tong_tien_taxi = 0.0
    if so_km <= 1:
        tong_tien_taxi = 15000
    elif so_km <= 10:
        tong_tien_taxi = 15000 + (so_km - 1) * 12000
    else:
        tong_tien_taxi = 15000 + (9 * 12000) + (so_km - 10) * 10000
    print(f"Tong tien cuoc taxi phai tra la: {tong_tien_taxi} VND.")