# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        # 使用 end 参数，避免每次打印后换行
        print(f"{j}*{i}={i * j}", end="\t")
    # 每打印完一行后换行
    print()
