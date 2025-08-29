import json
print("Quản lý kho hàng hàng")
danh_sach_nv = []
danh_sach_sp = []
danh_sach_ncc = []
danh_sach_kh = []
hang_can_xuat = []
danh_sach_dki = []
with open("login.json", "r", encoding = "utf-8") as f:
        danh_sach_dki = json.load(f)
def in_thong_tin_hh(hh, stt = 1):
    print("\n========= Thông tin hàng hóa ===========")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("|STT   | Mã hàng hóa       | Tên hàng                | Kho                 | Đơn vị tính        | Số lượng         | Hạn sử dụng   | Giá bán       |")
    print("|------|-------------------|-------------------------|---------------------|--------------------|------------------|---------------|---------------|")
    print(f"|{stt:<6} {hh['Mã hàng hóa']:<19} {hh['Tên hàng hóa']:<26} {hh['Kho']:<18} {hh['Đơn vị tính']:<20} {hh['Số lượng']:<18} {hh['Hạn sử dụng']:<18} {hh['Giá bán']:<18}")
    print("|--------------------------------------------------------------------------------------------------------------------------------------------------------------|")


def in_thong_tin_nv(nv, stt = 1):
    print("\n ===== Thông tin nhân viên ======")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("|STT   | Mã nhân viên       | Họ và tên                 | Địa chỉ           | Số điện thoại           | Kho               | Chức vụ          |")
    print("|------|--------------------|---------------------------|-------------------|-------------------------|-------------------|------------------|")
    print(f"|{stt:<6}| {nv['Mã nhân viên']:<19}| {nv['Họ và tên']:<26}| {nv['Địa chỉ']:<18}| {nv['Số điện thoại']:<24}| {nv['Tên kho']:<18}| {nv['Chức vụ']:<16}|")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")


def hien_thi_nv():
    with open("dsnv.json", "r", encoding = "utf-8") as f:
        danh_sach_nv = json.load(f)
    print("\n ===== Thông tin nhân viên ======")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("|STT   | Mã nhân viên       | Họ và tên                 | Địa chỉ           | Số điện thoại           | Kho               | Chức vụ          |")
    print("|------|--------------------|---------------------------|-------------------|-------------------------|-------------------|------------------|")
    for i, nv in enumerate(danh_sach_nv, start = 1):
        print(f"|{i:<6}| {nv['Mã nhân viên']:<19}| {nv['Họ và tên']:<26}| {nv['Địa chỉ']:<18}| {nv['Số điện thoại']:<24}| {nv['Tên kho']:<18}| {nv['Chức vụ']:<16}|")
        print("|-------------------------------------------------------------------------------------------------------------------------------------------|")


def hien_thi_sp():
    with open("dssp.json", "r", encoding = "utf-8") as f:
        danh_sach_sp = json.load(f)
    print("\n========= Thông tin hàng hóa ===========")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("|STT   | Mã hàng hóa       | Tên hàng                | Kho                 | Khối lượng         | Số lượng         | Hạn sử dụng   | Giá bán       |")
    print("|------|-------------------|-------------------------|---------------------|--------------------|------------------|---------------|---------------|")
    for i, hh in enumerate(danh_sach_sp, start = 1):
        print(f"|{i:<6} {hh['Mã hàng hóa']:<19} {hh['Tên hàng hóa']:<26} {hh['Kho']:<18} {hh['Khối lượng']:<20} {hh['Số lượng']:<18} {hh['Hạn sử dụng']:<18} {hh['Giá bán']:<18}")
        print("|--------------------------------------------------------------------------------------------------------------------------------------------------------------|")


def hien_thi_ncc():
    with open("dsncc.json", "r", encoding = "utf-8") as f:
        danh_sach_ncc = json.load(f)
    print("\n ================== Thông tin nhà cung cấp ====================")
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print("| STT  | Mã nhà cung cấp       | Tên nhà cung cấp           | Địa chỉ                | Số điện thoại       | Email                        |")
    print("|------|-----------------------|----------------------------|------------------------|---------------------|------------------------------|")
    for i, ncc in enumerate(danh_sach_ncc, start = 1):
        print(f"| {i:<4}| {ncc['Mã nhà cung cấp']:<23}| {ncc['Tên nhà cung cấp']:<27}| {ncc['Địa chỉ nhà cung cấp']:<25}| {ncc['Số điện thoại']:<22}| {ncc['Email']:<28}|")
        print("|---------------------------------------------------------------------------------------------------------------------------------------------")


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


