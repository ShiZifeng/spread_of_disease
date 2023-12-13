import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy

# 参数设置
f0 = 0.6
f1 = 0.005
f2 = 0.01
f3 = 0.01

# 初始化人群矩阵
S = np.ones((1002, 1002))
S[501, 501] = 2

# 初始化颜色矩阵
C = np.zeros((1002, 1002, 3))

# 初始化时间
t = 0

# 动画更新函数
def update(data):
    global S, C, t
    t += 1

    # 计算周围感染者数量
    Su = scipy.ndimage.convolve2d((S==2).astype(int), np.ones((3,3)), mode='same', boundary='fill', fillvalue=0)
    Su -= (S==2).astype(int)

    # 正常人感染
    mask = (Su > 0.5) & (S == 1)
    S[mask] = np.random.rand(np.sum(mask)) < f0

    # 治愈者再次感染
    mask = (Su > 0.5) & (S == 1.1)
    S[mask] = np.random.rand(np.sum(mask)) < f3

    # 感染者死亡
    mask = S == 2
    S[mask] = np.random.rand(np.sum(mask)) < f1

    # 感染者治愈
    mask = S == 2
    S[mask] = np.random.rand(np.sum(mask)) < f2

    # 更新颜色矩阵
    C[:,:,0] = (S == 2).astype(int)
    C[:,:,1] = (S == 1).astype(int) + 0.5 * (S == 1.1).astype(int)

    # 绘制
    plt.clf()
    plt.imshow(C, interpolation='nearest')

# 创建动画
ani = animation.FuncAnimation(plt.gcf(), update, interval=10)

plt.show()