def print_pascals_triangle(num_rows):
    # 初始化一个空列表来存储杨辉三角形的每一行
    triangle = []
 
    # 逐行生成杨辉三角形
    for i in range(num_rows):
        # 每一行开始都是一个1
        row = [1] * (i + 1)
        # 中间的元素是上方两个元素之和
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        # 将当前行添加到三角形中
        triangle.append(row)
 
    # 打印杨辉三角形
    max_width = len(" ".join(map(str, triangle[-1])))  # 计算最后一行的最大宽度
    for row in triangle:
        # 居中打印每一行，前面填充空格
        print(" " * ((max_width - len(" ".join(map(str, row)))) // 2) + " ".join(map(str, row)))
 
# 设置要打印的行数
num_rows = 10
 
# 打印杨辉三角形
print_pascals_triangle(num_rows)