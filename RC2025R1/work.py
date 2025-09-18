import matplotlib, numpy, matplotlib.pyplot as plt # noqa
matplotlib.use('TkAgg')  # 使用TkAgg后端

#本代码在https://github.com/Enecell/CURC-Robocon2025-Volleyball_FJUT开源
#在闲鱼购买请联系原作者LL3323126216@163.com+

#根据自己的机械尺寸修改相应的变量
#示例数据
R = 120 #静平面半径
r = 110 #动平面半径
L = 180#主动臂长度
La = 200 #从动臂长度


def Delta_works(theta_1, theta_2, theta_3):
    theta_1__ = numpy.pi * theta_1 / 180
    theta_2__ = numpy.pi * theta_2 / 180
    theta_3__ = numpy.pi * theta_3 / 180

    A1 = R + L * numpy.cos(theta_1__) - r
    B1 = 1
    C1 = L * numpy.sin(theta_1__)

    A2 = -(1 / 2) * (R + L * numpy.cos(theta_2__) - r)
    B2 = (numpy.sqrt(3) / 2) * (R + L * numpy.cos(theta_2__) - r)
    C2 = L * numpy.sin(theta_2__)

    A3 = -(1 / 2) * (R + L * numpy.cos(theta_3__) - r)
    B3 = -(numpy.sqrt(3) / 2) * (R + L * numpy.cos(theta_3__) - r)
    C3 = L * numpy.sin(theta_3__)

    D1 = (1 / 2) * (A2 * A2 - A1 * A1 + C2 * C2 - C1 * C1 + B2 * B2)

    A21 = A2 - A1
    C21 = C2 - C1

    D2 = (1 / 2) * (A3 * A3 - A1 * A1 + C3 * C3 - C1 * C1 + B3 * B3)

    A31 = A3 - A1
    C31 = C3 - C1

    E1 = (B3 * C21 - B2 * C31) / (A21 * B3 - A31 * B2)
    F1 = (B3 * D1 - B2 * D2) / (A21 * B3 - A31 * B2)

    E2 = (A31 * C21 - A21 * C31) / (A31 * B2 - A21 * B3)
    F2 = (A31 * D1 - A21 * D2) / (A31 * B2 - A21 * B3)

    a = E1 * E1 + E2 * E2 + 1
    b = 2 * E2 * F2 + 2 * C1 - 2 * E1 * (A1 - F1)
    c = (A1 - F1) * (A1 - F1) + F2 * F2 + C1 * C1 - La * La

    Z = (-b - numpy.sqrt(b * b - 4 * a * c)) / (2 * a)
    X = E1 * Z + F1
    Y = E2 * Z + F2
    return X, Y, Z

#作图精度设置
#输入参数依次为：初始角度，最大可旋转角度，坐标轴上每个点的角度间隔（类似最小分度值，值给的太小可能导致崩溃）
theta_1_ = numpy.arange(0, 85.0, 0.25)
theta_2_ = numpy.arange(0, 85.0, 0.25)
theta_3_ = numpy.arange(0, 85.0, 0.25)

theta23, theta32 = numpy.meshgrid(theta_2_, theta_3_)

fig = plt.figure(1, figsize=(8, 7))


#建议单次运行只启动其中一种作图程序，将另一端程序注释掉

#三位工作空间图
'''ax = fig.add_subplot(projection='3d')
ax.set_top_view()
for item in theta_1_:
    x, y, z = Delta_works(item, theta23, theta32)
    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='rainbow')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
plt.show()'''

#二维工作空间图
ax = fig.add_subplot()
for item in theta_1_:
    x, y, z = Delta_works(item, theta23, theta32)
    ax.plot(y, z, )
    ax.set_xlabel('y')
    ax.set_ylabel('z')
    ax.grid(True)
plt.show()





#本代码在https://github.com/Enecell/CURC-Robocon2025-Volleyball_FJUT开源
# 在闲鱼购买请联系原作者LL3323126216@163.com+