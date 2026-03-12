chuoi= input("Nhập câu bất kì: ")
tim_thay= False
print(f"Vị trí của chữu cái a là:")
for i, char in enumerate(chuoi):
    if char.lower() == 'a': 
        print(f"- Tìm thấy tại vị trí: {i}")
        tim_thay = True
if not tim_thay:
    print("Không tìm thấy chữ 'a' nào trong chuỗi của bạn.")