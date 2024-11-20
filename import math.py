import math
 
def print_sin_wave(amplitude, period, width, height):
    # 创建一个二维字符数组来存储图像
    image = [[' ' for _ in range(width)] for _ in range(height)]
 
    # 缩放因子，将sin函数的值映射到图像的高度
    scale_y = height / (2 * amplitude)
    # 缩放因子，将x值映射到图像的宽度
    scale_x = width / period
 
    # 遍历图像的每一列
    for x in range(width):
        # 将x值转换为sin函数的输入值
        theta = 2 * math.pi * (x / period)
        # 计算sin函数的值
        y = amplitude * math.sin(theta)
        # 将sin函数的值映射到图像的行
        row = int(height / 2 - y * scale_y)
 
        # 确保行值在有效范围内
        if 0 <= row < height:
            # 使用字符 '*' 来表示sin函数的值
            image[row][x] = '*'
 
    # 打印图像
    for row in image:
        print(''.join(row))
 
# 参数设置
amplitude = 10  # 振幅
period = 40     # 周期
width = 80      # 图像宽度
height = 20     # 图像高度
 
# 打印sin函数图像
print_sin_wave(amplitude, period, width, height)