def them_thong_tin():
    print(f"\n========== Thêm nhân viên ===========")
    #Cái này phải đọc file 
    try:
        with open("dsnv.json", "r", encoding="utf-8") as f:
            danh_sach_nv_hien_tai = json.load(f)
            
    except FileNotFoundError:
        danh_sach_nv_hien_tai = []
        print("Không tìm thấy file dsnv.json hoặc file trống/lỗi.")

    mnv = input("Nhập mã nhân viên: ")
    ho_ten = input("Nhập họ và tên: ")
    dia_chi = input("Nhập địa chỉ: ")
    sdt = input("Nhập số điện thoại: ")

    while True:
        ten_kho = input("Làm việc tại Kho A / Kho B: ")
        if ten_kho in ["Kho A", "Kho B"]:
            break
        else:
            print("Vui lòng chỉ chọn Kho A hoặc Kho B")

    while True:
        chuc_vu = input("Chức vụ (Nhân viên / Quản lý): ")
        if chuc_vu in ["Nhân viên", "Quản lý"]:
            break
        else:
            print("Vui lòng chỉ chọn Nhân viên hoặc Quản lý")

    nhan_vien_moi = {
        "Mã nhân viên": mnv,
        "Họ và tên": ho_ten,
        "Địa chỉ": dia_chi,
        "Số điện thoại": sdt,
        "Tên kho": ten_kho,
        "Chức vụ": chuc_vu
    }
    danh_sach_nv_hien_tai.append(nhan_vien_moi)

    with open("dsnv.json", "w", encoding="utf-8") as f:
        json.dump(danh_sach_nv_hien_tai, f, ensure_ascii=False, indent=4)

    print("Thêm nhân viên thành công và đã lưu vào file!")


def sua_thong_tin():
    print("========== Sửa thông tin ==========")
    try:
        with open("dsnv.json", "r", encoding="utf-8") as f:
            danh_sach_nv = json.load(f)
    except FileExistsError:
        print("Không tìm thấy file hoặc file đang trống/lỗi.")
        return
    if not danh_sach_nv:
        print("Danh sách nhân viên đang trống. Không có gì để sửa")
        return
    
    hien_thi_nv()
    
    mnv_can_sua = input("\nNhập mã nhân viên cần sửa đổi: ")
    tim_thay = False
    
    for nv in danh_sach_nv:
        if nv["Mã nhân viên"] == mnv_can_sua:
            tim_thay = True
            print(f"Đã tìm thấy nhân viên có mã {nv['Mã nhân viên']}.")
            in_thong_tin_nv(nv)
            
            ho_ten_moi = input(f"Nhập họ và tên mới ({nv['Họ và tên']}): ")
            if ho_ten_moi:
                nv["Họ và tên"] = ho_ten_moi

            dia_chi_moi = input(f"Nhập địa chỉ mới({nv['Địa chỉ']}): ")
            if dia_chi_moi:
                nv["Địa chỉ"] = dia_chi_moi

            sdt_moi = input(f"Nhập số điện thoại mới ({nv['Số điện thoại']}): ")
            if sdt_moi:
                nv["Số điện thoại"] = sdt_moi

            while True:
                ten_kho_moi = input(f"Làm việc tại Kho A / Kho B ({nv['Tên kho']}): ")
                if not ten_kho_moi: 
                    break
                if ten_kho_moi in ["Kho A", "Kho B"]:
                    nv["Tên kho"] = ten_kho_moi
                    break
                else:
                    print("Vui lòng chỉ chọn Kho A hoặc Kho B")

            while True:
                chuc_vu_moi = input(f"Chức vụ (Nhân viên / Quản lý) ({nv['Chức vụ']}): ")
                if not chuc_vu_moi: 
                    break
                if chuc_vu_moi in ["Nhân viên", "Quản lý"]:
                    nv["Chức vụ"] = chuc_vu_moi
                    break
                else:
                    print("Vui lòng chỉ chọn Nhân viên hoặc Quản lý")

            with open("dsnv.json", "w", encoding="utf-8") as f:
                json.dump(danh_sach_nv, f, ensure_ascii=False, indent=4)

            print("\nThông tin nhân viên đã được cập nhật và lưu vào file!")
            break 

    if not tim_thay:
        print(f"Không tìm thấy nhân viên với mã '{mnv_can_sua}'.")

