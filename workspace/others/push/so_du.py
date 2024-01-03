import random

for i in range(10):
    # Tạo một số có 3 chữ số
    so_3_chu_so = random.randint(100, 999)

    # Tạo một số có 1 chữ số
    so_1_chu_so = random.randint(1, 9)

    # Thực hiện phép chia có dư
    ket_qua_chia = so_3_chu_so // so_1_chu_so
    du = so_3_chu_so % so_1_chu_so

    # In kết quả
    print(f"{so_3_chu_so} / {so_1_chu_so} = {ket_qua_chia} dư {du}")
