import math

# --- HÀM HỖ TRỢ TÍNH TOÁN ---
def kiem_tra_nguyen_to(k):
    if k < 2: return False
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0: return False
    return True

def tinh_giai_thua(k):
    gt = 1
    for i in range(1, k + 1): gt *= i
    return gt

def tim_ucln(a, b):
    while b != 0: a, b = b, a % b
    return a

# --- CHƯƠNG TRÌNH CHÍNH (SỬ DỤNG KỸ THUẬT STRING) ---

# Bài 1: Kiểm tra đối xứng (Dùng đảo ngược chuỗi)
print("--- BÀI 1 ---")
n = int(input("Nhập n: "))
s = str(n) # Chuyển sang chuỗi
if s == s[::-1]: # Kỹ thuật cắt chuỗi (slicing) đặc trưng của Ch.8
    print(f"'{s}' là số đối xứng.")
else:
    print(f"'{s}' KHÔNG phải số đối xứng.")

# Bài 2: Tích số hoàn hảo
print("\n--- BÀI 2 ---")
n = int(input("Nhập n: "))
tich = 1
danh_sach_shh = [] # Dùng danh sách để lưu, sau đó xử lý chuỗi
for x in range(1, n):
    tong_uoc = 0
    for i in range(1, x):
        if x % i == 0: tong_uoc += i
    if tong_uoc == x:
        tich *= x
        danh_sach_shh.append(str(x)) # Lưu dưới dạng string để dùng join

if danh_sach_shh:
    # Dùng join để nối chuỗi - Kỹ thuật Ch.8
    chuoi_kq = ", ".join(danh_sach_shh) 
    print(f"Các số hoàn hảo tìm thấy: {chuoi_kq}")
    print(f"Tích của chúng là: {tich}")
else:
    print(f"Không có số hoàn hảo nào nhỏ hơn {n}.")

# Bài 3: Số nguyên tố trong khoảng [m, n]
print("\n--- BÀI 3 ---")
m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
kq_snt = []
for i in range(min(m, n), max(m, n) + 1):
    if kiem_tra_nguyen_to(i):
        kq_snt.append(str(i))

# Dùng join để in ra 1 chuỗi đẹp
print(f"Các số nguyên tố trong [{m}, {n}]: " + ", ".join(kq_snt))

# Bài 4: Số nguyên tố nhỏ hơn n
print("\n--- BÀI 4 ---")
n = int(input("Nhập n: "))
kq_snt_4 = []
for i in range(2, n):
    if kiem_tra_nguyen_to(i):
        kq_snt_4.append(str(i))
print(f"Các số nguyên tố nhỏ hơn {n}: " + ", ".join(kq_snt_4))

# Bài 5: Nguyên tố cùng nhau
print("\n--- BÀI 5 ---")
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
# Sử dụng f-string (định dạng chuỗi)
ket_luan = "LÀ" if tim_ucln(a, b) == 1 else "KHÔNG PHẢI"
print(f"Hai số {a} và {b} {ket_luan} nguyên tố cùng nhau.")

# Bài 6: Tính toán và định dạng chuỗi hiển thị
print("\n--- BÀI 6 ---")
n = int(input("Nhập n: "))
s2 = 0
s3 = 1
s4 = 0
tong_tu_s5 = 0

for k in range(1, n + 1):
    # S2
    tong_trong = sum(range(2, k + 1))
    if tong_trong > 0: s2 += tong_trong ** (1/5)
    # S3
    tong_mau = sum(range(1, k + 1))
    s3 *= (k / tong_mau)
    # S4
    s4 += (2 + tinh_giai_thua(k)) / tinh_giai_thua(k + 1)
    # S5
    tong_tu_s5 += tinh_giai_thua(k) ** (1/7)

s5 = tong_tu_s5 / tinh_giai_thua(n)

# Sử dụng định dạng chuỗi :.4f (làm tròn số thực trong chuỗi)
print(f"S1 = 0")print(f"S2 = {s2:.4f}")
print(f"S3 = {s3:.6f}")
print(f"S4 = {s4:.4f}")
print(f"S5 = {s5:.6f}")