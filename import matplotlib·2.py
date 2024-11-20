import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 创建一个新的图形和坐标轴
fig, ax = plt.subplots()

# 设置背景
ax.set_facecolor('white')

# 绘制头发
hair = patches.PathPatch(
    plt.Path([[0.1, 0.8], [0.3, 0.9], [0.5, 0.7], [0.7, 0.9], [0.9, 0.8]]),
    facecolor='pink', edgecolor='pink', lw=0
)
ax.add_patch(hair)

# 绘制左眼
eye_left = patches.Circle((0.25, 0.7), 0.05, color='blue', clip_on=False)
ax.add_patch(eye_left)
pupil_left = patches.Circle((0.25, 0.7), 0.02, color='black', clip_on=False)
ax.add_patch(pupil_left)

# 绘制右眼
eye_right = patches.Circle((0.75, 0.7), 0.05, color='blue', clip_on=False)
ax.add_patch(eye_right)
pupil_right = patches.Circle((0.75, 0.7), 0.02, color='black', clip_on=False)
ax.add_patch(pupil_right)

# 绘制鼻子
nose = patches.Polygon([[0.5, 0.65], [0.55, 0.6], [0.45, 0.6]], closed=True, color='pink')
ax.add_patch(nose)

# 绘制嘴巴
mouth = patches.Polygon([[0.4, 0.55], [0.5, 0.5], [0.6, 0.55]], closed=True, color='pink')
ax.add_patch(mouth)

# 绘制衣领
collar = patches.Polygon([[0.2, 0.8], [0.8, 0.8], [0.8, 0.9], [0.2, 0.9]], closed=True, color='pink')
ax.add_patch(collar)

# 设置图形的边界
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# 隐藏坐标轴
ax.axis('off')

# 显示图形
plt.show()