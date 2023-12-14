import os
import cv2
import imageio

# 获取文件夹下的所有文件名
folder = 'results/scatter'  # 你的文件夹路径
filenames = [os.path.join(folder, file) for file in os.listdir(folder) if file.endswith('.png')]

# 使用 cv2 库来读取图片
images = [cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2RGB) for filename in filenames]

# 使用 imageio 库来将图片保存为 GIF
imageio.mimsave('output_scatter.gif', images, duration=0.5)

# 获取文件夹下的所有文件名
folder = 'results/scatter2'  # 你的文件夹路径
filenames = [os.path.join(folder, file) for file in os.listdir(folder) if file.endswith('.png')]

# 使用 cv2 库来读取图片
images = [cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2RGB) for filename in filenames]

# 使用 imageio 库来将图片保存为 GIF
imageio.mimsave('output_scatter2.gif', images, duration=0.5)

# 获取文件夹下的所有文件名
folder = 'results/spread'  # 你的文件夹路径
filenames = [os.path.join(folder, file) for file in os.listdir(folder) if file.endswith('.png')]

# 使用 cv2 库来读取图片
images = [cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2RGB) for filename in filenames]

# 使用 imageio 库来将图片保存为 GIF
imageio.mimsave('output_spread.gif', images, duration=0.5)