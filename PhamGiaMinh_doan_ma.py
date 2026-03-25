# DẠNG 1: BIẾN VÀ QUY TẮC ĐẶT TÊN
# ------------------------------------------------------------------------------

print("\n--- DẠNG 1 ---")
# Bài 1: Khai báo biến ma_sinh_vien và in ra giá trị
ma_sinh_vien = "20230101" 
print(f"1. Mã sinh viên: {ma_sinh_vien}")

# Bài 2: Khai báo biến _diem_tong_ket là số thực. In kiểu dữ liệu.
_diem_tong_ket = 7.9 
print(f"2. Kiểu dữ liệu của _diem_tong_ket: {type(_diem_tong_ket)}")

# Bài 3: Khai báo nhiều biến trên cùng một dòng.
ten, tuoi, gioi_tinh = "An", 20, "Nam"
print(f"3. Thông tin: Tên: {ten}, Tuổi: {tuoi}, Giới tính: {gioi_tinh}")

# Bài 4: Khai báo biến temp_C và gán lại giá trị.
temp_C = 25.5 
temp_C = 30.0 
print(f"4. Giá trị mới của temp_C: {temp_C}")


# ------------------------------------------------------------------------------
# DẠNG 2: KIỂU DỮ LIỆU CƠ BẢN
# ------------------------------------------------------------------------------

print("\n--- DẠNG 2 ---")
# Bài 1: Phân biệt int, float, str.
so_nguyen = 15      
so_thuc = 15.0      
chuoi = "15"        
print(f"1. Kiểu của 15: {type(so_nguyen)}, Kiểu của 15.0: {type(so_thuc)}, Kiểu của '15': {type(chuoi)}")

# Bài 2: Kiểm tra 100 == 100.0 (Boolean).
print(f"2. 100 có bằng 100.0: {100 == 100.0}") 

# Bài 3: Nối first_name và last_name.
first_name = "Minh"
last_name = "Anh"
full_name = first_name + " " + last_name
print(f"3. Tên đầy đủ: {full_name}")

# Bài 4: Phép chia chuẩn (/) và chia nguyên (//).
phep_tinh_chia = 10 / 2
phep_tinh_nguyen = 10 // 2
print(f"4. 10/2: {phep_tinh_chia} ({type(phep_tinh_chia)}), 10//2: {phep_tinh_nguyen} ({type(phep_tinh_nguyen)})") 

# Bài 5: Khai báo Boolean và in câu.
gioi_tinh_nam = True 
print(f"5. Giới tính của người dùng là nam: {gioi_tinh_nam}")


# ------------------------------------------------------------------------------
# DẠNG 3: NHẬP, ÉP KIỂU VÀ ĐỊNH DẠNG
# ------------------------------------------------------------------------------

print("\n--- DẠNG 3 ---")
# Bài 1: Nhập chuỗi số và chuỗi chữ. Ép kiểu chuỗi số thành int.
chuoi_so = input("Bài 3.1: Nhập một chuỗi số: ")
chuoi_chu = input("Bài 3.1: Nhập một chuỗi chữ: ")
so_nguyen = int(chuoi_so)
print(f"1. Chuỗi số (int): {so_nguyen}, Chuỗi chữ: {chuoi_chu}")

# Bài 2: Nhập hai số nguyên.
so_a = int(input("Bài 3.2: Nhập số nguyên thứ nhất: "))
so_b = int(input("Bài 3.2: Nhập số nguyên thứ hai: "))print(f"2. Đã nhập: {so_a} và {so_b}")

# Bài 3: Nhập tên loài vật. In ra câu bằng f-strings.
ten_loai_vat = input("Bài 3.3: Nhập tên một loài vật: ")
print(f"3. Loài vật tôi thích nhất là {ten_loai_vat}.")

# Bài 4: Tính TB và định dạng 2 chữ số sau dấu phẩy bằng .format().
toan = float(input("Bài 3.4: Nhập điểm môn Toán: "))
van = float(input("Bài 3.4: Nhập điểm môn Văn: "))
diem_trung_binh = (toan + van) / 2
print("4. Điểm trung bình cộng: {0:.2f}".format(diem_trung_binh))

# Bài 5: In chieu_cao (1 chữ số) và can_nang (1 chữ số) bằng toán tử %.
chieu_cao = 1.75
can_nang = 65
print("5. Chiều cao là %.1f mét và cân nặng là %.1f kg." % (chieu_cao, can_nang))