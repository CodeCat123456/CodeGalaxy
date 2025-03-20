import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用SimHei字体（黑体）
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # x值范围
y_sin = np.sin(x)  # 正弦值

x_discrete = np.arange(-2 * np.pi, 2 * np.pi + 0.5, 0.5)
y_discrete = np.sin(x_discrete) #计算离散点值

#正弦曲线
plt.figure(figsize=(10,6))
plt.plot(x, y_sin, label='sin(x)',color='blue')
plt.title("Sin Function")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()  # 显示图例
plt.show()

#离散信号
plt.figure(figsize=(10,6))
plt.scatter(x_discrete, y_discrete, color='red')
plt.title("离散正弦信号")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()  # 显示图例
plt.show()