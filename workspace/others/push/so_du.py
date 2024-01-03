import random

for i in range(10):
    so_3_chu_so = random.randint(100, 999)
    so_1_chu_so = random.randint(1, 9)
    ket_qua_chia = so_3_chu_so // so_1_chu_so
    du = so_3_chu_so % so_1_chu_so
    print(f"{so_3_chu_so} / {so_1_chu_so} = {ket_qua_chia} dư {du}")
