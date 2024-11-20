import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 创建一个新的图形和坐标轴
fig, ax = plt.subplots()

# 设置背景
ax.set_facecolor('black')

# 绘制头部
head = patches.Circle((0.5, 0.5), 0.3, color='purple')
ax.add_patch(head)

# 绘制眼睛
eye_left = patches.Circle((0.4, 0.6), 0.03, color='white')
ax.add_patch(eye_left)
eye_right = patches.Circle((0.6, 0.6), 0.03, color='white')
ax.add_patch(eye_right)

# 绘制鼻子
nose = patches.Polygon([[0.5, 0.55], [0.52, 0.52], [0.48, 0.52]], closed=True, color='purple')
ax.add_patch(nose)

# 绘制嘴巴
mouth = patches.Polygon([[0.48, 0.58], [0.52, 0.58], [0.5, 0.62]], closed=True, color='purple')
ax.add_patch(mouth)

# 绘制衣服
shirt = patches.Rectangle((0.3, 0.7), 0.4, 0.2, color='pink')
ax.add_patch(shirt)
collar = patches.Polygon([[0.3, 0.7], [0.7, 0.7], [0.5, 0.8]], closed=True, color='purple')
ax.add_patch(collar)

# 设置图形的边界
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# 隐藏坐标轴
ax.axis('off')

# 显示图形
plt.show()