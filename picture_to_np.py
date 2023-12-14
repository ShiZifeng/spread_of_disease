import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve2d

# 读取图片
img = cv2.imread('D:/YAN1/feixianxing/R-C.jpg', cv2.IMREAD_GRAYSCALE)

# 缩放图片
img = cv2.resize(img, (1000, 1000))
img2 = cv2.resize(img, (100, 100))

# 二值化处理
_, img_binary = cv2.threshold(img, 50, 1, cv2.THRESH_BINARY)
_, mask = cv2.threshold(img2, 1, 1, cv2.THRESH_BINARY_INV)

# 转换为浮点数类型
img_binary = img_binary.astype(float)
mask = mask.astype(float)

# # 创建卷积核
# kernel = np.array([[0, 1, 0],
#                    [1, 1, 1],
#                    [0, 1, 0]])

# # 进行卷积操作
# img_binary = convolve2d(img_binary, kernel, mode='same', boundary='fill', fillvalue=0)
# img_binary = (img_binary > 0).astype(float)

# img_binary = convolve2d(img_binary, kernel, mode='same', boundary='fill', fillvalue=0)


# # 将大于1的值设置为1
# img_binary = (img_binary > 0).astype(float)

# 反转二值化数组
# img_binary = np.logical_not(img_binary)

# 绘制二值化数组
plt.imshow(img_binary, cmap='gray')
plt.show()
plt.imshow(mask, cmap='gray')
plt.show()

# 保存二维数组为文本文件
np.savetxt('img_binary.txt', img_binary)
np.savetxt('mask.txt', mask)