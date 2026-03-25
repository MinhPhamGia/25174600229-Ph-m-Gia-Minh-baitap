# ====================================================================
# BÀI TẬP TỔNG HỢP: TOÁN TỬ SỐ HỌC, SO SÁNH & LOGIC (TUÂN THỦ QUI ĐỊNH)
# ====================================================================

# -------------------------- BÀI 1: CHI PHÍ & VAT --------------------------
print("\n=== BÀI 1: TÍNH CHI PHÍ VÀ THUẾ VAT ===")
try:
    gia_san_pham = float(input("Nhập giá sản phẩm (VNĐ): "))
    so_luong = int(input("Nhập số lượng mua: "))
    
    # Toán tử Số học
    tong_chi_phi = gia_san_pham * so_luong
    thue_vat = tong_chi_phi * 0.1
    tong_tien_phai_tra = tong_chi_phi + thue_vat
    
    print(f"Tổng tiền phải trả: {round(tong_tien_phai_tra, 2):,.2f} VNĐ")
except ValueError:
    print("Lỗi nhập liệu ở Bài 1.")

# -------------------------- BÀI 2: CHIA KẸO -------------------------------
print("\n=== BÀI 2: CHIA KẸO ===")
try:
    tong_so_keo = int(input("Nhập tổng số kẹo: "))
    so_hoc_sinh = int(input("Nhập số học sinh: "))
    
    # Toán tử // và %
    keo_moi_hoc_sinh = tong_so_keo // so_hoc_sinh
    keo_con_thua = tong_so_keo % so_hoc_sinh
    
    print(f"Số kẹo mỗi học sinh nhận được: {keo_moi_hoc_sinh} viên")
    print(f"Số kẹo còn thừa: {keo_con_thua} viên")
except (ValueError, ZeroDivisionError):
    print("Lỗi nhập liệu ở Bài 2.")

# -------------------------- BÀI 3: DIỆN TÍCH TAM GIÁC ---------------------
print("\n=== BÀI 3: DIỆN TÍCH TAM GIÁC ===")
try:
    canh_day = float(input("Nhập độ dài cạnh đáy (cm): "))
    chieu_cao = float(input("Nhập chiều cao (cm): "))
    
    dien_tich = (canh_day * chieu_cao) / 2
    
    print(f"Diện tích tam giác là: {dien_tich:.2f} cm²")
except ValueError:
    print("Lỗi nhập liệu ở Bài 3.")

# -------------------------- BÀI 4: CHUYỂN ĐỔI TIỀN TỆ ---------------------
print("\n=== BÀI 4: CHUYỂN ĐỔI TIỀN TỆ (VNĐ sang USD) ===")
try:
    ty_gia_usd = 24500.0
    so_tien_vnd = float(input("Nhập số tiền VNĐ: "))
    
    so_tien_usd = so_tien_vnd / ty_gia_usd
    
    print(f"{so_tien_vnd:,.0f} VNĐ tương đương với {round(so_tien_usd, 2):,.2f} USD")
except ValueError:
    print("Lỗi nhập liệu ở Bài 4.")

# -------------------------- BÀI 5: TÍNH LÃI ĐƠN ---------------------------
print("\n=== BÀI 5: TÍNH LÃI ĐƠN ===")
try:
    so_tien_gui = float(input("Nhập số tiền gửi ban đầu (VNĐ): "))
    lai_suat_nam = float(input("Nhập lãi suất hàng năm (vd: 0.06 cho 6%): "))
    
    lai_1_thang = so_tien_gui * lai_suat_nam * (1 / 12)
    lai_2_quy = so_tien_gui * lai_suat_nam * (2 / 4)
    lai_3_nam = so_tien_gui * lai_suat_nam * 3
    
    print(f"Lãi nhận được sau 3 năm: {lai_3_nam:,.0f} VNĐ")
except ValueError:
    print("Lỗi nhập liệu ở Bài 5.")