def cap_nhat_tt():
    try:
        with open("dsnv.json", "r", encoding="utf-8") as f:
            danh_sach_nv = json.load(f)
    except FileNotFoundError:
        danh_sach_nv = []
        print("Không tìm thấy file hoặc file đang trống/lỗi.")
        
    while True:
        print("\n=============== Menu ==============")
        print("1. Xóa theo thứ tự bạn chọn")
        print("2. Xóa toàn bộ")
        print("3. Thêm nhân viên")
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
                    
                    with open("dsnv.json", "w", encoding="utf-8") as f:
                        json.dump(danh_sach_nv, f, ensure_ascii=False, indent=4)
                    print("Đã lưu thay đổi vào file.")
                    
                else:
                    print("Thứ tự không hợp lệ.")
            except ValueError:
                print("Vui lòng nhập số nguyên.")
                
        elif lua_chon == 2:
            danh_sach_nv.clear()
            print("Đã xóa toàn bộ danh sách.")
        elif lua_chon == 3:
            them_thong_tin()
        elif lua_chon == 4:
            sua_thong_tin()
        elif lua_chon == 5:
            hien_thi_nv()
        elif lua_chon == 6:
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")


def tim_kiem():
    while True:
        print("\n================ Menu tìm kiếm =================")
        print("1. Tìm kiếm nhân viên")
        print("2. Tìm kiếm nhà cung cấp")
        print("3. Tìm kiếm Hàng hóa")
        print("4. Thoát")
        lua_chon = int(input("Chọn: "))
        if lua_chon == 1:
            tim_thay = False
            mnv_tk = input("\nNhập mã nhân viên cần tìm kiếm: ")
            for nv in danh_sach_nv:
                if nv["Mã nhân viên"] == mnv_tk:
                    tim_thay = True
                    print("\nNhân viên tìm được:")
                    in_thong_tin_nv(nv)
                    break
            if not tim_thay:
                print("Không có nhân viên nào trong danh sách")
        elif lua_chon == 3:
            tim_thay = False
            mhh_tk = input("\nNhập mã hàng hóa cần tìm kiếm: ")
            for hh in danh_sach_kh:
                if hh["Mã hàng hóa"] == mhh_tk:
                    tim_thay = True
                    in_thong_tin_hh(hh)
                    break
                if not danh_sach_kh:
                    print(f"Không tồn tại mã hàng hóa {mhh_tk}")
        elif lua_chon == 4:
            if kiem_tra_thoat() == True:
                break


def thong_tin_khac():
    while True:
        print("\n======== Menu ========")
        print("1. Tìm kiếm thông tin")
        print("2. Tồn kho")
        print("3. Xuất kho")
        print("5. Thoát")
        try:
            lua_chon = int(input("Chọn: "))
            if lua_chon == 1:
                tim_kiem()
            elif lua_chon == 2:
                ton_kho()
            elif lua_chon == 3:
                xuat_kho()
            elif lua_chon == 5:
                kiem_tra_thoat()
                break
        except ValueError:
            print("Giá trị không hợp lệ vui lòng nhập lại !")


