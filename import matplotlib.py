import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 创建一个新的图形和坐标轴
fig, ax = plt.subplots()

# 设置背景颜色
ax.set_facecolor('#000000')

# 绘制头发
ax.add_patch(patches.Polygon([[0.1, 0.8], [0.3, 0.9], [0.7, 0.9], [0.9, 0.8]], color='#FFC0CB'))

# 绘制眼睛
ax.add_patch(patches.Circle((0.25, 0.7), 0.05, color='#0000FF'))
ax.add_patch(patches.Circle((0.75, 0.7), 0.05, color='#0000FF'))

# 绘制瞳孔
ax.add_patch(patches.Circle((0.265, 0.7), 0.02, color='#FFFFFF'))
ax.add_patch(patches.Circle((0.735, 0.7), 0.02, color='#FFFFFF'))

# 绘制鼻子
ax.add_patch(patches.Polygon([[0.5, 0.65], [0.55, 0.6], [0.45, 0.6]], color='#FFC0CB'))

# 绘制嘴巴
ax.add_patch(patches.Arc((0.5, 0.5), 0.2, 0.1, angle=0, theta1=0, theta2=180, color='#FFC0CB'))

# 隐藏坐标轴
ax.axis('off')

# 显示图形
plt.show()