# -------------------------- BÀI 6: KIỂM TRA NĂM NHUẬN ---------------------print("\n=== BÀI 6: KIỂM TRA NĂM NHUẬN ===")
try:
    nam = int(input("Nhập một năm: "))
    
    # Toán tử Logic (and, or) và So sánh
    chia_het_400 = (nam % 400 == 0)
    chia_het_4_va_khong_100 = (nam % 4 == 0) and (nam % 100 != 0)
    la_nam_nhuan = chia_het_400 or chia_het_4_va_khong_100
    
    print(f"Năm {nam} có phải là năm nhuận không: {la_nam_nhuan}")
except ValueError:
    print("Lỗi nhập liệu ở Bài 6.")

# -------------------------- BÀI 7: KIỂM TRA QUYỀN TRUY CẬP ----------------
print("\n=== BÀI 7: KIỂM TRA QUYỀN TRUY CẬP ===")
ten_dang_nhap = input("Nhập tên đăng nhập: ")
mat_khau = input("Nhập mật khẩu: ")

# Toán tử Logic (and) và So sánh
dieu_kien_ten = (ten_dang_nhap == "admin")
dieu_kien_mat_khau = (mat_khau != "password123")
quyen_truy_cap = dieu_kien_ten and dieu_kien_mat_khau

print(f"Quyền truy cập được cấp: {quyen_truy_cap}")

# -------------------------- BÀI 8: TÍNH CHỈ SỐ BMI ------------------------
print("\n=== BÀI 8: TÍNH CHỈ SỐ BMI ===")
try:
    can_nang = float(input("Nhập cân nặng (kg): "))
    chieu_cao = float(input("Nhập chiều cao (mét): "))
    
    bmi = can_nang / (chieu_cao * chieu_cao)
    
    print(f"Chỉ số BMI của bạn là: {round(bmi, 2)}")
except (ValueError, ZeroDivisionError):
    print("Lỗi nhập liệu ở Bài 8.")

# -------------------------- BÀI 9: TÍNH TIỀN ĐIỆN -------------------------
print("\n=== BÀI 9: TÍNH TIỀN ĐIỆN (DÙNG BOOLEAN LOGIC) ===")
try:
    kwh = int(input("Nhập số kWh điện đã tiêu thụ: "))
    
    # Định nghĩa giá
    GIA_BAC1 = 1678
    GIA_BAC2 = 1734
    GIA_BAC3 = 2014

    # Tính lượng tiêu thụ ở mỗi bậc dùng Boolean Arithmetic
    luong_bac1 = kwh * (kwh <= 100) + 100 * (kwh > 100)
    luong_thua_bac1 = kwh - 100
    luong_bac2 = luong_thua_bac1 * (luong_thua_bac1 > 0 and luong_thua_bac1 <= 100) + 100 * (luong_thua_bac1 > 100)
    luong_thua_bac2 = kwh - 200
    luong_bac3 = luong_thua_bac2 * (luong_thua_bac2 > 0 and luong_thua_bac2 <= 100) + 100 * (luong_thua_bac2 > 100)
    
    tong_tien = (luong_bac1 * GIA_BAC1) + (luong_bac2 * GIA_BAC2) + (luong_bac3 * GIA_BAC3)
    
    print(f"Tổng số tiền điện phải trả: {tong_tien:,.0f} VNĐ")
except ValueError:
    print("Lỗi nhập liệu ở Bài 9.")

# -------------------------- BÀI 10: TÍNH LƯƠNG ----------------------------
print("\n=== BÀI 10: TÍNH LƯƠNG THỰC NHẬN (DÙNG BOOLEAN LOGIC) ===")
try:
    luong_co_ban = float(input("Nhập mức lương cơ bản (VNĐ): "))
    ngay_cong = int(input("Nhập số ngày công trong tháng: "))
    
    luong_ngay = luong_co_ban / 22
    luong_chinh_thuc = luong_ngay * ngay_cong

    # Tính thưởng/phạt dùng Boolean Arithmetic
    tien_thuong = luong_chinh_thuc * 0.10 * (ngay_cong > 22)
    tien_phat = luong_chinh_thuc * 0.05 * (ngay_cong < 22)luong_thuc_nhan = luong_chinh_thuc + tien_thuong - tien_phat
    
    print(f"Tổng tiền lương thực nhận: {luong_thuc_nhan:,.0f} VNĐ")
except (ValueError, ZeroDivisionError):
    print("Lỗi nhập liệu ở Bài 10.")