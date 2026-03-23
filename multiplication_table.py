# 99乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        # 格式化输出，保持对齐
        print(f"{j} × {i} = {i*j:2}", end="  ")
    print()  # 换行