def ton_kho():
    print("============== Tồn kho ================")
    print("1. Kho A")
    print("2. Kho B")
    print("3. Thoát")
    lua_chon = int(input("Chọn: "))
    if lua_chon == 1:
        ten_kho = "Kho A"
    elif lua_chon == 2:
        ten_kho = "Kho B"
    else:
        print("Lựa chọn không hợp lệ !")
    danh_sach_tim_dc = [hh for hh in danh_sach_sp if hh["Kho"] == ten_kho]
    if not danh_sach_tim_dc:
        print("Không có sản phẩm nào trong kho !")
    print("\n========= Thông tin hàng hóa ===========")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("|STT   | Mã hàng hóa       | Tên hàng                | Kho                 | Khối lượng (Kg)    | Số lượng         | Hạn sử dụng   | Giá bán       |")
    print("|------|-------------------|-------------------------|---------------------|--------------------|------------------|---------------|---------------|")
    for i, hh in enumerate(danh_sach_tim_dc, start = 1):
        print(f"|{i:<6}| {hh['Mã hàng hóa']:<19}| {hh['Tên hàng hóa']:<26}| {hh['Kho']:<18}| {hh['Khối lượng']:<20}| {hh['Số lượng']:<18}| {hh['Hạn sử dụng']:<18}| {hh['Giá bán']:<18}|")
        print("|--------------------------------------------------------------------------------------------------------------------------------------------------------------|")


def xuat_kho():
    thong_tin_kh = {}
    da_nhap_hh = False
    hang_can_xuat = None

    while True:
        print("\n============== Xuất kho ================")
        print("1. Nhập vào thông tin khách hàng")
        print("2. Nhập vào hàng cần xuất")
        print("3. Xuất kho")
        print("4. Thoát")

        try:
            lua_chon = int(input("Chọn: "))
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")
            continue

        if lua_chon == 1:
            print("\n=============== Thông tin khách hàng ===============")
            mkh = input("Nhập mã khách hàng: ")
            ten_kh = input("Nhập họ tên: ")
            dia_chi_kh = input("Địa chỉ: ")
            try:
                khoang_cach = float(input("Khoảng cách: "))
            except ValueError:
                print("Khoảng cách phải là số.")
                continue

            thong_tin_kh = {
                "Mã khách hàng": mkh,
                "Tên khách hàng": ten_kh,
                "Địa chỉ": dia_chi_kh,
                "Khoảng cách": khoang_cach,
            }
            danh_sach_kh.append(thong_tin_kh)
            print("→ Đã lưu thông tin khách hàng.")

        elif lua_chon == 2:
            print("\n======= Hàng cần xuất =========")
            ma_hh = input("Nhập mã hàng hóa: ")
            try:
                so_luong_xuat = int(input("Nhập số lượng cần xuất: "))
            except ValueError:
                print("Số lượng phải là số nguyên.")
                continue

            hang_can_xuat = None
            for hh in danh_sach_sp:
                if hh["Mã hàng hóa"] == ma_hh:
                    hang_can_xuat = hh
                    break

            if not hang_can_xuat:
                print(f"Không tồn tại mã hàng hóa: {ma_hh}.")
            else:
                if hang_can_xuat["Số lượng"] < so_luong_xuat:
                    print(
                        f"Không đủ hàng. Chỉ còn {hang_can_xuat['Số lượng']} sản phẩm."
                    )
                else:
                    hang_can_xuat["Số lượng"] -= so_luong_xuat
                    da_nhap_hh = True
                    print(
                        f">> Đã xuất {so_luong_xuat} sản phẩm '{hang_can_xuat['Tên hàng hóa']}'."
                    )
                if thong_tin_kh and "Khoảng cách" in thong_tin_kh:
                    toc_do_giao_hang = 50
                    thoi_gian_giao = thong_tin_kh["Khoảng cách"] / toc_do_giao_hang
                    print(f">> Thời gian dự kiến giao hàng: {thoi_gian_giao:.2f} giờ.")
                else:
                    print("Chưa có thông tin khách hàng để tính thời gian giao hàng.")
        elif lua_chon == 3:
            if not thong_tin_kh:
                print("Vui lòng nhập thông tin khách hàng trước.")
            elif not da_nhap_hh:
                print("Vui lòng chọn hàng cần xuất trước.")
            else:
                print(">> Xuất kho hoàn tất. (Tùy chọn: Lưu hóa đơn nếu cần.)")

        elif lua_chon == 4:
            print(">> Đã thoát khỏi chức năng xuất kho.")
            break
        else:
            print("Lựa chọn không hợp lệ!")
            
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
            try:
                slnv = int(input("\nNhập vào số lượng nhân viên: "))
            except ValueError:
                print("Vui lòng nhập vào giá trị hợp lệ !")
                continue
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
                            print("Vui lòng chỉ chọn (nhân viên / quản lý)")
                    except ValueError:
                        print("Vui lòng chỉ chọn (nhân viên / quản lý)")

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
                with open("dsnv.json", "w", encoding = "utf-8") as f:
                    json.dump(danh_sach_nv, f, ensure_ascii = False, indent = 4 )
        elif lua_chon_nv == 2:
            cap_nhat_tt()
        elif lua_chon_nv == 3:
            if kiem_tra_thoat() == True:
                break
        else:
            print("Vui lòng nhập đúng giá trị !")


