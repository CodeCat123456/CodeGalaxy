import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用SimHei字体（黑体）
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

class SignalWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("基本离散信号演示")
        self.setMinimumSize(1000, 600)

    def initUI(self):
        #----- 创建布局
        main_layout = QHBoxLayout()      # 主布局：水平排列（左侧按钮，右侧图形）
        button_layout = QVBoxLayout()    # 按钮布局：垂直排列
        
        #----- 创建按钮
        self.btn_impulse = QPushButton("单位脉冲信号", self)
        self.btn_step = QPushButton("单位阶跃信号", self)
        self.btn_ramp = QPushButton("斜坡信号", self)
        self.btn_exponential = QPushButton("指数信号", self)
        self.btn_sinusoidal = QPushButton("正弦信号", self) 
        
        #----- 将按钮添加到布局
        button_layout.addWidget(self.btn_impulse)
        button_layout.addWidget(self.btn_step)
        button_layout.addWidget(self.btn_ramp)
        button_layout.addWidget(self.btn_exponential)
        button_layout.addWidget(self.btn_sinusoidal)  
        button_layout.addStretch()                    # 添加弹性空间使按钮靠上对齐
        
        #----- 创建Matplotlib图形
        self.figure = Figure(figsize=(8, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)       # 将Figure转换为Qt组件
        self.axes = self.figure.add_subplot(111)
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        #----- 右侧图形布局
        plot_layout = QVBoxLayout()
        plot_layout.addWidget(self.toolbar)
        plot_layout.addWidget(self.canvas)
        
        #----- 合并布局
        main_layout.addLayout(button_layout, 1)      # 左侧按钮布局占1份宽度
        main_layout.addLayout(plot_layout, 4)        # 右侧图形布局占4份宽度
        self.setLayout(main_layout)                  # 应用主布局
         
        #----- 连接信号槽
        # 将按钮点击事件与绘图方法绑定
        self.btn_impulse.clicked.connect(self.plot_impulse)
        self.btn_step.clicked.connect(self.plot_step)
        self.btn_ramp.clicked.connect(self.plot_ramp)
        self.btn_exponential.clicked.connect(self.plot_exponential)
        self.btn_sinusoidal.clicked.connect(self.plot_sinusoidal)  # 新连接
        
        #----- 初始显示脉冲信号
        self.plot_impulse()

    def plot_signal(self, n, x, title):
        """通用绘图函数"""
        self.axes.clear()
        self.axes.stem(n, x, linefmt='C0-', markerfmt='C0o', basefmt='C7-')# 线样式：蓝色实线 标记样式：蓝色圆圈 基线样式：灰色虚线
        self.axes.set_title(title)
        self.axes.set_xlabel("n")
        self.axes.set_ylabel("x[n]")
        self.axes.grid(True, linestyle='--', alpha=0.6)   # 显示虚线网格
        self.canvas.draw()  # 刷新画布

    def plot_impulse(self):
        n = np.arange(-10, 10)
        x = np.zeros_like(n)
        x[n == 0] = 1
        self.plot_signal(n, x, "单位脉冲信号 δ[n]")

    def plot_step(self):
        n = np.arange(-10, 10)
        x = np.zeros_like(n)
        x[n >= 0] = 1
        self.plot_signal(n, x, "单位阶跃信号 u[n]")

    def plot_ramp(self):
        n = np.arange(-10, 10)
        x = np.zeros_like(n)
        x[n >= 0] = n[n >= 0]
        self.plot_signal(n, x, "斜坡信号 r[n]")

    def plot_exponential(self):
        n = np.arange(-10, 10)
        x = np.zeros_like(n, dtype=float)
        x[n >= 0] = 0.5**n[n >= 0]
        self.plot_signal(n, x, "指数信号 0.5^n u[n]")

    def plot_sinusoidal(self):
        """新增正弦信号绘图方法"""
        n = np.arange(-10, 20)
        f = 0.05  # 设置信号频率
        omega = 2 * np.pi * f  # 计算角频率
        x = np.sin(omega * n)
        self.plot_signal(n, x, r"正弦信号 $\sin(0.1\pi n)$")

#-----程序入口
if __name__ == "__main__":
    app = QApplication(sys.argv)    # 创建Qt应用
    window = SignalWindow()         # 创建主窗口实例
    window.show()                   # 显示窗口
    sys.exit(app.exec())            # 进入主事件循环