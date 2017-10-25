import matplotlib.pyplot as xp
import numpy as np
from math import *
import random


list_x = []
list_y = []
# Absolute Value
gravity = 9.80665
colors = ['#12efff', '#eee111', '#eee00f', '#e00fff', '#123456', '#abc222', '#000000', '#123fff', '#1eff1f', '#2edf4f',
          '#2eaf9f', '#22222f', '#eeeff1', '#eee112', '#00ef00', '#aa0000', '#0000aa', '#000999', '#32efff', '#23ef68',
          '#2e3f56', '#7eef1f', '#eeef11']
C = random.randint(0, 22)


def coor_y(ini_v, time, angle):
    global gravity
    return (ini_v * time) * sin(radians(angle)) - (0.5 * gravity) * time ** 2


def coor_x(ini_v, time, angle):
    return (ini_v * time) * cos(radians(angle))


for i in range(int(input("Number of test projectiles? : "))):

    init_vel = int(input("Initial velocity of projectile {}: ".format(i + 1)))
    angle = int(input("Angle of projectile {}: ".format(i + 1)))

    for t in np.arange(0.0, 450, 0.01):
        value_x = coor_x(init_vel, t, angle)
        value_y = coor_y(init_vel, t, angle)

        if value_y >= 0:

            list_x.append(value_x)
            list_y.append(value_y)

    xp.plot(list_x, list_y, c=colors[C])
    xp.title("Projectile Test", fontsize=30)
    xp.xlabel("x(in meter)", fontsize=10)
    xp.ylabel("y(in meter)", fontsize=10)

    del list_x[0:]
    del list_y[0:]

xp.show()


