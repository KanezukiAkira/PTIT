name = input("Nhập tên của bạn: ");
print("Hello, ",name);

age = input("Nhập tuổi: ");
print(f"You are {age} years old");

a = int(input("Nhập số thứ nhất"))
b = int(input("Nhập số thứ hai"))
print("Tổng: ", a + b);


a = int(input("Nhập chiều dài"))
b = int(input("Nhập chiều rộng"))
area = a*b
print("Diện tích hình chữ nhật: ", area);

print("--- Bài 5 ---")
name = "John"
age = 20
score = 8.5
is_student = True
print("Kiểu của name:", type(name))
print("Kiểu của age:", type(age))
print("Kiểu của score:", type(score))
print("Kiểu của is_student:", type(is_student))

print("\n--- Bài 6 ---")
r = float(input("Nhập bán kính r: "))
c = 2 * 3.14 * r
print("Chu vi hình tròn là:", c)

print("\n--- Bài 7 ---")
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
print("Phần nguyên của a chia b là:", a // b)
print("Phần dư của a chia b là:", a % b)

print("\n--- Bài 8 ---")
num = int(input("Nhập một số nguyên: "))
if num % 2 == 0:
    print(f"{num} là số chẵn")
else:
    print(f"{num} là số lẻ")

print("\n--- Bài 9 ---")
tuoi = int(input("Nhập tuổi: "))
if tuoi >= 16:
    print("đủ tuổi làm căn cước công dân")
else:
    print("không đủ tuổi")

print("\n--- Bài 10 & Bài 11 ---")
toan = float(input("Nhập điểm Toán: "))
van = float(input("Nhập điểm Văn: "))
anh = float(input("Nhập điểm Anh: "))
dtb = (toan + van + anh) / 3
print("Điểm trung bình:", dtb)

if dtb >= 8:
    print("Xếp loại: Good")
elif dtb >= 6.5:
    print("Xếp loại: Fair")
elif dtb >= 5:
    print("Xếp loại: Average")
else:
    print("Xếp loại: Weak")

print("\n--- Bài 12 ---")
so_a = float(input("Nhập số a: "))
so_b = float(input("Nhập số b: "))
so_c = float(input("Nhập số c: "))
print("Số lớn nhất là:", max(so_a, so_b, so_c))

print("\n--- Bài 13 ---")
nam = int(input("Nhập một năm: "))
if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
    print(f"{nam} là năm nhuận")
else:
    print(f"{nam} không phải là năm nhuận")

print("\n--- Bài 14 ---")
n = int(input("Nhập số nguyên dương n: "))
print(f"Các số từ 1 đến {n}:")
for i in range(1, n + 1):
    print(i, end=" ")
print()

print("\n--- Bài 15 ---")
n15 = int(input("Nhập số nguyên dương n: "))
tong = 0
for i in range(1, n15 + 1):
    tong += i
print(f"Tổng từ 1 đến {n15} là: {tong}")

print("\n--- Bài 16 ---")
n16 = int(input("Nhập một số nguyên n để in bảng cửu chương: "))
for i in range(1, 11):
    print(f"{n16} x {i} = {n16 * i}")

print("\n--- Bài 17 ---")
n17 = int(input("Nhập số nguyên dương n: "))
dem_chan = 0
for i in range(1, n17 + 1):
    if i % 2 == 0:
        dem_chan += 1
print(f"Từ 1 đến {n17} có {dem_chan} số chẵn")

print("\n--- Bài 18 ---")
chuoi = input("Nhập một chuỗi: ")
print("Độ dài của chuỗi là:", len(chuoi))

print("\n--- Bài 19 ---")
chuoi_19 = input("Nhập một chuỗi để kiểm tra đối xứng: ")
if chuoi_19 == chuoi_19[::-1]:
    print("Đây là chuỗi đối xứng")
else:
    print("Đây không phải là chuỗi đối xứng")