def hang_hoa():
    while True:
        print("\n============ Hàng hóa ============")
        print("1. Nhập thông tin hàng hóa")
        print("2. Thoát")
        try:
            lua_chon_hh = int(input("Chọn: "))
        except ValueError:
            print("Vui lòng nhập lại giá trị hợp lệ !")
            continue

        if lua_chon_hh == 1:
            slhh = int(input("Nhập vào số lượng loại hàng hóa: "))
            for i in range(slhh):
                print(f"\n======== Hàng hóa thứ {i + 1} ==========")
                mshh = input("Nhập vào mã hàng hóa: ")
                ten_hh = input("Nhập tên hàng hóa: ")

                while True:
                    kho_hang = input("Nhập kho A / B: ")
                    if kho_hang in ["Kho A", "Kho B"]:
                        break
                    else:
                        print("Chỉ được nhập Kho A / B")

                while True:
                    try:
                        khoi_luong = float(input("Khối lượng (kg): "))
                        if khoi_luong > 0:
                            break
                        else:
                            print("Vui lòng nhập lại!")
                    except ValueError:
                        print("Vui lòng nhập lại!")

                while True:
                    try:
                        so_luong_hh = int(input("Nhập số lượng: "))
                        if so_luong_hh > 0:
                            break
                        else:
                            print("Vui lòng nhập lại!")
                    except ValueError:
                        print("Vui lòng nhập lại!")

                while True:
                    try:
                        han_su_dung = int(input("Hạn sử dụng (Số ngày): "))
                        if han_su_dung > 0:
                            break
                        else:
                            print("Vui lòng nhập lại!")
                    except ValueError:
                        print("Vui lòng nhập lại!")

                while True:
                    try:
                        gia_ban = float(input("Giá bán: "))
                        if gia_ban > 0:
                            break
                        else:
                            print("Vui lòng nhập lại!")
                    except ValueError:
                        print("Vui lòng nhập lại!")

                danh_sach_sp.append(
                    {
                        "Mã hàng hóa": mshh,
                        "Tên hàng hóa": ten_hh,
                        "Kho": kho_hang,
                        "Khối lượng": khoi_luong,
                        "Số lượng": so_luong_hh,
                        "Hạn sử dụng": han_su_dung,
                        "Giá bán": gia_ban
                    }
                )

            with open("dssp.json", "w", encoding="utf-8") as f:
                json.dump(danh_sach_sp, f, ensure_ascii=False, indent=4)
                print("Đã cập nhật sản phẩm thành công.")
        elif lua_chon_hh == 2:
            if kiem_tra_thoat() == True:
                break
        else:
            print("Lựa chọn không hợp lệ!")

