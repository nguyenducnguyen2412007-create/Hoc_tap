chuoi = input("Nhập một chuỗi: ")
in_hoa = 0
in_thuong = 0
so = 0
for ki_tu in chuoi:
    if ki_tu.isupper():
        in_hoa += 1
    elif ki_tu.islower():
        in_thuong += 1
    elif ki_tu.isdigit():
        so += 1
print(f"Số ký tự in hoa: {in_hoa}")
print(f"Số ký tự in thường: {in_thuong}")
print(f"Số ký tự số: {so}")        