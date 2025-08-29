
danh_sach_nv = []
danh_sach_sp = []
danh_sach_ncc = []
danh_sach_kh = []
hang_can_xuat = []
def nhan_vien():
    while True:
        print("\n============== Thông tin nhân viên ============")
        print("1. Nhập thông tin nhân viên")
        print("2. Cập nhật thông tin")
        print("3. Thoát")
        try:
            lua_chon_nv = int(input("Chọn: "))
        except ValueError:
            print("Vui lòng nhập lại giá trị phù hợp !")
        if lua_chon_nv == 1:
            slnv = int(input("\nNhập vào số lượng nhân viên: "))
            for i in range(slnv):
                print(f"\n========== Nhân viên thứ {i + 1} ===========")
                mnv = input("Nhập mã nhân viên: ")
                ho_ten = input("Nhập họ và tên: ")
                dia_chi = input("Nhập địa chỉ: ")
                sdt = input("Nhập số điện thoại: ")
                while True:
                    try:
                        ten_kho = input("Làm việc tại kho A / B: ")
                        if ten_kho in ["Kho A", "Kho B"]:
                            break
                        else:
                            print("Vui lòng chỉ chọn kho A / B")
                    except ValueError:
                        print("Vui lòng chỉ chọn kho A / B")
                while True:
                    try:
                        chuc_vu = input("Chức vụ: ")
                        if chuc_vu in ["Quản lý", "Nhân viên"]:
                            break
                        else:
                            print("Vui lòng chỉ chọn nhân viên / quản lý")
                    except ValueError:
                        print("Vui lòng chỉ chọn nhân viên / quản lý")

                danh_sach_nv.append(
                    {
                        "Mã nhân viên": mnv,
                        "Họ và tên": ho_ten,
                        "Địa chỉ": dia_chi,
                        "Số điện thoại": sdt,
                        "Tên kho": ten_kho,
                        "Chức vụ": chuc_vu,
                    }
                )
                with open("File.txt", "w", encoding="utf-8") as f:
                    f.write(
                        "\n============================= Danh sách nhân viên ==========================\n"
                    )
                    f.write(
                        "--------------------------------------------------------------------------------------------------------------------------\n"
                    )
                    f.write(
                        "| STT | Mã nhân viên     | Họ và tên         | Địa chỉ               | Số điện thoại    | Tên Kho         | Chức vụ      |\n"
                    )
                    f.write(
                        "|-----|------------------|-------------------|-----------------------|------------------|-----------------|--------------|\n"
                    )

                    for i, nv in enumerate(danh_sach_nv, start=1):
                        f.write(
                            f"|{i:<5}|{nv['Mã nhân viên']:<18}|{nv['Họ và tên']:<19}|{nv['Địa chỉ']:<23}|{nv['Số điện thoại']:<18}|{nv['Tên kho']:<17}|{nv['Chức vụ']:14}|\n"
                        )
                        f.write(
                            "|-----|------------------|-------------------|-----------------------|------------------|-----------------|--------------|\n"
                        )
        elif lua_chon_nv == 2:
            cap_nhat_tt()
        elif lua_chon_nv == 3:
            if kiem_tra_thoat() == True:
                break
        else:
            print("Vui lòng nhập đúng giá trị !")
            
def cap_nhat_tt():
    while True:
        print("\n=============== Menu ==============")
        print("1. Xóa theo thứ tự bạn chọn")
        print("2. Xóa toàn bộ")
        print("3. Thêm thông tin")
        print("4. Sửa thông tin")
        print("5. Hiển thị")
        print("6. Thoát")

        try:
            lua_chon = int(input("Chọn: "))
        except ValueError:
            print("Vui lòng nhập số nguyên.")
            continue

        if lua_chon == 1:
            try:
                n = int(input("Nhập vào thứ tự nhân viên cần xóa: "))
                if 1 <= n <= len(danh_sach_nv):
                    del danh_sach_nv[n - 1]
                    print("Đã xóa nhân viên.")
                else:
                    print("Thứ tự không hợp lệ.")
            except ValueError:
                print("Vui lòng nhập số nguyên.")
        elif lua_chon == 2:
            danh_sach_nv.clear()
            print("Đã xóa toàn bộ danh sách.")
        elif lua_chon == 5:
            hien_thi_nv()
        elif lua_chon == 6:
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")
            
def menu_hien_thi():
    while True:
        print("\n =============== Hiển thị ============")
        print("1. Hiển thị thông tin nhân viên")
        print("2. Hiển thị thông tin sản phẩm")
        print("3. Hiển thị thông tin nhà cung cấp")
        print("4. Quay lại")


        try:
            lua_chon_hien_thi = int(input("Chọn: "))
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")
            continue
        if lua_chon_hien_thi == 1:
            hien_thi_nv()
        elif lua_chon_hien_thi == 2:
            hien_thi_sp()
        elif lua_chon_hien_thi == 3:
            hien_thi_ncc()
        elif lua_chon_hien_thi == 4:
            if kiem_tra_thoat() == True:
                break
        else:
            print("Lựa chọn không hợp lệ!")

def kiem_tra_thoat():
    while True:
        print("\n========= Menu ==========")
        print("1. Đồng ý thoát")
        print("2. Không đồng ý thoát")
        try:
            thoat = int(input("Chọn: "))
            if thoat == 1:
                return True
            elif thoat == 2:
                return False
            else:
                print("Chỉ chọn 1 & 2")
        except ValueError:
            print("Vui lòng nhập đúng giá trị !")

if __name__ == "__main__":   
    while True:
        print("============== Menu ==============")
        print("1. Quản lý nhân viên")
        print("2. Quản lý sản phẩm")
        print("3. Cập nhật kho hàng")
        print("4. Tìm kiếm / lọc sản phẩm")
        print("5. Nhà cung cấp")
        print("6. Hiển thị thông tin")
        print("7. Thoát")
        lua_chon = int(input("Chọn: "))
        if lua_chon == 1:
            nhan_vien()
        elif lua_chon == 2:
            
        elif lua_chon == 3:
        
        elif lua_chon == 4:
        
        elif lua_chon == 5:
            
        elif lua_chon == 6:
            menu_hien_thi()
        elif lua_chon == 7:
            if kiem_tra_thoat() == True:
                break