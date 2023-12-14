import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

# 参数设置
f0 = 0.05  # 正常人的感染率
f1 = 0.001  # 感染者的死亡率
f2 = 0.1  # 感染者在没有死亡下的治愈率
f3 = 0.02  # 治愈者再次被感染的几率

# 初始化人群矩阵
S = np.ones((1000, 1000))
S[499, 499] = 2  # 设置初始感染者位置

# 初始化颜色矩阵
C = np.zeros((1002, 1002, 3))
C[1:1001, 1:1001, 0] = (S == 2)
C[1:1001, 1:1001, 1] = (S == 1)

# 初始化时间
t = 0

while t < 10000:
    t += 1

    # 计算周围感染者数量
    Su = convolve2d((S==2).astype(int), np.ones((3,3)), mode='same', boundary='fill', fillvalue=0)
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
    C[1:1001,1:1001,0] = (S == 2).astype(int)
    C[1:1001,1:1001,1] = (S == 1).astype(int) + 0.5 * (S == 1.1).astype(int)

    # 绘制
    plt.clf()
    plt.imshow(C, interpolation='nearest')
    plt.pause(0.01)