def nha_cung_cap():
    while True:
        print("\n=============== Nhà cung cấp ================")
        print("1. Nhập thông tin nhà cung cấp")
        print("2. Cập nhật thông tin")
        print("3. Thoát")
        try:
            lua_chon_cc = int(input("Chọn: "))
        except ValueError:
            print("Vui lòng nhập một số hợp lệ!")
            continue
        if lua_chon_cc == 1:
            try:
                slncc = int(input("Nhập vào số lượng nhà cung cấp: "))
            except ValueError:
                print("Số lượng không hợp lệ !")
                continue
            for i in range(slncc):
                print(f"\n========== Nhà cung cấp thứ {i + 1} ==========")
                ma_ncc = input("Nhập vào mã nhà cung cấp: ")
                ten_nha_cc = input("Nhập tên: ")
                dia_chi_cc = input("Nhập địa chỉ:  ")
                sdt_cc = input("Nhập số điện thoại: ")
                email_cc = input("Nhập email: ")
                danh_sach_ncc.append(
                    {
                        "Mã nhà cung cấp": ma_ncc,
                        "Tên nhà cung cấp": ten_nha_cc,
                        "Địa chỉ nhà cung cấp": dia_chi_cc,
                        "Số điện thoại": sdt_cc,
                        "Email": email_cc,
                    }
                )
                with open("dsncc.json", "w", encoding = "utf-8") as f:
                    json.dump(danh_sach_ncc, f, ensure_ascii = False, indent = 4) 
        elif lua_chon_cc == 3:
            if kiem_tra_thoat() == True:
                break
        else:
            print("Lựa chọn không hợp lệ!")
            
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
def khanh_hang():
    while True:
        print("\n===== MENU =====")
        print("1. Xem thông tin hàng hóa")
        print("2. Thoát")
        lua_chon = input("Chọn: ")

        if lua_chon == "1":
            ton_kho()
        elif lua_chon == "2":
            if kiem_tra_thoat() == True:
                break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
    
def admin():
    while True:
        print("\n============= MENU ==============")
        print("1. Quản lý nhân viên")
        print("2. Quản lý hàng hóa")
        print("3. Nhà cung cấp")
        print("4. Hiển thị")
        print("5. Một số thông tin khác")
        print("6. Thoát")
        lua_chon = int(input("Chọn: "))

        if lua_chon == 1:
            nhan_vien()
        elif lua_chon == 2:
            hang_hoa()
        elif lua_chon == 3:
            nha_cung_cap()
        elif lua_chon == 4:
            menu_hien_thi()
        elif lua_chon == 5:
            thong_tin_khac()
        elif lua_chon == 6:
            if kiem_tra_thoat() == True:
                break

if __name__ == "__main__":
    while True:
        print("\n=========== Đăng nhập ===========")
        print("1. Đăng nhập")
        print("2. Đăng kí")
        print("3. Thoát")
        lua_chon = int(input("Chọn: "))
        
        if lua_chon == 1:
            ten_tai_khoan = input("Tên tài khoản: ")
            mat_khau = input("Mật khẩu: ")
            if ten_tai_khoan == "admin" and mat_khau == "admin123":
                print("\nĐăng nhập thành công!")
                admin()
                
            tim_thay = False
            for tai_khoan in danh_sach_dki:
                if tai_khoan ['Tên tài khoản'] == ten_tai_khoan and tai_khoan['Mật khẩu'] == mat_khau:
                    tim_thay = True
                    print("Đăng nhập thành công!")
                    break
            if tim_thay:
                khanh_hang()   
            else:
                print("Sai tên tài khoản hoặc mật khẩu.")
        
        elif lua_chon == 2:
            print("\n========== Đăng ký tài khoản ==========")
            ten_tai_khoan = input("Nhập tên tài khoản: ")
            kiem_tra = False
            for nguoi_dung in danh_sach_dki:
                if ten_tai_khoan == nguoi_dung ['Tên tài khoản']:
                    kiem_tra = True
                    break
                
            if kiem_tra:
                print("Tên tài khoản đã tồn tại")
                
            mat_khau = input("Nhập mật khẩu: ")
            for nguoi_dung in danh_sach_dki:
                if ten_tai_khoan == nguoi_dung ['Mật khẩu']:
                    kiem_tra = True
                    break
            if kiem_tra:
                print("Mật khẩu đã tồn tại")
                
            else:
                tim_thay = False
                for tai_khoan in danh_sach_dki: 
                    if tai_khoan['Mật khẩu'] == mat_khau and tai_khoan['Tên tài khoản'] == ten_tai_khoan:
                        tim_thay = True
                        print("Đăng ký thành công!")
                    danh_sach_dki.append({
                        "Tên tài khoản": ten_tai_khoan,
                        "Mật khẩu": mat_khau
                    })
                    with open("login.json", "w", encoding="utf-8") as f:
                            json.dump(danh_sach_dki, f, ensure_ascii=False, indent=4)
                            break
                khanh_hang()
            
        elif lua_chon == 3:
           kiem_tra_thoat() == True
           print("Đã thoát trương trình!")
           break

            

